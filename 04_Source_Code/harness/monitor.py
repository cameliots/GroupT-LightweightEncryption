"""Performance Monitoring Unit.

Implements the "Performance Monitoring Unit" component of Figure 3.1. Records
timing, memory and throughput information for a single cipher operation.

Measurement decisions, and why they matter for comparability:

* ``time.perf_counter_ns`` is used because it is monotonic and has the highest
  resolution available on the platform. The same timer is used for all four
  algorithms.
* The timer brackets *only* the cipher call. Data generation, validation and
  logging happen outside the timed region so they do not contaminate the
  measurement.
* ``tracemalloc`` measures peak memory allocated by the Python interpreter
  during the operation. It is started and stopped around each operation so the
  peak reflects that operation alone.
* Throughput is derived from the payload size and the measured time rather than
  measured separately, so it is always consistent with the recorded time.
"""

from __future__ import annotations

import time
import tracemalloc
from dataclasses import dataclass


@dataclass
class Measurement:
    """One measured cipher operation."""

    elapsed_ms: float
    peak_memory_kb: float
    throughput_mbps: float
    output_bytes: int
    output: bytes

    def as_row(self, prefix: str) -> dict:
        """Flatten into CSV columns with the given prefix ("encrypt"/"decrypt")."""
        return {
            f"{prefix}_time_ms": round(self.elapsed_ms, 6),
            f"{prefix}_peak_memory_kb": round(self.peak_memory_kb, 3),
            f"{prefix}_throughput_mbps": round(self.throughput_mbps, 4),
        }


def measure(operation, payload_size: int, *args) -> Measurement:
    """Run ``operation(*args)`` once, measuring time and peak memory.

    Args:
        operation: The cipher call to measure.
        payload_size: Size in bytes of the data being processed, used for the
            throughput calculation.
        *args: Arguments forwarded to ``operation``.

    Returns:
        A :class:`Measurement` holding the metrics and the operation's output.
    """
    tracemalloc.start()
    baseline_current, _ = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()

    start = time.perf_counter_ns()
    result = operation(*args)
    end = time.perf_counter_ns()

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_ns = end - start
    elapsed_ms = elapsed_ns / 1_000_000
    elapsed_s = elapsed_ns / 1_000_000_000

    # Guard against a zero-duration measurement on a very fast, very small run.
    throughput_mbps = (payload_size * 8) / elapsed_s / 1_000_000 if elapsed_s > 0 else 0.0
    peak_kb = max(peak - baseline_current, 0) / 1024

    return Measurement(
        elapsed_ms=elapsed_ms,
        peak_memory_kb=peak_kb,
        throughput_mbps=throughput_mbps,
        output_bytes=len(result),
        output=result,
    )


def timer_resolution_ns() -> int:
    """Report the platform timer resolution, recorded in the results metadata."""
    return time.get_clock_info("perf_counter").resolution * 1_000_000_000
