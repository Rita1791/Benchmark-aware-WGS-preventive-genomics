# Day 11 — Publication-Ready Tables and Figures

## Goal:
To convert the 50-region GIAB HG001 chr22 benchmark results into clean publication-ready tables and figures.

## Starting Point:
Day 10 completed formal RTG vcfeval benchmarking across 50 chr22 regions.

Primary formal result:
- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

Supporting normalized bcftools isec result:
- Precision: 100.00%
- Recall: 95.25%
- F1: 97.57%

## Planned Outputs:
- Table 1: Benchmark scale comparison
- Table 2: Formal RTG vcfeval result
- Table 3: Missed variant summary
- Table 4: Low-recall regions
- Table 5: bcftools isec vs RTG vcfeval discrepancy regions
- Figure 1: Benchmark scale performance
- Figure 2: bcftools isec vs RTG vcfeval comparison
- Figure 3: Missed variant type distribution
- Figure 4: Lowest recall regions
- Figure 5: Workflow overview

---

# Day 11 Result — Publication-Ready Tables and Figures Completed

## Work Completed:
Publication-ready tables and figures were generated for the 50-region GIAB HG001 GRCh38 chr22 benchmark.

## Table Outputs:
Generated in:
- results/publication_ready/tables

Tables created:
- Table 1: Benchmark scale comparison
- Table 2: Formal RTG vcfeval result
- Table 3: Missed variant summary
- Table 4: Low-recall regions
- Table 5: bcftools isec vs RTG vcfeval discrepancy regions

Each table was saved in both Markdown and TSV format.

## Figure Outputs:
Generated in:
- results/publication_ready/figures

Figures created:
- Figure 1: Benchmark scale performance
- Figure 2: bcftools isec vs RTG vcfeval comparison
- Figure 3: Missed variant type distribution
- Figure 4: Lowest recall regions
- Figure 5: Workflow overview

All figures were saved as 300 dpi PNG files.

## Caption Output:
Generated in:
- results/publication_ready/captions/publication_table_figure_captions.md

## Primary Benchmark Result:
The formal RTG vcfeval benchmark should be reported as the primary benchmark result:
- Precision: 99.84%
- Sensitivity: 95.10%
- F-measure: 97.41%

## Supporting Benchmark Result:
The normalized bcftools isec comparison should be reported as the supporting benchmark result:
- Precision: 100.00%
- Recall: 95.25%
- F1: 97.57%

## Scientific Interpretation:
The publication-ready outputs show that the variant-calling workflow achieved strong performance across 50 GIAB HG001 GRCh38 chr22 benchmark regions. RTG vcfeval provided a stricter formal benchmark than bcftools isec, but the results remained highly consistent.

The remaining limitations are concentrated in false negatives, mostly indels and difficult-region contexts, while formal precision remained very high at 99.84%.

## Final Day 11 Conclusion:
Day 11 successfully converted the benchmark results into publication-ready tables, figures, and captions. These outputs are ready to support manuscript writing, thesis documentation, CV portfolio presentation, and Swiss PhD application material.

## Next Step:
Prepare the manuscript-style Results section and Methods section using the generated benchmark tables and figures.
