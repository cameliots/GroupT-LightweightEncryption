"""Common cipher interface for the comparative evaluation.

Every algorithm in this study implements this same interface so that the
Experimental Control Module can invoke all four ciphers through identical calls.

This is a deliberate methodological decision. Section 2.4.2 identifies that prior
studies are difficult to compare because different algorithms were measured under
different conditions. Forcing every cipher through one interface removes the
framework itself as a source of difference between the measurements.
"""

from __future__ import annotations

import abc


class Cipher(abc.ABC):
    """Abstract base class for all ciphers under evaluation."""

    #: Human-readable algorithm name used in the results CSV.
    name: str = "UNDEFINED"

    #: Key length in bytes.
    key_size: int = 0

    #: Nonce / IV length in bytes.
    nonce_size: int = 0

    #: Block size in bytes (rate, for sponge constructions).
    block_size: int = 0

    #: "Conventional" for the AES baseline, "Lightweight" otherwise.
    category: str = "Lightweight"

    #: Short note describing the mode of operation, reported with the results.
    mode: str = ""

    @abc.abstractmethod
    def encrypt(self, key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
        """Encrypt ``plaintext`` and return the ciphertext."""

    @abc.abstractmethod
    def decrypt(self, key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
        """Decrypt ``ciphertext`` and return the recovered plaintext."""

    def describe(self) -> dict:
        """Return the cipher's declared parameters for the results metadata."""
        return {
            "name": self.name,
            "category": self.category,
            "mode": self.mode,
            "key_bits": self.key_size * 8,
            "nonce_bits": self.nonce_size * 8,
            "block_bits": self.block_size * 8,
        }

    def __repr__(self) -> str:  # pragma: no cover - debugging helper
        return f"<{self.__class__.__name__} {self.name}>"


def ctr_keystream_xor(
    block_encrypt,
    block_size: int,
    nonce: bytes,
    data: bytes,
) -> bytes:
    """Apply CTR mode to ``data`` using ``block_encrypt``.

    CTR mode turns a block cipher into a stream cipher. The counter block is the
    nonce (left half) concatenated with a big-endian counter (right half). Each
    counter block is encrypted and XORed with the corresponding plaintext block.

    CTR is used for AES, PRESENT and SPECK so that all three block ciphers
    process arbitrary-length payloads under the same construction. Because CTR is
    symmetric, the same function performs both encryption and decryption.

    Args:
        block_encrypt: Callable taking one ``block_size``-byte block and
            returning the encrypted block.
        block_size: Cipher block size in bytes.
        nonce: Nonce of exactly ``block_size // 2`` bytes.
        data: Plaintext or ciphertext of any length.

    Returns:
        The XORed output, the same length as ``data``.
    """
    half = block_size // 2
    if len(nonce) != half:
        raise ValueError(
            f"nonce must be {half} bytes for a {block_size}-byte block, got {len(nonce)}"
        )

    out = bytearray(len(data))
    counter = 0
    position = 0
    data_len = len(data)

    while position < data_len:
        counter_block = nonce + counter.to_bytes(half, "big")
        keystream = block_encrypt(counter_block)

        chunk_end = min(position + block_size, data_len)
        for i in range(position, chunk_end):
            out[i] = data[i] ^ keystream[i - position]

        position = chunk_end
        counter += 1

    return bytes(out)
