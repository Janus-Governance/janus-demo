# Demo Contract (Janus Core Lite)

This document defines the minimal contract that all demos in this repository follow.

## Goals

- Keep demos portable and reproducible
- Standardize how fixtures are represented
- Standardize how demo results are reported

## Inputs

A demo consumes one **case directory** under [../datasets/](../datasets/).

A case directory may include:

- Append-only event logs (file-based)
- Optional schema declarations used to interpret logs
- Optional telemetry signals (for derived evidence)

At scaffold stage, fixtures are represented primarily as documentation placeholders.

## Outputs

A demo produces a single results object matching [result-schema.json](result-schema.json).

Recommended output location per demo:

- `demos/<demo>/outputs/` (ignored by design except `.gitkeep`)

## Semantics

Demos should validate the following concepts (as applicable):

- Append-only log handling
- Evidence generation (`E+` / `E-`)
- Omission detection (negative evidence)
- Audit writer authority boundary (only one component writes the audit log)
- Deterministic rebuild (replay yields the same reconstructed state)
- Schema-governed interpretation (schemas constrain meaning)

## Non-goals

- No external platform bindings
- No private infrastructure references
- No credentials, tokens, or account-specific identifiers
