# case-06-deterministic-rebuild

## Goal

Prove deterministic rebuildability: re-evaluating the exact same input artifacts produces the exact same governance result.

## Dataset

This dataset contains 4 deployments:

- `dep-0601`, `dep-0602`, `dep-0603` are compliant (have `DEPLOYMENT_CONFIRMED`).
- `dep-0604` is intentionally missing confirmation evidence.

## Expected outcome

- The audit is non-compliant (`NON_COMPLIANT`) because at least one deployment is missing required evidence.
- The demo runner replays the evaluation twice against the same parsed inputs and records two digests.
- The rebuild summary should report:
  - `first_run_digest == second_run_digest`
  - `outputs_identical == true`
  - `replay_count == 2`
  - `deterministic_rebuild == true`
