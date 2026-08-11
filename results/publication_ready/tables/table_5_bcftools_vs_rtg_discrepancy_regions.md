# Table 5. bcftools isec vs RTG vcfeval Discrepancy Regions

## Purpose

Region-level comparison between normalized bcftools isec concordance and formal RTG vcfeval benchmarking across the 50-region GIAB HG001 GRCh38 chr22 benchmark.

## Aggregate Comparison

| Metric | bcftools isec | RTG vcfeval |
|---|---:|---:|
| True/shared positives | 2,469 | 2,465 |
| False positives | 0 | 4 |
| False negatives | 123 | 127 |
| Recall / sensitivity | 95.25% | 95.10% |
| Precision | 100.00% | 99.84% |
| F1 / F-measure | 97.57% | 97.41% |

## Region-Level Discrepancies

| Region | bcftools Shared | RTG TP | TP Diff | bcftools FN | RTG FN | FN Diff | bcftools FP | RTG FP | FP Diff |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [generated region] | [value] | [value] | [value] | [value] | [value] | [value] | [value] | [value] | [value] |

## Interpretation

RTG vcfeval produced a slightly stricter formal benchmark than the normalized bcftools isec comparison.

Across the complete 50-region benchmark, RTG vcfeval identified four fewer true positives, four additional false negatives, and four false positives.

The resulting performance difference was small:

- Precision: 100.00% → 99.84%
- Recall/sensitivity: 95.25% → 95.10%
- F1/F-measure: 97.57% → 97.41%

The agreement between the methods remains strong, while the formal RTG vcfeval result provides the more appropriate benchmark-oriented performance estimate.
