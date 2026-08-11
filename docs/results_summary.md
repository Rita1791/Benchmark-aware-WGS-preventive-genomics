# Results Summary

## 1. Benchmark scale comparison

The workflow was evaluated using progressively expanded chromosome 22 benchmark regions.

| Benchmark | Truth variants | Shared | Missed | Extra | Recall | Precision | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5-region | 444 | 428 | 16 | 0 | 96.40% | 100.00% | 98.17% |
| 25-region | 1,504 | 1,421 | 83 | 0 | 94.48% | 100.00% | 97.16% |
| 50-region | 2,592 | 2,469 | 123 | 0 | 95.25% | 100.00% | 97.57% |

## 2. Formal RTG benchmark

The final 50-region evaluation produced:

| Metric | Result |
|---|---:|
| True positives | 2,465 |
| False positives | 4 |
| False negatives | 127 |
| Precision | 99.84% |
| Sensitivity | 95.10% |
| F-measure | 97.41% |

## 3. Normalized versus formal benchmarking

The normalized comparison produced:

- Precision: 100.00%
- Recall: 95.25%
- F1: 97.57%

RTG `vcfeval` produced:

- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

The formal benchmark therefore identified four false positives and four additional false negatives relative to the direct normalized comparison.

## 4. Missed variants

Among the 123 missed variants identified in the normalized 50-region comparison:

| Variant type | Count |
|---|---:|
| Deletion | 66 |
| Insertion | 56 |
| SNV | 1 |

A total of 77 missed variants had difficult-region annotations.

## 5. Low-recall regions

Ten regions had recall below 92%.

These regions contained:

- 56 missed variants,
- 31 deletions,
- 24 insertions,
- 1 SNV,
- 32 difficult-region annotated missed variants.

## 6. Main finding

The dominant error pattern was associated with indel detection rather than broad SNV failure.

The results suggest that further workflow improvement should focus on:

- indel-sensitive calling,
- difficult genomic regions,
- complex/repetitive sequence contexts,
- broader benchmark coverage.

## 7. Interpretation

The workflow demonstrates high benchmark performance within the evaluated chromosome 22 regional framework.

The results should not be interpreted as evidence of whole-genome clinical diagnostic accuracy because the current study does not evaluate the complete genome.
