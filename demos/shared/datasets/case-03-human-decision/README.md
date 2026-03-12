# Case 03 — Human Decision

This case demonstrates human authority in Janus Core Lite without erasing factual omission.

## Inputs

- `MANAGEMENT_LOG.ndjson`
	- Contains a `DEPLOYMENT_COMPLETED` governance event.
	- Intentionally omits the required confirmation evidence.
	- Contains a human authority governance exception event linked to the same deployment.
- `SCHEMA_LOG.ndjson`
	- Declares the expectation: every `DEPLOYMENT_COMPLETED` must have matching `DEPLOYMENT_CONFIRMED` evidence with the same `deployment_id`.

## Expected outcome

- Explicit negative evidence (`E-`) is emitted for the missing confirmation.
- `omission_detected: true` remains part of the audit truth.
- A human decision is detected and linked to the omission.
- Audit decision is an explicitly human-approved exception (not ordinary compliance).
