"""ASCON-128 authenticated encryption — NIST lightweight cryptography standard.

ASCON is a lightweight cryptographic family designed for constrained devices. It
provides authenticated encryption, which delivers confidentiality and integrity
within a single cryptographic construction. NIST standardised the ASCON family
for lightweight cryptography in SP 800-232 (2025), which is the development that
motivates its inclusion in this study.

ASCON-128 parameters: 128-bit key, 128-bit nonce, 128-bit tag, 64-bit rate,
12 initialisation/finalisation rounds and 6 rounds per data block.

Reference:
    Turan, M. S., McKay, K., Kang, J., Kelsey, J., & Chang, D. (2025).
    Ascon-based lightweight cryptography standards for constrained devices:
    Authenticated encryption, hash, and extendable output functions. NIST.
    https://doi.org/10.6028/NIST.SP.800-232

Implementation note:
    Reference implementation written for this comparative study. Not
    constant-time; must not be used to protect real data.

Note on comparability:
    ASCON is an AEAD scheme, so its output is 16 bytes longer than the plaintext
    because it includes an authentication tag. AES, PRESENT and SPECK are run in
    CTR mode and produce ciphertext the same length as the plaintext. This is a
    genuine difference in what the algorithms provide, not an inconsistency in
    the experiment, and is reported as such in the results.
"""

from __future__ import annotations

from .base import Cipher

MASK64 = 0xFFFFFFFFFFFFFFFF

#: Initial value for ASCON-128: k=128, r=64, a=12, b=6.
IV_ASCON_128 = 0x80400C0600000000

RATE_BYTES = 8
ROUNDS_A = 12
ROUNDS_B = 6
TAG_BYTES = 16


def _ror(value: int, amount: int) -> int:
    return ((value >> amount) | (value << (64 - amount))) & MASK64


def permutation(state: list[int], rounds: int) -> None:
    """Apply the ASCON permutation p^rounds to the 320-bit state in place."""
    x0, x1, x2, x3, x4 = state

    for r in range(12 - rounds, 12):
        # --- Addition of round constant ---
        x2 ^= (0xF0 - r * 0x10 + r * 0x1)

        # --- Substitution layer (bitsliced 5-bit S-box) ---
        x0 ^= x4
        x4 ^= x3
        x2 ^= x1
        t0 = (~x0 & MASK64) & x1
        t1 = (~x1 & MASK64) & x2
        t2 = (~x2 & MASK64) & x3
        t3 = (~x3 & MASK64) & x4
        t4 = (~x4 & MASK64) & x0
        x0 ^= t1
        x1 ^= t2
        x2 ^= t3
        x3 ^= t4
        x4 ^= t0
        x1 ^= x0
        x0 ^= x4
        x3 ^= x2
        x2 ^= MASK64  # x2 = ~x2

        # --- Linear diffusion layer ---
        x0 ^= _ror(x0, 19) ^ _ror(x0, 28)
        x1 ^= _ror(x1, 61) ^ _ror(x1, 39)
        x2 ^= _ror(x2, 1) ^ _ror(x2, 6)
        x3 ^= _ror(x3, 10) ^ _ror(x3, 17)
        x4 ^= _ror(x4, 7) ^ _ror(x4, 41)

    state[0], state[1], state[2], state[3], state[4] = x0, x1, x2, x3, x4


def _initialise(key: bytes, nonce: bytes) -> tuple[list[int], int, int]:
    """Build the initial state and return it with the two key words."""
    k0 = int.from_bytes(key[:8], "big")
    k1 = int.from_bytes(key[8:], "big")
    n0 = int.from_bytes(nonce[:8], "big")
    n1 = int.from_bytes(nonce[8:], "big")

    state = [IV_ASCON_128, k0, k1, n0, n1]
    permutation(state, ROUNDS_A)
    state[3] ^= k0
    state[4] ^= k1

    # Domain separation between associated data and plaintext. This study uses
    # no associated data, so the separator is applied directly.
    state[4] ^= 1

    return state, k0, k1


def _finalise(state: list[int], k0: int, k1: int) -> bytes:
    state[1] ^= k0
    state[2] ^= k1
    permutation(state, ROUNDS_A)
    tag0 = state[3] ^ k0
    tag1 = state[4] ^ k1
    return tag0.to_bytes(8, "big") + tag1.to_bytes(8, "big")


def encrypt(key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
    """Encrypt and authenticate. Returns ciphertext || 16-byte tag."""
    if len(key) != 16:
        raise ValueError(f"ASCON-128 requires a 16-byte key, got {len(key)}")
    if len(nonce) != 16:
        raise ValueError(f"ASCON-128 requires a 16-byte nonce, got {len(nonce)}")

    state, k0, k1 = _initialise(key, nonce)

    # Pad the plaintext: append 0x80 then zero bytes up to a rate multiple.
    padded = plaintext + b"\x80" + b"\x00" * (
        RATE_BYTES - (len(plaintext) + 1) % RATE_BYTES if (len(plaintext) + 1) % RATE_BYTES else 0
    )

    out = bytearray()
    num_blocks = len(padded) // RATE_BYTES

    for i in range(num_blocks):
        block = int.from_bytes(padded[i * RATE_BYTES:(i + 1) * RATE_BYTES], "big")
        state[0] ^= block
        out += state[0].to_bytes(8, "big")
        if i < num_blocks - 1:
            permutation(state, ROUNDS_B)

    # The final ciphertext block is truncated to the unpadded plaintext length.
    ciphertext = bytes(out[:len(plaintext)])
    tag = _finalise(state, k0, k1)
    return ciphertext + tag


def decrypt(key: bytes, nonce: bytes, data: bytes) -> bytes:
    """Verify the tag and decrypt. Raises ValueError if authentication fails."""
    if len(data) < TAG_BYTES:
        raise ValueError("input shorter than the authentication tag")

    ciphertext = data[:-TAG_BYTES]
    received_tag = data[-TAG_BYTES:]

    state, k0, k1 = _initialise(key, nonce)

    out = bytearray()
    num_full = len(ciphertext) // RATE_BYTES

    for i in range(num_full):
        block = int.from_bytes(ciphertext[i * RATE_BYTES:(i + 1) * RATE_BYTES], "big")
        out += (state[0] ^ block).to_bytes(8, "big")
        state[0] = block
        permutation(state, ROUNDS_B)

    # Handle the final partial block, including the padding bit.
    remainder = ciphertext[num_full * RATE_BYTES:]
    tail = state[0].to_bytes(8, "big")
    plain_tail = bytes(a ^ b for a, b in zip(remainder, tail))
    out += plain_tail

    padded_tail = plain_tail + b"\x80" + b"\x00" * (RATE_BYTES - len(remainder) - 1)
    state[0] ^= int.from_bytes(padded_tail, "big")

    expected_tag = _finalise(state, k0, k1)

    # Constant-time-ish comparison. The cipher itself is not constant-time, but
    # the tag comparison should not short-circuit on the first differing byte.
    diff = 0
    for a, b in zip(expected_tag, received_tag):
        diff |= a ^ b
    if diff != 0:
        raise ValueError("ASCON authentication failed: tag mismatch")

    return bytes(out)


class Ascon128(Cipher):
    """ASCON-128 authenticated encryption with associated data."""

    name = "ASCON-128"
    key_size = 16
    nonce_size = 16
    block_size = RATE_BYTES
    category = "Lightweight"
    mode = "AEAD"

    def encrypt(self, key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
        return encrypt(key, nonce, plaintext)

    def decrypt(self, key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
        return decrypt(key, nonce, ciphertext)
