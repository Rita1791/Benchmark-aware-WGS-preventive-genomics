# Day 9 — Expanded chr22 50-Region GIAB Benchmark

## Goal:
To expand the GIAB HG001 GRCh38 chr22 benchmark from 25 regions to 50 high-confidence regions.

## Starting Point:
Day 8 completed a 25-region chr22 benchmark.

25-region result:
- Total normalized truth variants: 1504
- Project variants: 1421
- Shared variants: 1421
- Truth-only missed variants: 83
- Project-only extra variants: 0
- Recall: 94.48%
- Precision: 100.00%
- F1: 97.16%

## Work Done:
Expanded the regional benchmark to 50 chr22 high-confidence regions.

## 50-Region Combined Result:
- Total normalized truth variants: 2592
- Total project variants: 2469
- Shared variants: 2469
- Truth-only missed variants: 123
- Project-only extra variants: 0
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

## Missed Variant Type Analysis:
- Deletions: 66
- Insertions: 56
- SNVs: 1

## Difficult-Region Analysis:
- 77 missed variants had difficult-region annotation.

## Initial Scientific Interpretation:
The 50-region benchmark confirms strong regional concordance with GIAB HG001 truth data. The workflow recovered 2469 of 2592 normalized truth variants and produced no project-only extra variants after normalization.

The result improved slightly compared with the 25-region benchmark, supporting the robustness of the workflow across a broader regional test set.

Most missed variants were indels, with only one missed SNV. This suggests that remaining limitations are concentrated in indel calling and difficult genomic contexts rather than broad SNV-calling failure.

## Limitation:
This remains a regional chr22 benchmark, not full-chromosome or whole-genome benchmarking.

## Next Step:
Perform low-recall diagnostic analysis for the 50-region benchmark and compare 5-region, 25-region, and 50-region performance.

---

# Day 9B — 50-Region Low-Recall Analysis and Scale Comparison

## Work Completed:
After completing the 50-region GIAB chr22 benchmark, low-recall diagnostic analysis and benchmark-scale comparison were performed.

## Files Created:
- results/benchmark_valid_chr22_50_region/reports/low_recall_region_summary.tsv
- results/benchmark_valid_chr22_50_region/reports/low_recall_missed_variants.tsv
- results/benchmark_valid_chr22_50_region/reports/low_recall_region_interpretation.md
- results/final_comparison/benchmark_scale_comparison.tsv
- results/final_comparison/benchmark_scale_comparison.md

## 50-Region Benchmark Result:
- Total normalized truth variants: 2592
- Total project variants: 2469
- Shared variants: 2469
- Truth-only missed variants: 123
- Project-only extra variants: 0
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

## 50-Region Missed Variant Pattern:
- Deletions: 66
- Insertions: 56
- SNVs: 1
- Difficult-region missed variants: 77

## Low-Recall Region Analysis:
Ten regions had recall below 92%.

In these low-recall regions:
- Total missed variants: 56
- Deletions: 31
- Insertions: 24
- SNVs: 1
- Difficult-region missed variants: 32

## Scale Comparison:
The benchmark was compared across 5, 25, and 50 chr22 regions.

5-region result:
- Truth variants: 444
- Recall: 96.40%
- Precision: 100.00%
- F1: 98.17%

25-region result:
- Truth variants: 1504
- Recall: 94.48%
- Precision: 100.00%
- F1: 97.16%

50-region result:
- Truth variants: 2592
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

## Scientific Interpretation:
The benchmark remained stable as the validation expanded from 5 to 25 and then 50 chr22 regions. The 50-region benchmark provides the strongest current evidence because it evaluates the largest number of truth variants and genomic contexts.

Across all scales, precision remained 100%, meaning no project-only extra variants were detected after normalization. Missed variants were consistently dominated by insertions and deletions, with only one missed SNV in the 25-region and 50-region analyses.

This indicates that the remaining limitations are mainly related to indel detection in difficult genomic contexts, not broad variant-calling failure.

## Final Day 9 Conclusion:
The 50-region GIAB HG001 GRCh38 chr22 benchmark achieved strong regional concordance with truth data. The workflow reached 95.25% recall, 100.00% precision, and 97.57% F1 across 2592 normalized truth variants. The result is suitable as the current strongest benchmark result for the WGS/NGS pipeline research.

## Next Step:
The next stage should be formal benchmarking using hap.py or vcfeval on selected regions, or expansion to 100 chr22 regions after preserving the 50-region results as the current validated milestone.
