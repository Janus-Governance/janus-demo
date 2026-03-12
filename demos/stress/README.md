# Stress Demo (Scaffold)

This demo is a stress / reproducibility harness scaffold.

## What it demonstrates

Intended (once implemented):

- Generating a large append-only event stream deterministically
- Rebuilding state from the stream and checking invariants
- Producing a portable result summary

## Layout

- `fixtures/`: deterministic seeds / small baseline fixtures
- `src/`: load generator + rebuild verifier
- `outputs/`: generated artifacts (kept out of git except `.gitkeep`)

## Run (scaffold)

- `node src/generate-load.js`
- `node src/verify-rebuild.js`

At scaffold stage, each script prints a placeholder result.
