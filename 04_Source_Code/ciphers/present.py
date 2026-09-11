"""PRESENT-80 in CTR mode — ultra-lightweight block cipher.

PRESENT is an ultra-lightweight block cipher designed for highly constrained
environments. It uses a 64-bit block size and an 80-bit key, and its compact
design focuses on reducing hardware requirements while maintaining suitable
security characteristics. It is included in this study to represent the
hardware-oriented end of the lightweight design space.

Reference:
    Bogdanov, A., Knudsen, L. R., Leander, G., Paar, C., Poschmann, A.,
    Robshaw, M. J. B., Seurin, Y., & Vikkelsoe, C. (2007). PRESENT: An
    ultra-lightweight block cipher. In Cryptographic Hardware and Embedded
    Systems - CHES 2007 (pp. 450-466). Springer.
    https://doi.org/10.1007/978-3-540-74735-2_31

Implementation note:
    Reference implementation written for this comparative study. Not
    constant-time; must not be used to protect real data.
"""

from __future__ import annotations

from .base import Cipher, ctr_keystream_xor

#: PRESENT 4-bit S-box (CHES 2007, Table 1).
SBOX = (0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD, 0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2)

#: Inverse S-box, used by the block decryption routine.
SBOX_INV = [0] * 16
for _i, _v in enumerate(SBOX):
    SBOX_INV[_v] = _i
SBOX_INV = tuple(SBOX_INV)

NUM_ROUNDS = 31
BLOCK_BYTES = 8
MASK64 = 0xFFFFFFFFFFFFFFFF


def _build_pbox() -> tuple[int, ...]:
    """Bit permutation: P(i) = i*16 mod 63, with P(63) = 63."""
    table = []
    for i in range(64):
        table.append(63 if i == 63 else (i * 16) % 63)
    return tuple(table)


PBOX = _build_pbox()
PBOX_INV = [0] * 64
for _i, _v in enumerate(PBOX):
    PBOX_INV[_v] = _i
PBOX_INV = tuple(PBOX_INV)


def _sbox_layer(state: int, box=SBOX) -> int:
    """Apply the 4-bit S-box to each of the 16 nibbles."""
    out = 0
    for i in range(16):
        out |= box[(state >> (4 * i)) & 0xF] << (4 * i)
    return out


def _pbox_layer(state: int, table=PBOX) -> int:
    """Apply the bit permutation."""
    out = 0
    for i in range(64):
        if (state >> i) & 1:
            out |= 1 << table[i]
    return out


def expand_key(key: bytes) -> list[int]:
    """Generate 32 round keys from an 80-bit key (CHES 2007, Section 3).

    The key register holds 80 bits. Each round takes the leftmost 64 bits as the
    round key, then rotates the register left by 61, applies the S-box to the top
    nibble, and XORs the round counter into bits 19..15.
    """
    if len(key) != 10:
        raise ValueError(f"PRESENT-80 requires a 10-byte key, got {len(key)}")

    reg = int.from_bytes(key, "big")  # 80-bit key register
    round_keys = []

    for rnd in range(1, NUM_ROUNDS + 2):
        round_keys.append((reg >> 16) & MASK64)

        # Rotate the 80-bit register left by 61 positions.
        reg = ((reg << 61) | (reg >> 19)) & ((1 << 80) - 1)
        # S-box the most significant nibble.
        reg = (reg & ~(0xF << 76)) | (SBOX[(reg >> 76) & 0xF] << 76)
        # XOR the round counter into bits 19..15.
        reg ^= rnd << 15

    return round_keys


def encrypt_block(block: bytes, round_keys: list[int]) -> bytes:
    """Encrypt one 8-byte block."""
    state = int.from_bytes(block, "big")

    for rnd in range(NUM_ROUNDS):
        state ^= round_keys[rnd]
        state = _sbox_layer(state)
        state = _pbox_layer(state)

    state ^= round_keys[NUM_ROUNDS]
    return state.to_bytes(8, "big")


def decrypt_block(block: bytes, round_keys: list[int]) -> bytes:
    """Decrypt one 8-byte block.

    Not used by CTR mode, but provided so the implementation can be verified
    against the published test vectors in both directions.
    """
    state = int.from_bytes(block, "big")
    state ^= round_keys[NUM_ROUNDS]

    for rnd in range(NUM_ROUNDS - 1, -1, -1):
        state = _pbox_layer(state, PBOX_INV)
        state = _sbox_layer(state, SBOX_INV)
        state ^= round_keys[rnd]

    return state.to_bytes(8, "big")


class Present80(Cipher):
    """PRESENT-80 operated in CTR mode."""

    name = "PRESENT-80"
    key_size = 10
    nonce_size = 4
    block_size = BLOCK_BYTES
    category = "Lightweight"
    mode = "CTR"

    def _stream(self, key: bytes, nonce: bytes, data: bytes) -> bytes:
        round_keys = expand_key(key)
        return ctr_keystream_xor(
            lambda blk: encrypt_block(blk, round_keys),
            BLOCK_BYTES,
            nonce,
            data,
        )

    def encrypt(self, key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
        return self._stream(key, nonce, plaintext)

    def decrypt(self, key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
        return self._stream(key, nonce, ciphertext)
