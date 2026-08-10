# Day 7 — Clean Benchmark Report and Missed Variant Error Analysis

## Goal:
To clean the Day 6 multi-region GIAB chr22 benchmark results and perform missed-variant error analysis.

## Starting Point:
Day 6 completed a benchmark-valid 5-region GIAB HG001 GRCh38 chr22 workflow using:
- GIAB-aligned BAM
- GIAB chr22 confident BED regions
- GIAB chr22 truth VCF
- GRCh38 chr22 reference FASTA
- bcftools variant calling
- VCF normalization
- bcftools isec comparison

## Work Done Today:
1. Created a clean multi-region benchmark summary table.
2. Created a clean Markdown benchmark report.
3. Created a missed-truth-variant analysis table.
4. Classified missed variants by type.
5. Counted missed variants located in difficult genomic regions.
6. Added final biological interpretation to the report.

## Report Files Created:
- results/benchmark_valid_multi_region_v2/reports/clean_multi_region_benchmark_summary.tsv
- results/benchmark_valid_multi_region_v2/reports/clean_multi_region_benchmark_report.md
- results/benchmark_valid_multi_region_v2/reports/missed_truth_variant_analysis.tsv

## Clean Multi-Region Benchmark Result:
Five chr22 GIAB high-confidence regions were analyzed.

Per-region metrics:
- region_1: recall 98.10%, precision 100.00%, F1 99.04%
- region_2: recall 91.35%, precision 100.00%, F1 95.48%
- region_3: recall 100.00%, precision 100.00%, F1 100.00%
- region_4: recall 94.67%, precision 100.00%, F1 97.26%
- region_5: recall 98.55%, precision 100.00%, F1 99.27%

## Combined Benchmark Metrics:
- Total normalized GIAB truth variants: 444
- Total project variants: 428
- Shared variants: 428
- Truth-only missed variants: 16
- Project-only extra variants: 0
- Recall: 96.40%
- Precision: 100.00%
- F1: 98.17%

## Missed Variant Error Analysis:
Total missed variants: 16

Variant type classification:
- Deletions: 10
- Insertions: 6
- SNVs: 0

Difficult-region count:
- 8 of 16 missed variants had difficult-region annotation.

## Biological Interpretation:
All missed variants were indels. No SNVs were missed. This suggests that the remaining errors are mainly related to indel calling, not general SNP/variant-calling failure.

Half of the missed variants were located in difficult genomic contexts such as homopolymers, simple repeats, or tandem repeats. These contexts are known to be harder for short-read variant calling.

region_2 showed the lowest recall at 91.35%, likely because it contained more missed indels and difficult-context variants.

The absence of project-only variants after normalization indicates that the workflow produced no extra false-positive records in this benchmark comparison.

## Main Scientific Conclusion:
The 5-region GIAB HG001 GRCh38 chr22 benchmark demonstrates strong regional concordance with truth data. The pipeline recovered 428 of 444 normalized truth variants, with 0 project-only extra variants.

This supports the conclusion that the earlier low-overlap chr22 experiment was caused by weak experimental design, not failure of the variant-calling workflow.

## Limitation:
This result is from 5 selected chr22 high-confidence regions. It is not a full-chromosome or whole-genome benchmark.

## Next Step:
Expand benchmarking to more chr22 regions and later move toward formal benchmarking using hap.py or vcfeval.
