# Janus Core Lite Invariants (Demo View)

These are the invariants that the demos in this repository reference and aim to validate.

## Append-only logs

Events are recorded as an append-only sequence. Demos must never rewrite historical records.

## Audit writer authority boundary

Only a designated audit-writer component is allowed to write audit records.

## Deterministic rebuildability

A governance-relevant state representation can be reconstructed by replaying logs.

## Evidence model: E+ and E-

- `E+` (positive evidence): an expected record exists.
- `E-` (negative evidence): an expected record is verifiably absent.

## Omission detection

When an expected record is absent, the demo should represent that omission as a first-class governance signal.

## Schema-governed interpretation

Schemas constrain how events and records are interpreted. Schema drift should be detectable.

## Fixture/runtime separation

Public demo fixtures are stable, committed inputs. Runtime behaviors are implemented by demo runners.
