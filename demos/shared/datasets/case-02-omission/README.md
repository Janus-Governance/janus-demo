# Case 02 — Omission

This case is the canonical omission-detection example for the public Node demo.

## Inputs

- `MANAGEMENT_LOG.ndjson`
	- Contains a single governance event (`DEPLOYMENT_COMPLETED`).
	- Intentionally does **not** contain the required confirmation evidence.
- `SCHEMA_LOG.ndjson`
	- Declares the expectation: every `DEPLOYMENT_COMPLETED` must have matching `DEPLOYMENT_CONFIRMED` evidence with the same `deployment_id`.

## Expected outcome

- Explicit negative evidence (`E-`) is emitted for the missing confirmation.
- `omission_detected: true`
- Audit decision is non-compliant.
