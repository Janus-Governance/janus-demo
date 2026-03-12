"""Python telemetry demo runner (scaffold)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from ingest_signals import ingest_signals
from derive_evidence import derive_evidence


def main() -> None:
    case_name = sys.argv[1] if len(sys.argv) > 1 else "case-01-happy-path"
    case_dir = (Path(__file__).resolve().parents[2] / "shared" / "datasets" / case_name)

    signals = ingest_signals(case_dir)
    _evidence = derive_evidence(signals)

    result = {
        "case": case_name,
        "demo": "python-telemetry",
        "invariants": [
            "evidence E+ / E-",
            "omission detection",
            "schema-governed interpretation",
        ],
        "status": "SKIP" if case_dir.exists() else "FAIL",
        "summary": (
            "Scaffold runner: case directory exists; logic not implemented yet."
            if case_dir.exists()
            else "Case directory not found."
        ),
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
