"""Experimental environment recorder.

Captures the platform on which the experiment was executed. This exists because
Section 2.4.2 identifies differences in undocumented hardware and software
environments as a primary reason that results from prior studies cannot be
compared directly. Recording the environment with the results is what allows a
later reviewer to say whether two sets of measurements are comparable.
"""

from __future__ import annotations

import platform
import sys
from datetime import datetime, timezone

from .monitor import timer_resolution_ns


def capture() -> dict:
    """Return a dictionary describing the current execution environment."""
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "platform": platform.platform(),
        "system": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor() or "unavailable",
        "python_version": sys.version.split()[0],
        "python_implementation": platform.python_implementation(),
        "timer_resolution_ns": timer_resolution_ns(),
    }


def format_report(env: dict) -> str:
    """Render the environment as a Markdown table for the results report."""
    lines = ["| Property | Value |", "|---|---|"]
    for key, value in env.items():
        label = key.replace("_", " ").title()
        lines.append(f"| {label} | {value} |")
    return "\n".join(lines)
