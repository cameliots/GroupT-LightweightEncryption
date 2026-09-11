#!/usr/bin/env python3
"""Generate the synthetic IoT test data used as encryption input.

Implements the "Sample IoT Test Data" component of Figure 3.1 and the test data
parameters of Table 3.1.

Two design decisions matter here:

1. **Synthetic data only.** No confidential, personal or organisational data is
   collected, stored or processed at any stage (Section 3.6.1). The payloads are
   generated sensor-style readings.

2. **Deterministic generation.** The data is derived from a fixed seed rather
   than a random source, so the identical bytes are produced on every run and on
   every machine. This supports the reproducibility requirement in Section 3.6.3
   and guarantees that all four algorithms are compared on identical input.

Usage:
    python generate_test_data.py              # write all four sizes to generated/
    python generate_test_data.py --preview    # show a sample record only
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

#: Same seed used by harness/control_module.py, so the generated files match the
#: bytes the experiment feeds to the ciphers.
DATA_SEED = b"GroupT-LightweightEncryption-2026"

SIZES = [
    ("1KB", 1 * 1024),
    ("10KB", 10 * 1024),
    ("100KB", 100 * 1024),
    ("1MB", 1024 * 1024),
]

OUTPUT_DIR = Path(__file__).parent / "generated"

SENSOR_TYPES = ["temperature", "humidity", "pressure", "motion", "light", "co2"]


def raw_payload(size_bytes: int) -> bytes:
    """Generate ``size_bytes`` of deterministic pseudo-random bytes.

    This is what the experiment actually encrypts. Using a hash chain gives data
    with no exploitable structure, so no algorithm is advantaged by input
    patterns, while remaining perfectly reproducible.
    """
    out = bytearray()
    counter = 0
    while len(out) < size_bytes:
        out += hashlib.sha256(DATA_SEED + counter.to_bytes(8, "big")).digest()
        counter += 1
    return bytes(out[:size_bytes])


def sensor_records(count: int) -> list[dict]:
    """Generate readable sensor-style records.

    Provided so the test data is inspectable and clearly recognisable as
    synthetic IoT telemetry. The experiment encrypts the raw byte payloads above;
    these records document what the payloads represent.
    """
    records = []
    for i in range(count):
        digest = hashlib.sha256(DATA_SEED + b"record" + i.to_bytes(4, "big")).digest()
        sensor = SENSOR_TYPES[digest[0] % len(SENSOR_TYPES)]
        records.append({
            "device_id": f"iot-node-{digest[1] % 64:03d}",
            "sensor": sensor,
            "value": round(digest[2] + digest[3] / 256, 2),
            "unit": {"temperature": "C", "humidity": "%", "pressure": "hPa",
                     "motion": "bool", "light": "lux", "co2": "ppm"}[sensor],
            "sequence": i,
            "timestamp_offset_s": i * 5,
        })
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--preview", action="store_true", help="Print a sample record and exit")
    args = parser.parse_args()

    if args.preview:
        print(json.dumps(sensor_records(5), indent=2))
        return 0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Generating synthetic IoT test data (Table 3.1)")
    print()
    for label, size in SIZES:
        data = raw_payload(size)
        path = OUTPUT_DIR / f"test_data_{label}.bin"
        path.write_bytes(data)
        checksum = hashlib.sha256(data).hexdigest()
        print(f"  {label:>6}  {size:>9,} bytes  sha256={checksum[:16]}…  -> {path.name}")

    sample_path = Path(__file__).parent / "sample_sensor_records.json"
    sample_path.write_text(json.dumps(sensor_records(20), indent=2), encoding="utf-8")
    print()
    print(f"  Readable sample written -> {sample_path.name}")
    print()
    print("Note: generated/ is git-ignored. The files are reproducible from this")
    print("script, so they do not need to be committed to the repository.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
