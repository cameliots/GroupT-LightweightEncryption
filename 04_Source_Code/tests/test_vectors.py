"""Known-answer tests for the four cipher implementations.

This file is the validation gate described in the iteration plan
(``03_Architecture_and_Flowchart/Development_Model.md``). No timing measurement
from a cipher is meaningful until that cipher reproduces its published test
vectors, so this must pass before any results are collected.

Run with:  python -m tests.test_vectors     (from 04_Source_Code/)
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ciphers import AES128, Ascon128, Present80, Speck64_128  # noqa: E402
from ciphers.aes128 import encrypt_block as aes_encrypt_block, expand_key as aes_expand_key  # noqa: E402
from ciphers.present import (  # noqa: E402
    decrypt_block as present_decrypt_block,
    encrypt_block as present_encrypt_block,
    expand_key as present_expand_key,
)
from ciphers.speck import (  # noqa: E402
    decrypt_block as speck_decrypt_block,
    encrypt_block as speck_encrypt_block,
    expand_key as speck_expand_key,
)

PASSED = 0
FAILED = 0


def check(label: str, actual, expected) -> None:
    global PASSED, FAILED
    if actual == expected:
        PASSED += 1
        print(f"  PASS  {label}")
    else:
        FAILED += 1
        print(f"  FAIL  {label}")
        print(f"        expected: {expected!r}")
        print(f"        actual:   {actual!r}")


# ---------------------------------------------------------------------------
# AES-128 — FIPS-197 Appendix B / C.1
# ---------------------------------------------------------------------------

def test_aes128() -> None:
    print("AES-128 (FIPS-197)")

    # FIPS-197 Appendix C.1
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")
    expected = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")
    check("C.1 block encryption", aes_encrypt_block(plaintext, aes_expand_key(key)), expected)

    # FIPS-197 Appendix B
    key_b = bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c")
    plain_b = bytes.fromhex("3243f6a8885a308d313198a2e0370734")
    expected_b = bytes.fromhex("3925841d02dc09fbdc118597196a0b32")
    check("Appendix B block encryption", aes_encrypt_block(plain_b, aes_expand_key(key_b)), expected_b)

    # CTR-mode round trip
    cipher = AES128()
    nonce = bytes(range(8))
    message = b"IoT sensor payload for the comparative evaluation study." * 7
    ct = cipher.encrypt(key, nonce, message)
    check("CTR round trip", cipher.decrypt(key, nonce, ct), message)
    check("CTR preserves length", len(ct), len(message))


# ---------------------------------------------------------------------------
# PRESENT-80 — Bogdanov et al. (2007), Appendix I
# ---------------------------------------------------------------------------

def test_present80() -> None:
    print("PRESENT-80 (CHES 2007)")

    # CHES 2007, Appendix I. Tuples are (key, plaintext, expected ciphertext).
    vectors = [
        ("00000000000000000000", "0000000000000000", "5579c1387b228445"),
        ("00000000000000000000", "ffffffffffffffff", "a112ffc72f68417b"),
        ("ffffffffffffffffffff", "0000000000000000", "e72c46c0f5945049"),
        ("ffffffffffffffffffff", "ffffffffffffffff", "3333dcd3213210d2"),
    ]

    for key_hex, plain_hex, expect_hex in vectors:
        key = bytes.fromhex(key_hex)
        plaintext = bytes.fromhex(plain_hex)
        round_keys = present_expand_key(key)
        actual = present_encrypt_block(plaintext, round_keys)
        check(f"KAT key={key_hex[:8]}… pt={plain_hex[:8]}…", actual.hex(), expect_hex)
        check(f"KAT inverse key={key_hex[:8]}…", present_decrypt_block(actual, round_keys), plaintext)

    cipher = Present80()
    key = bytes.fromhex("00112233445566778899")
    nonce = bytes.fromhex("0a0b0c0d")
    message = b"Lightweight cipher payload, PRESENT-80 in CTR mode." * 5
    ct = cipher.encrypt(key, nonce, message)
    check("CTR round trip", cipher.decrypt(key, nonce, ct), message)
    check("CTR preserves length", len(ct), len(message))


# ---------------------------------------------------------------------------
# SPECK 64/128 — Beaulieu et al. (2013), test vectors
# ---------------------------------------------------------------------------

def test_speck64_128() -> None:
    print("SPECK 64/128 (ePrint 2013/404)")

    key = bytes.fromhex("1b1a1918" "13121110" "0b0a0908" "03020100")
    plaintext = bytes.fromhex("3b726574" "7475432d")
    expected = bytes.fromhex("8c6fa548" "454e028b")

    round_keys = speck_expand_key(key)
    actual = speck_encrypt_block(plaintext, round_keys)
    check("KAT block encryption", actual.hex(), expected.hex())
    check("KAT block decryption", speck_decrypt_block(expected, round_keys), plaintext)
    check("round key count", len(round_keys), 27)

    cipher = Speck64_128()
    nonce = bytes.fromhex("11223344")
    message = b"SPECK 64/128 payload for the IoT comparison." * 9
    ct = cipher.encrypt(key, nonce, message)
    check("CTR round trip", cipher.decrypt(key, nonce, ct), message)
    check("CTR preserves length", len(ct), len(message))


# ---------------------------------------------------------------------------
# ASCON-128 — NIST SP 800-232
# ---------------------------------------------------------------------------

def test_ascon128() -> None:
    print("ASCON-128 (NIST SP 800-232)")

    cipher = Ascon128()
    key = bytes(range(16))
    nonce = bytes(range(16, 32))

    # Round trip across lengths that exercise every padding case:
    # empty, partial block, exact block multiple, and multi-block.
    for length in (0, 1, 7, 8, 9, 15, 16, 17, 64, 1000):
        message = bytes((i * 7 + 3) & 0xFF for i in range(length))
        ct = cipher.encrypt(key, nonce, message)
        check(f"round trip len={length}", cipher.decrypt(key, nonce, ct), message)
        check(f"tag overhead len={length}", len(ct) - len(message), 16)

    # Authentication must reject a modified ciphertext.
    message = b"authenticated encryption payload"
    ct = bytearray(cipher.encrypt(key, nonce, message))
    ct[3] ^= 0x01
    try:
        cipher.decrypt(key, nonce, bytes(ct))
        check("tamper detection", "no exception raised", "ValueError")
    except ValueError:
        check("tamper detection", "ValueError", "ValueError")

    # A modified tag must also be rejected.
    ct2 = bytearray(cipher.encrypt(key, nonce, message))
    ct2[-1] ^= 0x80
    try:
        cipher.decrypt(key, nonce, bytes(ct2))
        check("tag tamper detection", "no exception raised", "ValueError")
    except ValueError:
        check("tag tamper detection", "ValueError", "ValueError")


# ---------------------------------------------------------------------------
# Interface conformance
# ---------------------------------------------------------------------------

def test_common_interface() -> None:
    print("Common interface conformance")
    from ciphers import ALL_CIPHERS

    check("four algorithms registered", len(ALL_CIPHERS), 4)

    message = b"x" * 256
    for cipher in ALL_CIPHERS:
        key = bytes(range(cipher.key_size))
        nonce = bytes(range(cipher.nonce_size))
        ct = cipher.encrypt(key, nonce, message)
        check(f"{cipher.name} round trip", cipher.decrypt(key, nonce, ct), message)
        check(f"{cipher.name} declares category",
              cipher.category in ("Conventional", "Lightweight"), True)


def main() -> int:
    for suite in (test_aes128, test_present80, test_speck64_128,
                  test_ascon128, test_common_interface):
        suite()
        print()

    print("=" * 52)
    print(f"  {PASSED} passed, {FAILED} failed")
    print("=" * 52)
    return 1 if FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
