"""AES-128 in CTR mode — the conventional baseline for this study.

AES is included as the reference point because it is the most widely used
symmetric encryption standard and is commonly adopted as a comparison point in
lightweight cryptography research, including Radhakrishnan et al. (2024). It
represents "conventional cryptography" as distinguished from the lightweight
category comprising PRESENT, SPECK and ASCON.

Reference:
    National Institute of Standards and Technology. (2001). Advanced Encryption
    Standard (AES). FIPS PUB 197. https://doi.org/10.6028/NIST.FIPS.197

Implementation note:
    This is a reference implementation written for the comparative study. All
    four ciphers in this repository are implemented in the same language and
    runtime so that the measured differences reflect the algorithms rather than
    differences in library optimisation. See 03_Architecture_and_Flowchart/
    Research_Methodology.md for the justification.

    It is NOT constant-time and must not be used to protect real data.
"""

from __future__ import annotations

from .base import Cipher, ctr_keystream_xor

# ---------------------------------------------------------------------------
# S-box (FIPS-197, Figure 7)
# ---------------------------------------------------------------------------
SBOX = bytes([
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
])

#: Round constants for the key schedule (FIPS-197, Section 5.2).
RCON = (0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36)

NUM_ROUNDS = 10
BLOCK_BYTES = 16


def _xtime(value: int) -> int:
    """Multiply by x (0x02) in GF(2^8) with the AES reduction polynomial."""
    value <<= 1
    if value & 0x100:
        value ^= 0x11B
    return value & 0xFF


# Precomputed multiplication tables for MixColumns. Building these once at import
# time keeps the per-block work representative of the cipher rather than of
# repeated GF arithmetic in the interpreter.
MUL2 = bytes(_xtime(i) for i in range(256))
MUL3 = bytes(_xtime(i) ^ i for i in range(256))


def expand_key(key: bytes) -> list[bytes]:
    """Expand a 16-byte key into 11 round keys (FIPS-197, Section 5.2)."""
    if len(key) != 16:
        raise ValueError(f"AES-128 requires a 16-byte key, got {len(key)}")

    words = [list(key[i * 4:(i + 1) * 4]) for i in range(4)]

    for i in range(4, 4 * (NUM_ROUNDS + 1)):
        temp = list(words[i - 1])
        if i % 4 == 0:
            # RotWord, SubWord, then XOR with the round constant.
            temp = temp[1:] + temp[:1]
            temp = [SBOX[b] for b in temp]
            temp[0] ^= RCON[i // 4 - 1]
        words.append([words[i - 4][j] ^ temp[j] for j in range(4)])

    return [
        bytes(words[4 * r][j] for j in range(4)) +
        bytes(words[4 * r + 1][j] for j in range(4)) +
        bytes(words[4 * r + 2][j] for j in range(4)) +
        bytes(words[4 * r + 3][j] for j in range(4))
        for r in range(NUM_ROUNDS + 1)
    ]


def encrypt_block(block: bytes, round_keys: list[bytes]) -> bytes:
    """Encrypt one 16-byte block with the expanded round keys."""
    state = bytearray(a ^ b for a, b in zip(block, round_keys[0]))

    for rnd in range(1, NUM_ROUNDS + 1):
        # SubBytes
        for i in range(16):
            state[i] = SBOX[state[i]]

        # ShiftRows — the state is column-major, so row r is at indices r, r+4, ...
        state[1], state[5], state[9], state[13] = state[5], state[9], state[13], state[1]
        state[2], state[6], state[10], state[14] = state[10], state[14], state[2], state[6]
        state[3], state[7], state[11], state[15] = state[15], state[3], state[7], state[11]

        # MixColumns — omitted in the final round (FIPS-197, Section 5.1)
        if rnd != NUM_ROUNDS:
            for c in range(0, 16, 4):
                a0, a1, a2, a3 = state[c], state[c + 1], state[c + 2], state[c + 3]
                state[c] = MUL2[a0] ^ MUL3[a1] ^ a2 ^ a3
                state[c + 1] = a0 ^ MUL2[a1] ^ MUL3[a2] ^ a3
                state[c + 2] = a0 ^ a1 ^ MUL2[a2] ^ MUL3[a3]
                state[c + 3] = MUL3[a0] ^ a1 ^ a2 ^ MUL2[a3]

        # AddRoundKey
        rk = round_keys[rnd]
        for i in range(16):
            state[i] ^= rk[i]

    return bytes(state)


class AES128(Cipher):
    """AES-128 operated in CTR mode."""

    name = "AES-128"
    key_size = 16
    nonce_size = 8
    block_size = BLOCK_BYTES
    category = "Conventional"
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
        # CTR mode is symmetric: encryption and decryption are the same operation.
        return self._stream(key, nonce, ciphertext)
