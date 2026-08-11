# Table 2. Formal RTG vcfeval Benchmark Result

## Purpose

Formal benchmark evaluation of the 50-region GIAB HG001 GRCh38 chr22 validation using RTG vcfeval.

| Benchmark | TP Baseline | TP Call | False Positives | False Negatives | Precision | Sensitivity | F-measure |
|---|---:|---:|---:|---:|---:|---:|---:|
| RTG vcfeval — 50-region chr22 | 2,465 | 2,465 | 4 | 127 | 99.84% | 95.10% | 97.41% |

## Interpretation

RTG vcfeval identified 2,465 true-positive matches, four false positives, and 127 false negatives.

The resulting formal benchmark performance was 99.84% precision, 95.10% sensitivity, and 97.41% F-measure.

The formal result is complementary to the normalized bcftools isec comparison and provides a stricter benchmark-oriented assessment.
