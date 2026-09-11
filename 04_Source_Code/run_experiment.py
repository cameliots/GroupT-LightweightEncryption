#!/usr/bin/env python3
"""Main entry point for the comparative evaluation experiment.

Executes the process shown in Figure 3.2: for each algorithm, for each test data
size, repeat encryption and decryption for the configured number of trials while
recording performance metrics. Results are written to a CSV and analysed into a
Markdown report.

Usage:
    python run_experiment.py                 # full run (30 trials, up to 1 MB)
    python run_experiment.py --quick         # short run for verification
    python run_experiment.py --trials 10     # custom trial count
    python run_experiment.py --max-size 100KB
    python run_experiment.py --analyse-only  # re-analyse an existing CSV

Note:
    The full run performs 480 encrypt/decrypt pairs on payloads up to 1 MB using
    pure-Python cipher implementations. This is intentionally not fast — the
    point is a fair comparison under identical conditions, not absolute speed.
    Use --quick while verifying the setup.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from ciphers import ALL_CIPHERS  # noqa: E402
from harness import RunConfig, run_experiment  # noqa: E402
from harness.analysis import write_report  # noqa: E402
from harness.control_module import DATA_SIZES  # noqa: E402
from harness.environment import capture, format_report  # noqa: E402

DEFAULT_CSV = Path(__file__).parent.parent / "06_Results_or_Expected_Output" / "results.csv"
DEFAULT_REPORT = Path(__file__).parent.parent / "06_Results_or_Expected_Output" / "Analysis_Report.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=None,
                        help="Trials per algorithm per data size (default: 30)")
    parser.add_argument("--max-size", choices=[label for label, _ in DATA_SIZES], default=None,
                        help="Largest data size to test (default: 1MB)")
    parser.add_argument("--quick", action="store_true",
                        help="Short verification run: 3 trials, up to 10KB")
    parser.add_argument("--analyse-only", action="store_true",
                        help="Skip the experiment and re-analyse the existing CSV")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="Results CSV path")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT, help="Analysis report path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("=" * 64)
    print("  A Comparative Evaluation of Lightweight Encryption Algorithms")
    print("  for Resource-Constrained IoT Devices")
    print("=" * 64)
    print()

    if not args.analyse_only:
        trials = args.trials if args.trials else (3 if args.quick else 30)

        max_label = args.max_size or ("10KB" if args.quick else "1MB")
        cutoff = [label for label, _ in DATA_SIZES].index(max_label)
        sizes = DATA_SIZES[:cutoff + 1]

        print("Experimental environment:")
        print(format_report(capture()))
        print()
        print(f"Algorithms : {', '.join(c.name for c in ALL_CIPHERS)}")
        print(f"Data sizes : {', '.join(label for label, _ in sizes)}")
        print(f"Trials     : {trials} per algorithm per data size")
        print(f"Total runs : {len(ALL_CIPHERS) * len(sizes) * trials} encrypt/decrypt pairs")
        print()
        print("Running experiment...")

        config = RunConfig(trials=trials, sizes=sizes, output_csv=str(args.csv))
        logger = run_experiment(config)

        print()
        print(f"Recorded {logger.row_count} trial rows -> {args.csv}")

    if not Path(args.csv).exists():
        print(f"No results CSV at {args.csv}. Run without --analyse-only first.", file=sys.stderr)
        return 1

    report_path = write_report(args.csv, args.report)
    print(f"Analysis report written -> {report_path}")
    print()
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
