# Reproducibility

## Determinism
- Each trial defines an explicit seed.
- Runner sets deterministic random seed before trial execution.

## Config snapshots
- Each trial result stores a snapshot of TrialConfig in metadata.

## Artifacts
- Raw JSONL and aggregate CSV are both exported for every run.
