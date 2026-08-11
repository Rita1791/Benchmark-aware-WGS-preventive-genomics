# Tests

This directory contains lightweight tests for validating the structure and configuration of the benchmark-aware WGS analysis repository.

The tests are intentionally designed to run without requiring the large sequencing, alignment, reference, or benchmark files used during the full analysis.

## Test scope

The test suite checks:

- required repository directories,
- required documentation files,
- benchmark configuration,
- benchmark sample identity,
- GRCh38/chr22 configuration,
- benchmark scales,
- and essential reproducibility metadata.

## Run tests

From the repository root:

```bash
python -m pytest tests/
