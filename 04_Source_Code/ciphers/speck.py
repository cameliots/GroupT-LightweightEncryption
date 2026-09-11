"""SPECK 64/128 in CTR mode — lightweight ARX block cipher.

SPECK is a family of lightweight block ciphers designed for efficient operation
on constrained computing platforms. It uses only addition, rotation and XOR
(ARX) operations, which support efficient software implementation and low
computational overhead. Radhakrishnan et al. (2024) reported strong efficiency
for SPECK on constrained IoT boards, which is the finding this study tests under
its own controlled conditions.

The 64/128 variant is used here: a 64-bit block with a 128-bit key, giving the
same block size as PRESENT and the same key size as AES-128.

Reference:
    Beaulieu, R., Shors, D., Smith, J., Treatman-Clark, S., Weeks, B., &
    Wingers, L. (2013). The SIMON and SPECK families of lightweight block
    ciphers. IACR Cryptology ePrint Archive, Report 2013/404.
    https://eprint.iacr.org/2013/404

Implementation note:
    Reference implementation written for this comparative study. Not
    constant-time; must not be used to protect real data.
"""

from __future__ import annotations

from .base import Cipher, ctr_keystream_xor

WORD_BITS = 32
MASK = 0xFFFFFFFF
ALPHA = 8   # right-rotation amount in the round function
BETA = 3    # left-rotation amount in the round function
NUM_ROUNDS = 27
KEY_WORDS = 4  # m, the number of key words for the 128-bit key
BLOCK_BYTES = 8


def _ror(value: int, amount: int) -> int:
    return ((value >> amount) | (value << (WORD_BITS - amount))) & MASK


def _rol(value: int, amount: int) -> int:
    return ((value << amount) | (value >> (WORD_BITS - amount))) & MASK


def expand_key(key: bytes) -> list[int]:
    """Generate 27 round keys from a 128-bit key.

    The key is parsed as four 32-bit big-endian words (l2, l1, l0, k0), matching
    the convention used in the SIMON and SPECK paper's test vectors.
    """
    if len(key) != 16:
        raise ValueError(f"SPECK 64/128 requires a 16-byte key, got {len(key)}")

    words = [int.from_bytes(key[i * 4:(i + 1) * 4], "big") for i in range(4)]
    # words == [l2, l1, l0, k0] as written in the paper.
    k = [words[3]]
    ell = [words[2], words[1], words[0]]

    for i in range(NUM_ROUNDS - 1):
        new_l = ((k[i] + _ror(ell[i], ALPHA)) & MASK) ^ i
        ell.append(new_l)
        k.append(_rol(k[i], BETA) ^ new_l)

    return k


def encrypt_block(block: bytes, round_keys: list[int]) -> bytes:
    """Encrypt one 8-byte block."""
    x = int.from_bytes(block[:4], "big")
    y = int.from_bytes(block[4:], "big")

    for rk in round_keys:
        x = ((_ror(x, ALPHA) + y) & MASK) ^ rk
        y = _rol(y, BETA) ^ x

    return x.to_bytes(4, "big") + y.to_bytes(4, "big")


def decrypt_block(block: bytes, round_keys: list[int]) -> bytes:
    """Decrypt one 8-byte block.

    Not used by CTR mode, but provided so the implementation can be verified
    against the published test vectors in both directions.
    """
    x = int.from_bytes(block[:4], "big")
    y = int.from_bytes(block[4:], "big")

    for rk in reversed(round_keys):
        y = _ror(x ^ y, BETA)
        x = _rol((x ^ rk) - y & MASK, ALPHA)

    return x.to_bytes(4, "big") + y.to_bytes(4, "big")


class Speck64_128(Cipher):
    """SPECK 64/128 operated in CTR mode."""

    name = "SPECK-64/128"
    key_size = 16
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
