# Results Summary

## 1. Benchmark-scale comparison

The WGS variant-calling workflow was evaluated using progressively expanded GIAB HG001 GRCh38 chromosome 22 benchmark regions.

| Benchmark | Truth variants | Shared variants | Missed variants | Extra variants | Recall | Precision | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5-region | 444 | 428 | 16 | 0 | 96.40% | 100.00% | 98.17% |
| 25-region | 1,504 | 1,421 | 83 | 0 | 94.48% | 100.00% | 97.16% |
| 50-region | 2,592 | 2,469 | 123 | 0 | 95.25% | 100.00% | 97.57% |

The 50-region evaluation contained the largest number of benchmark variants among the evaluated regional configurations.

Recall decreased from 96.40% at 5 regions to 94.48% at 25 regions before increasing to 95.25% at 50 regions.

Precision remained 100.00% in the normalized comparison across all three evaluated benchmark scopes.

## 2. Final 50-region formal benchmark

The final 50-region evaluation was additionally assessed using RTG `vcfeval`.

| Metric | Result |
|---|---:|
| True positives | 2,465 |
| False positives | 4 |
| False negatives | 127 |
| Precision | 99.84% |
| Sensitivity | 95.10% |
| F-measure | 97.41% |

The RTG result represents the primary formal benchmark for the final 50-region evaluation.

## 3. Normalized versus formal benchmarking

The normalized `bcftools isec` comparison produced:

| Metric | Result |
|---|---:|
| Shared variants | 2,469 |
| Truth-only missed variants | 123 |
| Project-only extra variants | 0 |
| Recall | 95.25% |
| Precision | 100.00% |
| F1 | 97.57% |

The formal RTG `vcfeval` benchmark produced:

| Metric | Result |
|---|---:|
| True positives | 2,465 |
| False positives | 4 |
| False negatives | 127 |
| Precision | 99.84% |
| Sensitivity | 95.10% |
| F-measure | 97.41% |

The two approaches were highly concordant but not identical.

The normalized comparison identified 2,469 shared variants and 123 truth-only variants, whereas RTG `vcfeval` identified 2,465 true positives, 4 false positives, and 127 false negatives.

## 4. Benchmark-method discrepancies

Four benchmark regions showed discrepancies between the normalized comparison and RTG `vcfeval`:

- region_14
- region_20
- region_30
- region_40

These discrepancies demonstrate that benchmark methodology can influence individual variant classifications even when aggregate performance remains highly similar.

## 5. Missed-variant analysis

The normalized 50-region comparison identified 123 truth-only missed variants.

| Variant class | Missed variants |
|---|---:|
| Deletion | 66 |
| Insertion | 56 |
| SNV | 1 |
| **Total** | **123** |

Thus, 122 of 123 missed variants were indels.

The dominant observed error pattern was therefore indel-related rather than broadly distributed across SNVs.

## 6. Difficult-region analysis

Of the 123 missed variants:

- 77 overlapped annotated difficult genomic regions.
- 46 did not have a difficult-region annotation.

The 77 overlapping variants correspond to 62.6% of all missed variants.

This represents substantial overlap between observed misses and difficult genomic contexts.

A formal statistical enrichment analysis is not claimed because an appropriate genomic background set was not evaluated.

## 7. Low-recall regions

Ten benchmark regions had recall below 92%.

These regions contained:

- 56 missed variants,
- 31 deletions,
- 24 insertions,
- 1 SNV,
- 32 missed variants overlapping difficult-region annotations.

The low-recall regions therefore contained a substantial proportion of the observed missed variants and showed the same overall pattern of indel-dominated errors.

## 8. Overall interpretation

The workflow demonstrated high benchmark performance within the evaluated GIAB HG001 GRCh38 chromosome 22 regional framework.

The normalized comparison achieved:

- 95.25% recall,
- 100.00% precision,
- 97.57% F1.

The formal RTG `vcfeval` benchmark achieved:

- 95.10% sensitivity,
- 99.84% precision,
- 97.41% F-measure.

The dominant observed limitation was indel detection, with substantial overlap between missed variants and difficult genomic contexts.

## 9. Scope of interpretation

These results should be interpreted as a regional research validation.

They do not establish:

- whole-genome variant-calling performance,
- clinical diagnostic sensitivity,
- clinical diagnostic specificity,
- clinical validity,
- or clinical utility.

Broader validation across additional chromosomes, benchmark samples, and whole-genome datasets is required before making such claims.

## 10. Key result

The principal result of the study is that the evaluated WGS workflow achieved high precision and approximately 95% sensitivity within the final 50-region GIAB HG001 chromosome 22 benchmark, while the detailed error analysis identified indels and difficult genomic contexts as the primary observed areas for further optimization.
