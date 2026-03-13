# Demos

This folder contains the public, reproducible demonstrations for Janus Core Lite.

For a case-by-case overview (case-01 … case-06), see the root README.

## How to use this repo

- Read the shared contract first: [shared/specs/demo-contract.md](shared/specs/demo-contract.md)
- Use the shared datasets under [shared/datasets/](shared/datasets/)
- Run a demo runner (Node / Python / CSV verifier / Stress scaffolding)

## Run the Node runner

From the repo root:

- `node demos/node/src/run-demo.js case-01-happy-path`
- `node demos/node/src/run-demo.js case-02-omission`
- `node demos/node/src/run-demo.js case-03-human-decision`
- `node demos/node/src/run-demo.js case-04-schema-drift`
- `node demos/node/src/run-demo.js case-05-stress`
- `node demos/node/src/run-demo.js case-06-deterministic-rebuild`

## What is considered “portable” here

Portable means:

- No cloud services required
- No organization-specific infrastructure
- No private identifiers or credentials
- Inputs and outputs are files committed in the repo (fixtures + results schema)

## Datasets

Datasets are structured as cases (happy path, omission, human decision, schema drift, stress) and are designed to be:

- Append-only (as files)
- Deterministically replayable
- Easy to validate against the shared result schema
