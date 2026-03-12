# Node Demo Runner

This demo provides a small, fully-local Node.js runner for Janus demo cases.

It intentionally implements only one canonical case (`case-01-happy-path`) to keep the public demo portable and easy to audit.

## What `case-01-happy-path` demonstrates

- Reads append-only input artifacts (NDJSON logs)
- Uses a schema log to declare what evidence is required
- Finds explicit positive evidence (`E+`) in the management log
- Produces an audit result (COMPLIANT) with no omission detected
- Writes deterministic output artifacts (fixed `evaluated_at`)

## What `case-02-omission` demonstrates

This case uses the same schema rule as case-01, but the required confirmation evidence is absent.

- Reads append-only input artifacts (NDJSON logs)
- Uses the schema log to declare what evidence is required
- Emits explicit negative evidence (`E-`) for the missing confirmation
- Marks omission detected and produces a non-compliant audit decision
- Writes deterministic output artifacts (fixed `evaluated_at`)

## Invariants referenced

- Append-only input artifacts
- Schema-governed interpretation
- Explicit positive evidence (`E+`)
- No omission detected (happy path)
- Deterministic rebuildability
- Separation between input evidence and audit output

## Inputs

- Case directory under `../shared/datasets/`

For `case-01-happy-path` the runner reads:

- `MANAGEMENT_LOG.ndjson`
- `SCHEMA_LOG.ndjson`

For `case-02-omission` the runner reads the same filenames:

- `MANAGEMENT_LOG.ndjson`
- `SCHEMA_LOG.ndjson`

## Outputs

- Prints a minimal result object to stdout (schema: `../shared/specs/result-schema.json`)
- Writes artifacts under `./outputs/`:
	- `audit-result.case-01-happy-path.json`
	- `rebuild-summary.case-01-happy-path.json`
	- `audit-result.case-02-omission.json`
	- `rebuild-summary.case-02-omission.json`

## Run

From the repo root:

- `node demos/node/src/run-demo.js demos/shared/datasets/case-01-happy-path`

Or (case-name form):

- `node demos/node/src/run-demo.js case-01-happy-path`

The output artifacts are written to `demos/node/outputs/`.
