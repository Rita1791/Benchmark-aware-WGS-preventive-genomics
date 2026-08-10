# Day 10 — Formal Benchmarking Preparation Using RTG vcfeval

## Goal:
To add a formal variant benchmarking layer using RTG vcfeval on selected GIAB HG001 GRCh38 chr22 regions.

## Starting Point:
Day 9 completed a 50-region GIAB chr22 benchmark using bcftools isec.

Final 50-region result:
- Total normalized truth variants: 2592
- Total project variants: 2469
- Shared variants: 2469
- Truth-only missed variants: 123
- Project-only extra variants: 0
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

## Reason for Day 10:
bcftools isec is useful for exact/normalized VCF comparison, but formal variant benchmarking tools such as RTG vcfeval can provide a stronger comparison framework, especially for indels and complex variant representations.

## Planned Regions:
- region_1: high-performing benchmark region
- region_22: lowest-recall region in 50-region benchmark
- region_24: second-lowest recall region in 50-region benchmark

## Expected Output:
- RTG SDF reference template for chr22
- vcfeval output folders for selected regions
- summary metrics for formal benchmarking
- comparison between bcftools isec and RTG vcfeval

---

# Day 10 Result — Selected Region RTG vcfeval Benchmarking

## Work Completed:
RTG vcfeval was successfully run on three representative chr22 benchmark regions:
- region_1: high-performing region
- region_22: lowest-recall region
- region_24: second-lowest recall region

## Results:

### region_1
- True positives baseline: 103
- True positives call: 103
- False positives: 0
- False negatives: 2
- Precision: 1.0000
- Sensitivity: 0.9810
- F-measure: 0.9904

### region_22
- True positives baseline: 41
- True positives call: 41
- False positives: 0
- False negatives: 7
- Precision: 1.0000
- Sensitivity: 0.8542
- F-measure: 0.9213

### region_24
- True positives baseline: 42
- True positives call: 42
- False positives: 0
- False negatives: 6
- Precision: 1.0000
- Sensitivity: 0.8750
- F-measure: 0.9333

## Interpretation:
The RTG vcfeval results matched the normalized bcftools isec results for the tested regions.

This suggests that the remaining missed variants are likely true false negatives rather than simple VCF representation artifacts.

## Scientific Conclusion:
Formal vcfeval benchmarking supports the previous benchmark interpretation. The pipeline maintains perfect precision in selected representative regions, while remaining sensitivity limitations are concentrated in difficult indel/repeat-context variants.

## Next Step:
Run RTG vcfeval across all 50 chr22 benchmark regions and compare the aggregate result with the bcftools isec 50-region benchmark.
EOFcat >> docs/lab_notebook/2026_06_15_day10_formal_vcfeval_benchmarking.md <<'EOF'

---

# Day 10 Result — Selected Region RTG vcfeval Benchmarking

## Work Completed:
RTG vcfeval was successfully run on three representative chr22 benchmark regions:
- region_1: high-performing region
- region_22: lowest-recall region
- region_24: second-lowest recall region

## Results:

### region_1
- True positives baseline: 103
- True positives call: 103
- False positives: 0
- False negatives: 2
- Precision: 1.0000
- Sensitivity: 0.9810
- F-measure: 0.9904

### region_22
- True positives baseline: 41
- True positives call: 41
- False positives: 0
- False negatives: 7
- Precision: 1.0000
- Sensitivity: 0.8542
- F-measure: 0.9213

### region_24
- True positives baseline: 42
- True positives call: 42
- False positives: 0
- False negatives: 6
- Precision: 1.0000
- Sensitivity: 0.8750
- F-measure: 0.9333

## Interpretation:
The RTG vcfeval results matched the normalized bcftools isec results for the tested regions.

This suggests that the remaining missed variants are likely true false negatives rather than simple VCF representation artifacts.

## Scientific Conclusion:
Formal vcfeval benchmarking supports the previous benchmark interpretation. The pipeline maintains perfect precision in selected representative regions, while remaining sensitivity limitations are concentrated in difficult indel/repeat-context variants.

## Next Step:
Run RTG vcfeval across all 50 chr22 benchmark regions and compare the aggregate result with the bcftools isec 50-region benchmark.
---

# Day 10B — Formal RTG vcfeval Benchmark Across 50 Regions

## Goal:
To run RTG vcfeval formal benchmarking across all 50 chr22 benchmark regions and compare the result with the previous normalized bcftools isec benchmark.

## Work Completed:
RTG vcfeval was run successfully for all 50 GIAB HG001 GRCh38 chr22 benchmark regions.

## Output Check:
- vcfeval output folders: 50
- summary.txt files: 50

## Aggregated RTG vcfeval Result:
- True positives baseline: 2465
- True positives call: 2465
- False positives: 4
- False negatives: 127
- Precision: 0.9984
- Sensitivity: 0.9510
- F-measure: 0.9741

## Percentage Metrics:
- Precision: 99.84%
- Sensitivity / Recall: 95.10%
- F-measure / F1: 97.41%

## Comparison with bcftools isec:
The RTG vcfeval aggregate result was highly consistent with the normalized bcftools isec 50-region benchmark, but not identical.

bcftools isec result:
- Shared variants: 2469
- Project-only extra variants: 0
- Truth-only missed variants: 123
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

RTG vcfeval result:
- True positives baseline: 2465
- True positives call: 2465
- False positives: 4
- False negatives: 127
- Sensitivity: 95.10%
- Precision: 99.84%
- F-measure: 97.41%

## Scientific Interpretation:
The small difference between bcftools isec and RTG vcfeval suggests that formal benchmarking is slightly stricter than normalized record-based comparison.

RTG vcfeval identified 4 false positives and 127 false negatives, compared with 0 project-only and 123 truth-only variants from bcftools isec. Despite this difference, the overall performance remained highly stable.

The formal benchmark confirms that the workflow has high precision and strong sensitivity across 50 chr22 regions. Remaining errors are consistent with earlier missed-variant analysis showing indel and difficult-region limitations.

## Final Day 10 Conclusion:
Formal RTG vcfeval benchmarking strengthened the research by adding an accepted variant-evaluation layer. Across 50 chr22 benchmark regions, the workflow achieved 99.84% precision, 95.10% sensitivity, and 97.41% F-measure.

This result supports the benchmark validity of the WGS/NGS variant-calling workflow while presenting a more rigorous and honest formal evaluation than bcftools isec alone.

## Next Step:
Create a discrepancy report identifying the regions where RTG vcfeval differs from bcftools isec, especially the regions with false positives.


---

# Day 10C — bcftools isec vs RTG vcfeval Discrepancy Analysis

## Goal:
To identify and interpret differences between the normalized bcftools isec comparison and the formal RTG vcfeval benchmark across 50 chr22 regions.

## Files Created:
- results/final_comparison/bcftools_vs_vcfeval_50_region_discrepancy.tsv
- results/final_comparison/bcftools_vs_vcfeval_50_region_discrepancy.md

## Aggregate Comparison:

### bcftools isec:
- Shared variants: 2469
- Project-only extra variants: 0
- Truth-only missed variants: 123
- Recall: 95.25%
- Precision: 100.00%
- F1: 97.57%

### RTG vcfeval:
- True positives: 2465
- False positives: 4
- False negatives: 127
- Sensitivity: 95.10%
- Precision: 99.84%
- F-measure: 97.41%

## Regions with Differences:
Four regions showed differences between bcftools isec and RTG vcfeval:
- region_14
- region_20
- region_30
- region_40

Each of these regions had:
- 1 fewer RTG true positive
- 1 additional RTG false negative
- 1 RTG false positive

## Scientific Interpretation:
RTG vcfeval produced a slightly stricter formal benchmark than normalized bcftools isec. The overall difference was small: 4 fewer true positives, 4 additional false negatives, and 4 false positives.

Despite this stricter classification, the formal benchmark remained very strong:
- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

This supports the robustness of the workflow while providing a more rigorous and publication-ready evaluation layer.

## Final Day 10 Conclusion:
Day 10 successfully added formal RTG vcfeval benchmarking to the project. The 50-region chr22 benchmark is now supported by both normalized bcftools isec comparison and formal vcfeval evaluation.

The formal result should be reported as the primary benchmark result:
- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

The bcftools isec result should be reported as a supporting normalized comparison:
- Precision: 100.00%
- Recall: 95.25%
- F1: 97.57%

## Next Step:
Create final figures and publication-ready result tables for the 50-region benchmark, missed variant analysis, low-recall analysis, and formal vcfeval comparison.
