"""CSV portable verifier (scaffold)."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    case_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("cases/case-01-happy-path")
    exists = case_path.exists()

    result = {
        "case": str(case_path),
        "demo": "csv-portable",
        "invariants": [
            "append-only logs",
            "deterministic rebuild",
            "omission detection",
        ],
        "status": "SKIP" if exists else "FAIL",
        "summary": (
            "Scaffold verifier: case path exists; CSV verification not implemented yet."
            if exists
            else "Case path not found."
        ),
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
