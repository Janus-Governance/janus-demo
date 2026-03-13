# Janus Demo

Public, portable demo cases for **Janus Core Lite**.

This repository is intentionally scoped to the **demos layer** only: deterministic datasets (fixtures) plus minimal runners that evaluate those fixtures and write stable artifacts.

## Why this repo exists

Janus needs public, portable demonstrations of its invariants that can be reviewed and replayed without access to private infrastructure.

This repo provides:

- Versioned, append-only input fixtures (NDJSON logs)
- Minimal runners that emit explicit `E+`/`E-` evidence and deterministic audit artifacts
- Cases that demonstrate how outcomes change (or remain stable) under controlled conditions

## Relationship to Janus Core Lite / janus-governance-core

- **Janus Core Lite** describes the normative concepts (evidence, omission, authority, schema interpretation).
- **janus-governance-core** is the canonical home for the core documents/spec.
- This repo complements that work with **portable demo fixtures + reference demo runners**.

## Quick Start

Prerequisites: Node.js 18+.

Run a demo case (from repo root):

- `node demos/node/src/run-demo.js case-01-happy-path`

Outputs are written to `demos/node/outputs/` (audit result + rebuild summary).

## Demo cases (case-01 … case-06)

| Case | Purpose | Primary invariant demonstrated |
| --- | --- | --- |
| `case-01-happy-path` | Required evidence is present (`E+`) and the audit is compliant | Evidence model (`E+`), schema-governed interpretation |
| `case-02-omission` | Required evidence is missing and the audit is non-compliant | Explicit negative evidence (`E-`), omission detection |
| `case-03-human-decision` | Omission remains true (`E-`), but a human authority event accepts the exception | Human authority boundary; separation of omission truth vs decision |
| `case-04-schema-drift` | Same history, different outcome under a newer schema expectation | Schema-governed interpretation; schema drift |
| `case-05-stress` | Deterministic evaluation at higher volume with stable counts and ordering | Stress determinism; stable ordering; stable summaries |
| `case-06-deterministic-rebuild` | Evaluate twice against identical parsed inputs and prove results match | Deterministic rebuildability (replay equality) |

## How to run the Node demos

From the repo root:

- `node demos/node/src/run-demo.js case-01-happy-path`
- `node demos/node/src/run-demo.js case-02-omission`
- `node demos/node/src/run-demo.js case-03-human-decision`
- `node demos/node/src/run-demo.js case-04-schema-drift`
- `node demos/node/src/run-demo.js case-05-stress`
- `node demos/node/src/run-demo.js case-06-deterministic-rebuild`

Or pass a dataset directory explicitly:

- `node demos/node/src/run-demo.js demos/shared/datasets/case-06-deterministic-rebuild`

## What these demos validate

- `E+`: explicit positive evidence is recorded when requirements are met
- `E-`: explicit negative evidence is recorded when required evidence is missing
- Omission detection is a first-class, preserved fact (not inferred implicitly)
- Human authority can accept exceptions without erasing `E-`
- Schema drift: interpretation can change when expectations change, even with the same history
- Stress determinism: stable counting and stable ordering under higher event volume
- Deterministic rebuild: replaying the same inputs produces identical normalized outputs

## Repository structure

- [demos/](demos/): entry point for all demo assets
- [demos/shared/](demos/shared/): shared fixtures, datasets, and demo contract/specs
- [demos/node/](demos/node/): minimal Node.js runner and outputs
- [demos/python-telemetry/](demos/python-telemetry/): minimal Python telemetry/evidence scaffolding
- [demos/csv-portable/](demos/csv-portable/): CSV-first portable fixtures and verifiers
- [demos/stress/](demos/stress/): stress-style reproducibility scaffolding

## Safety / portability

This repo must remain:

- Free of private IDs, credentials, tokens, or internal URLs
- Free of external platform bindings
- Reproducible on a local machine with standard toolchains
