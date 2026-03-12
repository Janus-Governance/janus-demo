# CSV Portable Demo (Scaffold)

This demo is a CSV-first scaffold: the primary artifacts are portable CSV files that can be verified without any runtime service.

## What it demonstrates

Intended (once implemented):

- Append-only log rows as CSV
- Deterministic verification / rebuild from CSV inputs
- A simple verifier that emits a minimal demo result JSON

## Layout

- `cases/`: per-case CSV fixtures
- `src/`: verifier scripts
- `outputs/`: generated results (ignored by git except `.gitkeep`)

## Run (scaffold)

- `python src/verify.py cases/case-01-happy-path`

At scaffold stage, it prints a placeholder result.
