# Day 7 — Clean Benchmark Report and Error Analysis

## Goal:
To clean the Day 6 multi-region GIAB chr22 benchmark results and analyze the missed truth variants.

## Starting Point:
Day 6 completed a 5-region GIAB HG001 GRCh38 chr22 benchmark.

Final Day 6 combined result:
- Truth variants: 444
- Project variants: 428
- Shared variants: 428
- Truth-only missed variants: 16
- Project-only variants: 0
- Recall: 96.40%
- Precision: 100.00%
- F1: 98.17%

## Today’s Plan:
1. Generate a clean benchmark report.
2. Recompute metrics directly from isec files.
3. Extract all missed GIAB-only variants.
4. Classify missed variants by type.
5. Interpret whether missed variants are mostly indels/repeat-context variants.

## Scientific Reason:
Benchmarking is incomplete without error analysis. Missed variants need to be inspected to understand whether errors are due to SNP calling, indel representation, homopolymers, repeat regions, or coverage/calling limitations.

## Expected Output:
- Clean multi-region benchmark TSV
- Clean multi-region benchmark Markdown report
- Missed variant analysis TSV
- Biological interpretation of missed variants
