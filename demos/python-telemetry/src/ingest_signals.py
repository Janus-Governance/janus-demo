"""Ingest telemetry-like signals (scaffold).

At scaffold stage this module only defines the intended entrypoints.
"""

from __future__ import annotations

from pathlib import Path


def ingest_signals(case_dir: Path) -> list[dict]:
    """Load portable signals for a case.

    This is a placeholder; implementations should remain file-based and portable.
    """

    _ = case_dir
    return []
