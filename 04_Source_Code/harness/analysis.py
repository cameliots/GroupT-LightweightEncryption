"""Analysis and Comparison Module.

Implements the "Analysis and Comparison Module" component of Figure 3.1 and the
evaluation plan in Section 3.7. Reads the raw results CSV, computes mean and
standard deviation per algorithm per data size, and expresses each lightweight
algorithm as a ratio relative to the AES-128 baseline.

Uses only the Python standard library, so the analysis runs anywhere the
experiment runs.
"""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path

METRICS = [
    ("encrypt_time_ms", "Encryption Time (ms)", "lower"),
    ("decrypt_time_ms", "Decryption Time (ms)", "lower"),
    ("encrypt_peak_memory_kb", "Encrypt Peak Memory (KB)", "lower"),
    ("decrypt_peak_memory_kb", "Decrypt Peak Memory (KB)", "lower"),
    ("encrypt_throughput_mbps", "Encrypt Throughput (Mbps)", "higher"),
    ("decrypt_throughput_mbps", "Decrypt Throughput (Mbps)", "higher"),
]

BASELINE = "AES-128"

SIZE_ORDER = ["1KB", "10KB", "100KB", "1MB"]


def load_rows(csv_path: str | Path) -> list[dict]:
    """Read the results CSV, converting numeric columns."""
    rows = []
    with Path(csv_path).open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            for key, _label, _dir in METRICS:
                row[key] = float(row[key])
            row["data_size_bytes"] = int(row["data_size_bytes"])
            row["trial"] = int(row["trial"])
            row["roundtrip_valid"] = str(row["roundtrip_valid"]).lower() == "true"
            rows.append(row)
    return rows


def summarise(rows: list[dict]) -> dict:
    """Compute mean and standard deviation per (algorithm, data size, metric)."""
    grouped = defaultdict(list)
    for row in rows:
        if not row["roundtrip_valid"]:
            continue  # Exclude invalid trials from the analysis.
        grouped[(row["algorithm"], row["data_size_label"])].append(row)

    summary = {}
    for (algorithm, size), group in grouped.items():
        entry = {"trials": len(group), "category": group[0]["category"], "mode": group[0]["mode"]}
        for key, _label, _dir in METRICS:
            values = [r[key] for r in group]
            entry[key] = {
                "mean": statistics.fmean(values),
                "stdev": statistics.stdev(values) if len(values) > 1 else 0.0,
                "min": min(values),
                "max": max(values),
            }
        summary[(algorithm, size)] = entry
    return summary


def _sorted_sizes(summary: dict) -> list[str]:
    present = {size for _alg, size in summary}
    return [s for s in SIZE_ORDER if s in present] + sorted(present - set(SIZE_ORDER))


def _sorted_algorithms(summary: dict) -> list[str]:
    present = {alg for alg, _size in summary}
    rest = sorted(present - {BASELINE})
    return ([BASELINE] if BASELINE in present else []) + rest


def metric_table(summary: dict, metric_key: str, label: str) -> str:
    """Render one metric as a Markdown table: algorithms x data sizes."""
    sizes = _sorted_sizes(summary)
    algorithms = _sorted_algorithms(summary)

    lines = [f"### {label}", ""]
    lines.append("| Algorithm | " + " | ".join(sizes) + " |")
    lines.append("|---" * (len(sizes) + 1) + "|")

    for algorithm in algorithms:
        cells = []
        for size in sizes:
            entry = summary.get((algorithm, size))
            if entry is None:
                cells.append("—")
            else:
                stats = entry[metric_key]
                cells.append(f"{stats['mean']:.4f} ± {stats['stdev']:.4f}")
        lines.append(f"| {algorithm} | " + " | ".join(cells) + " |")

    lines.append("")
    lines.append("_Values are mean ± standard deviation across all valid trials._")
    lines.append("")
    return "\n".join(lines)


def baseline_comparison(summary: dict, metric_key: str, label: str, direction: str) -> str:
    """Express each algorithm relative to the AES-128 baseline."""
    sizes = _sorted_sizes(summary)
    algorithms = _sorted_algorithms(summary)

    lines = [f"### {label} — relative to {BASELINE}", ""]
    lines.append("| Algorithm | " + " | ".join(sizes) + " |")
    lines.append("|---" * (len(sizes) + 1) + "|")

    for algorithm in algorithms:
        cells = []
        for size in sizes:
            entry = summary.get((algorithm, size))
            base = summary.get((BASELINE, size))
            if entry is None or base is None or base[metric_key]["mean"] == 0:
                cells.append("—")
            elif algorithm == BASELINE:
                cells.append("1.00× (baseline)")
            else:
                ratio = entry[metric_key]["mean"] / base[metric_key]["mean"]
                better = (ratio < 1) if direction == "lower" else (ratio > 1)
                marker = " ✅" if better else ""
                cells.append(f"{ratio:.2f}×{marker}")
        lines.append(f"| {algorithm} | " + " | ".join(cells) + " |")

    lines.append("")
    hint = "below 1.00× is better" if direction == "lower" else "above 1.00× is better"
    lines.append(f"_Ratio of each algorithm to the {BASELINE} baseline; {hint}._")
    lines.append("")
    return "\n".join(lines)


def build_report(csv_path: str | Path, title: str = "Experimental Results") -> str:
    """Produce the full Markdown analysis report."""
    rows = load_rows(csv_path)
    summary = summarise(rows)

    invalid = sum(1 for r in rows if not r["roundtrip_valid"])

    parts = [
        f"# {title}",
        "",
        f"Total trials recorded: **{len(rows)}**  ",
        f"Invalid trials excluded: **{invalid}**  ",
        f"Algorithms evaluated: **{len(_sorted_algorithms(summary))}**  ",
        f"Data sizes: **{', '.join(_sorted_sizes(summary))}**",
        "",
        "---",
        "",
        "## 1. Measured Metrics",
        "",
    ]

    for key, label, _direction in METRICS:
        parts.append(metric_table(summary, key, label))

    parts += ["---", "", "## 2. Comparison Against the Baseline", ""]
    for key, label, direction in METRICS:
        parts.append(baseline_comparison(summary, key, label, direction))

    parts += ["---", "", "## 3. Ciphertext Expansion", "", _expansion_table(rows)]

    return "\n".join(parts)


def _expansion_table(rows: list[dict]) -> str:
    """Report ciphertext length against plaintext length.

    ASCON produces 16 additional bytes because it is an AEAD scheme and includes
    an authentication tag. Reporting this makes the difference explicit rather
    than leaving it as an unexplained anomaly in the throughput figures.
    """
    seen = {}
    for row in rows:
        key = (row["algorithm"], row["data_size_label"])
        if key not in seen:
            seen[key] = (int(row["ciphertext_bytes"]), row["data_size_bytes"])

    lines = ["| Algorithm | Data Size | Plaintext (B) | Ciphertext (B) | Overhead (B) |", "|---|---|---|---|---|"]
    for (algorithm, size), (ct, pt) in sorted(seen.items()):
        lines.append(f"| {algorithm} | {size} | {pt} | {ct} | {ct - pt} |")
    lines.append("")
    lines.append(
        "_ASCON-128 adds a 16-byte authentication tag because it provides integrity "
        "as well as confidentiality. The CTR-mode block ciphers add no overhead._"
    )
    return "\n".join(lines)


def write_report(csv_path: str | Path, output_path: str | Path, title: str = "Experimental Results") -> Path:
    """Build the report and write it to disk."""
    report = build_report(csv_path, title)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    return out
