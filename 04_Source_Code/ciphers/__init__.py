"""Encryption Algorithm Module.

Holds the four ciphers under evaluation behind the common interface defined in
``base.Cipher``. This corresponds to the "Encryption Algorithm Module" and
"Decryption Algorithm Module" components of Figure 3.1.
"""

from .base import Cipher
from .aes128 import AES128
from .present import Present80
from .speck import Speck64_128
from .ascon import Ascon128

#: The four algorithms confirmed in Phase 1, in the order they are evaluated.
#: AES-128 is first because it is the baseline all others are compared against.
ALL_CIPHERS = [
    AES128(),
    Present80(),
    Speck64_128(),
    Ascon128(),
]

BASELINE = "AES-128"

CIPHERS_BY_NAME = {c.name: c for c in ALL_CIPHERS}

__all__ = [
    "Cipher",
    "AES128",
    "Present80",
    "Speck64_128",
    "Ascon128",
    "ALL_CIPHERS",
    "CIPHERS_BY_NAME",
    "BASELINE",
]
