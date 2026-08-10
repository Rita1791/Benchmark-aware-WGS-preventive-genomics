# Day 8 — Expanded chr22 25-Region GIAB Benchmark

## Goal:
To expand the GIAB HG001 GRCh38 chr22 regional benchmark from 5 regions to 25 high-confidence regions.

## Starting Point:
Day 7 produced a clean 5-region chr22 benchmark report.

Final 5-region result:
- Total normalized truth variants: 444
- Project variants: 428
- Shared variants: 428
- Truth-only missed variants: 16
- Project-only extra variants: 0
- Recall: 96.40%
- Precision: 100.00%
- F1: 98.17%

## Reason for Today’s Work:
Five regions are useful, but a larger 25-region benchmark is stronger and reduces cherry-picking concerns.

## Plan:
1. Create a 25-region benchmark script.
2. Select 25 chr22 GIAB high-confidence regions with enough truth variants.
3. Extract regional BAMs from GIAB-aligned BAM.
4. Call variants using bcftools.
5. Filter and normalize VCFs.
6. Compare against GIAB truth using bcftools isec.
7. Generate clean summary and missed-variant analysis.

## Expected Output:
- 25 regional BAMs
- 25 normalized truth VCFs
- 25 normalized project VCFs
- 25 isec comparison folders
- Clean 25-region benchmark report


---

# Day 8 Result — Expanded 25-Region chr22 Benchmark

## Work Completed:
Expanded the GIAB HG001 GRCh38 chr22 benchmark from 5 regions to 25 high-confidence regions.

## Output Check:
- Selected regions: 25
- Regional BAM files: 25
- Normalized truth VCFs: 25
- Normalized project VCFs: 25
- isec comparison folders: 25

## Combined 25-Region Metrics:
- Total normalized truth variants: 1504
- Total project variants: 1421
- Shared variants: 1421
- Truth-only missed variants: 83
- Project-only extra variants: 0
- Recall: 94.48%
- Precision: 100.00%
- F1: 97.16%

## Missed Variant Type Analysis:
- Deletions: 45
- Insertions: 37
- SNVs: 1

## Difficult-Region Analysis:
- 50 of 83 missed variants had difficult-region annotation.
- This is approximately 60.24%.

## Biological Interpretation:
The expanded 25-region benchmark confirms strong regional concordance with GIAB truth data. The pipeline recovered 1421 of 1504 normalized truth variants and produced no project-only extra variants after normalization.

Most missed variants were indels, with only one missed SNV. This suggests that remaining errors are mainly related to indel calling, especially in difficult genomic regions such as homopolymers, simple repeats, and tandem repeats.

## Scientific Conclusion:
The 25-region result is stronger than the earlier 5-region benchmark because it tests more diverse chr22 regions and reduces cherry-picking concerns. The workflow remains highly precise and biologically credible.

## Limitation:
This is an expanded regional chr22 benchmark, not full-chromosome or whole-genome benchmarking.

## Next Step:
Analyze lower-recall regions and missed variants, then expand to 50–100 chr22 regions or transition to formal benchmarking using hap.py or vcfeval.

---

# Day 8B — Low-Recall Region Diagnostic Analysis

## Goal:
To analyze the lower-recall regions from the 25-region chr22 GIAB benchmark and determine why some regions performed below 92% recall.

## Input Files:
- results/benchmark_valid_chr22_25_region/reports/clean_multi_region_benchmark_summary.tsv
- results/benchmark_valid_chr22_25_region/reports/missed_truth_variant_analysis.tsv

## Output Files Created:
- results/benchmark_valid_chr22_25_region/reports/low_recall_region_summary.tsv
- results/benchmark_valid_chr22_25_region/reports/low_recall_missed_variants.tsv
- results/benchmark_valid_chr22_25_region/reports/low_recall_region_interpretation.md

## Low-Recall Regions Identified:
Eight regions had recall below 92%:
- region_2: 91.35%
- region_9: 91.38%
- region_10: 91.38%
- region_13: 90.74%
- region_22: 85.42%
- region_23: 89.58%
- region_24: 87.50%
- region_25: 89.36%

## Missed Variant Summary in Low-Recall Regions:
Total missed variants in low-recall regions: 47

Variant types:
- Deletions: 26
- Insertions: 20
- SNVs: 1

Therefore, 46 of 47 missed variants were indels.

## Difficult-Region Summary:
- 28 of 47 missed variants had difficult-region annotation.
- Difficult-region contexts included homopolymers, simple repeats, and tandem repeats.

## Important Observation:
The only missed SNV was found in region_13 at chr22:49096517 C>G and was located inside a tandem-repeat annotated region.

## Scientific Interpretation:
The lower-recall regions were mainly affected by missed insertions and deletions. Most missed variants were not simple SNVs but indels, and many occurred in difficult genomic contexts.

This suggests that the remaining limitation of the workflow is not general variant-calling failure. Instead, it is concentrated in indel detection and repeat-context variant calling.

## Conclusion:
The 25-region chr22 benchmark remains strong because precision stayed at 100%, and the missed variants are biologically explainable. The low-recall diagnostic analysis supports the conclusion that the workflow performs well under benchmark-compatible conditions, with remaining limitations mainly in difficult indel/repeat regions.

## Next Step:
The next research step should be either:
1. expand to 50–100 chr22 regions, or
2. add formal benchmarking with hap.py or vcfeval for more robust indel comparison.
