# Case 01 — Happy Path

This is the canonical minimal happy-path case for the public Node demo.

## Inputs

- `MANAGEMENT_LOG.ndjson`
	- Contains a governance event and an explicit positive evidence record (`E+`).
- `SCHEMA_LOG.ndjson`
	- Declares the single expectation the evaluator applies.

## Scenario

- A governance event `DEPLOYMENT_COMPLETED` occurs for `deployment_id = dep-001`.
- The schema declares that such a deployment must have explicit confirmation evidence.
- The management log contains matching evidence `DEPLOYMENT_CONFIRMED` for the same `deployment_id`.

Expected outcome: compliant / validated, explicit positive evidence (`E+`), no omission detected.
