# Python Telemetry Demo (Scaffold)

This demo is a minimal Python scaffold for demonstrating how telemetry-like signals could be ingested and turned into evidence.

## What it demonstrates

Intended (once implemented):

- Ingesting signals (portable files) without external services
- Deriving evidence objects (`E+` / `E-`) from signals and expected rules
- Producing a minimal demo result JSON

## Invariants referenced

- Evidence `E+` / `E-`
- Omission detection
- Schema-governed interpretation
- Deterministic rebuildability (where applicable)

## Run (scaffold)

- Create a virtual environment
- Install requirements
- Run `python src/run_demo.py case-01-happy-path`

At scaffold stage, it prints a placeholder result.
