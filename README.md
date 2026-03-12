# janus-demo

Public, portable demonstrations for **Janus Core Lite**.

This repository is intentionally scoped to the **demos layer** only:

- **Core** (normative kernel) lives elsewhere.
- **Runtimes** (implementations) live elsewhere.
- This repo provides **reproducible, portable demo fixtures + minimal runners** that illustrate the Janus invariants.

## What these demos demonstrate

Across the demo set, we focus on the Janus Core Lite invariants:

- Append-only logs
- Audit writer authority boundary
- Deterministic rebuildability (replay)
- Evidence model: `E+` and `E-`
- Omission detection
- Schema-governed interpretation
- Separation between runtime behavior and public demo fixtures

## Repository layout

All demos live under [demos/](demos/):

- [demos/shared/](demos/shared/): shared fixtures, datasets, and demo contract
- [demos/node/](demos/node/): minimal Node.js runner scaffold
- [demos/python-telemetry/](demos/python-telemetry/): minimal Python telemetry/evidence scaffold
- [demos/csv-portable/](demos/csv-portable/): CSV-first portable fixtures and verifiers
- [demos/stress/](demos/stress/): stress-style reproducibility scaffolding

## Status

This is a **scaffold + documentation pass**. The code is intentionally minimal and does not implement full business logic yet.

## Safety / portability

This repo must remain:

- Free of private IDs, credentials, tokens, or internal URLs
- Free of external platform bindings (e.g., Apps Script)
- Reproducible on a local machine with standard toolchains
