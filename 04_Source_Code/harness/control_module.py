"""Experimental Control Module.

Implements the "Experimental Control Module" component of Figure 3.1 and the
loop structure of Figure 3.2.

Its single responsibility is to hold the experimental conditions constant. It
supplies the same plaintext bytes to every algorithm, enforces a fixed trial
count, and sequences the runs so that no algorithm receives a different
execution context from another. This is the mechanism by which the study
addresses the "lack of standardised comparison" problem in Section 1.3.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

from ciphers import ALL_CIPHERS, Cipher
from .data_logger import DataLogger
from .environment import capture
from .monitor import measure

# ---------------------------------------------------------------------------
# Experimental parameters (Table 3.1: Data Collection Parameters)
# ---------------------------------------------------------------------------

#: Test data sizes representing typical IoT payloads.
DATA_SIZES: list[tuple[str, int]] = [
    ("1KB", 1 * 1024),
    ("10KB", 10 * 1024),
    ("100KB", 100 * 1024),
    ("1MB", 1024 * 1024),
]

#: Repeated runs per algorithm per data size, to improve reliability.
TRIALS_PER_CONFIGURATION = 30

#: Unmeasured iterations before each measured set. The first execution of a code
#: path in an interpreted runtime includes one-time costs that are not
#: representative of steady-state cipher performance. Applied identically to all
#: four algorithms so it advantages none of them.
WARMUP_ITERATIONS = 3

#: Fixed seed so the generated test data is identical on every run and on every
#: machine. Reproducibility requirement, Section 3.6.3.
DATA_SEED = b"GroupT-LightweightEncryption-2026"


@dataclass
class RunConfig:
    """Parameters for one experimental run."""

    trials: int = TRIALS_PER_CONFIGURATION
    warmup: int = WARMUP_ITERATIONS
    sizes: list[tuple[str, int]] | None = None
    algorithms: list[Cipher] | None = None
    output_csv: str = "../06_Results_or_Expected_Output/results.csv"

    def resolved_sizes(self) -> list[tuple[str, int]]:
        return self.sizes if self.sizes is not None else DATA_SIZES

    def resolved_algorithms(self) -> list[Cipher]:
        return self.algorithms if self.algorithms is not None else ALL_CIPHERS


def derive_key_material(cipher: Cipher) -> tuple[bytes, bytes]:
    """Derive a fixed key and nonce for a cipher.

    The key is derived deterministically from the cipher name so it is identical
    on every run, and generated once per algorithm rather than per trial. Key
    generation cost therefore never enters the measured region.

    These are test keys for a performance experiment. They are deliberately
    reproducible and must never be used to protect real data.
    """
    digest = hashlib.sha256(DATA_SEED + cipher.name.encode()).digest()
    key = digest[:cipher.key_size]
    nonce = hashlib.sha256(digest).digest()[:cipher.nonce_size]
    return key, nonce


def generate_payload(size_bytes: int) -> bytes:
    """Generate deterministic synthetic sensor-style test data.

    The same bytes are supplied to all four algorithms at a given size, which is
    what makes the comparison valid. No confidential or personal data is used
    (Section 3.6.1).
    """
    out = bytearray()
    counter = 0
    while len(out) < size_bytes:
        out += hashlib.sha256(DATA_SEED + counter.to_bytes(8, "big")).digest()
        counter += 1
    return bytes(out[:size_bytes])


def run_experiment(config: RunConfig | None = None, verbose: bool = True) -> DataLogger:
    """Execute the full experiment following the flowchart in Figure 3.2.

    Loop order: algorithm -> data size -> trial.
    """
    config = config or RunConfig()
    logger = DataLogger(config.output_csv)

    algorithms = config.resolved_algorithms()
    sizes = config.resolved_sizes()

    # Payloads are generated once and reused, so generation cost is outside the
    # measured region and every algorithm sees byte-identical input.
    payloads = {label: generate_payload(size) for label, size in sizes}

    invalid_trials = 0

    for cipher in algorithms:                                  # Outer loop
        key, nonce = derive_key_material(cipher)

        for label, size in sizes:                              # Middle loop
            plaintext = payloads[label]

            # --- Warm-up (unmeasured) ---
            for _ in range(config.warmup):
                cipher.decrypt(key, nonce, cipher.encrypt(key, nonce, plaintext))

            for trial in range(1, config.trials + 1):          # Inner loop
                enc = measure(cipher.encrypt, size, key, nonce, plaintext)
                dec = measure(cipher.decrypt, size, key, nonce, enc.output)

                # Verification step (Section 3.4.2). A timing measurement taken
                # from an incorrect implementation would be meaningless.
                valid = dec.output == plaintext
                if not valid:
                    invalid_trials += 1

                row = {
                    "algorithm": cipher.name,
                    "category": cipher.category,
                    "mode": cipher.mode,
                    "data_size_label": label,
                    "data_size_bytes": size,
                    "trial": trial,
                    "ciphertext_bytes": enc.output_bytes,
                    "roundtrip_valid": valid,
                }
                row.update(enc.as_row("encrypt"))
                row.update(dec.as_row("decrypt"))
                logger.record(row)

            if verbose:
                print(f"  {cipher.name:<14} {label:>6}  {config.trials} trials complete")

    logger.flush()
    logger.write_metadata({
        "environment": capture(),
        "parameters": {
            "trials_per_configuration": config.trials,
            "warmup_iterations": config.warmup,
            "data_sizes": {label: size for label, size in sizes},
            "algorithms": [c.describe() for c in algorithms],
            "baseline": "AES-128",
            "total_rows": logger.row_count,
            "invalid_trials": invalid_trials,
        },
    })

    return logger
