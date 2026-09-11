"""Data Logger.

Implements the "Data Logger" component of Figure 3.1. Writes one CSV row per
trial to a results store.

Raw per-trial rows are stored rather than pre-aggregated averages. This supports
the transparency and reproducibility requirement in Section 3.6.3: anyone
reviewing the study can recompute the summary statistics from the raw data, or
apply a different analysis, without re-running the experiment.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

COLUMNS = [
    "algorithm",
    "category",
    "mode",
    "data_size_label",
    "data_size_bytes",
    "trial",
    "encrypt_time_ms",
    "decrypt_time_ms",
    "encrypt_peak_memory_kb",
    "decrypt_peak_memory_kb",
    "encrypt_throughput_mbps",
    "decrypt_throughput_mbps",
    "ciphertext_bytes",
    "roundtrip_valid",
]


class DataLogger:
    """Append-only CSV writer for trial records."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._rows: list[dict] = []

    def record(self, row: dict) -> None:
        """Store one trial record."""
        missing = [c for c in COLUMNS if c not in row]
        if missing:
            raise KeyError(f"trial record is missing columns: {missing}")
        self._rows.append(row)

    def flush(self) -> Path:
        """Write all recorded rows to the CSV file."""
        with self.path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=COLUMNS)
            writer.writeheader()
            for row in self._rows:
                writer.writerow({k: row[k] for k in COLUMNS})
        return self.path

    def write_metadata(self, metadata: dict) -> Path:
        """Write the run metadata alongside the CSV.

        Section 2.4.2 identifies undocumented experimental environments as a
        cause of non-comparable results in prior work. Recording the environment
        next to the measurements lets a reviewer state whether their conditions
        matched.
        """
        meta_path = self.path.with_suffix(".metadata.json")
        meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        return meta_path

    @property
    def row_count(self) -> int:
        return len(self._rows)
