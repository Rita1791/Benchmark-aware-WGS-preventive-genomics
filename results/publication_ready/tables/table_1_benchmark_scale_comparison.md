# Table 1. Benchmark Scale Comparison

## Purpose

Comparison of normalized variant-calling performance across progressively expanded GIAB HG001 GRCh38 chr22 benchmark regions.

| Benchmark | Truth Variants | Project Variants | Shared | Missed Truth | Extra Project | Recall | Precision | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 5-region chr22 | 444 | 428 | 428 | 16 | 0 | 96.40% | 100.00% | 98.17% |
| 25-region chr22 | 1,504 | 1,421 | 1,421 | 83 | 0 | 94.48% | 100.00% | 97.16% |
| 50-region chr22 | 2,592 | 2,469 | 2,469 | 123 | 0 | 95.25% | 100.00% | 97.57% |

## Interpretation

The normalized comparison maintained high precision across all three benchmark scales.

The 50-region analysis provides the broadest validation scope and achieved 95.25% recall, 100.00% precision, and 97.57% F1 across 2,592 normalized truth variants.

The benchmark scales represent progressively expanded regional validation and should not be interpreted as independent biological replicates.
