# Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chromosome 22 reference regions

## Abstract

Accurate variant calling is essential for downstream genomic interpretation, but reproducibility and benchmark validation remain critical requirements before research or clinical translation. This study developed and evaluated a reproducible WGS variant-calling validation workflow using Genome in a Bottle HG001 / NA12878 reference material and GRCh38 chromosome 22 high-confidence benchmark regions. The workflow was progressively evaluated across 5, 25, and 50 regional chr22 validation sets using normalized bcftools isec comparison and formal RTG vcfeval benchmarking. In the final 50-region normalized comparison, 2592 truth variants were evaluated, with 2469 shared variants, 123 truth-only missed variants, and 0 project-only extra variants, corresponding to 95.25% recall, 100.00% precision, and 97.57% F1. Formal RTG vcfeval benchmarking across the same 50 regions identified 2465 true positives, 4 false positives, and 127 false negatives, corresponding to 99.84% precision, 95.10% sensitivity, and 97.41% F-measure. Missed variants were dominated by indels, including 66 deletions and 56 insertions, with only one missed SNV. A total of 77 missed variants had difficult-region annotations. These results demonstrate a a reproducible benchmark-aware regional validation framework and identify indel detection in difficult genomic contexts as the major remaining limitation.

## Keywords

Whole-genome sequencing; variant calling; Genome in a Bottle; HG001; NA12878; GRCh38; chromosome 22; RTG vcfeval; bcftools; benchmark validation; indel detection; bioinformatics workflow

## Introduction

Whole-genome sequencing has become a foundational technology for human genomics, precision medicine, population genetics, and translational bioinformatics. However, the utility of WGS depends heavily on the accuracy and reproducibility of variant-calling workflows. False positives can lead to overinterpretation, while false negatives can obscure biologically relevant variants. Therefore, benchmark-aware validation using well-characterized reference materials is essential before applying variant-calling pipelines to downstream interpretation.

Genome in a Bottle provides high-confidence reference materials and benchmark callsets for human genome analysis. HG001 / NA12878 is one of the most widely used benchmark samples and enables systematic evaluation of variant-calling workflows against curated truth variants and confident genomic regions. Benchmarking against GIAB truth data allows a workflow to be evaluated quantitatively in terms of true positives, false positives, false negatives, precision, sensitivity, and F-measure.

This study focuses on building a reproducible regional WGS variant-calling validation workflow using GIAB HG001 GRCh38 chromosome 22 benchmark regions. Chromosome 22 was selected as a tractable benchmark target for iterative workflow development, formal validation, and error analysis. The workflow was progressively scaled from 5 to 25 and finally 50 benchmark regions. The final evaluation combined normalized bcftools isec comparison with formal RTG vcfeval benchmarking, followed by missed variant, low-recall region, and discrepancy analyses.

## Results

### Progressive expansion of GIAB chr22 regional benchmarking

Benchmarking was expanded from an initial 5-region chr22 validation set to 25 regions and finally to 50 GIAB HG001 GRCh38 chr22 high-confidence regions.

In the 5-region benchmark, 444 normalized truth variants were evaluated. The workflow recovered 428 shared variants, with 16 truth-only missed variants and 0 project-only extra variants. This resulted in 96.40% recall, 100.00% precision, and 98.17% F1.

In the 25-region benchmark, 1504 normalized truth variants were evaluated. The workflow recovered 1421 shared variants, with 83 truth-only missed variants and 0 project-only extra variants. This resulted in 94.48% recall, 100.00% precision, and 97.16% F1.

In the final 50-region benchmark, 2592 normalized truth variants were evaluated. The workflow recovered 2469 shared variants, with 123 truth-only missed variants and 0 project-only extra variants. This resulted in 95.25% recall, 100.00% precision, and 97.57% F1.

Performance remained within a relatively narrow range across the evaluated benchmark scales, although recall decreased from 96.40% at 5 regions to 94.48% at 25 regions before increasing to 95.25% at 50 regions.

### Formal RTG vcfeval benchmarking

To strengthen the evaluation beyond normalized record-based comparison, RTG vcfeval was performed across all 50 chr22 benchmark regions.

The formal RTG vcfeval benchmark identified 2465 true positives, 4 false positives, and 127 false negatives. This corresponded to 99.84% precision, 95.10% sensitivity, and 97.41% F-measure.

Compared with the normalized bcftools isec result, RTG vcfeval produced a slightly stricter benchmark. bcftools isec reported 2469 shared variants, 0 project-only extra variants, and 123 truth-only missed variants, while RTG vcfeval reported 2465 true positives, 4 false positives, and 127 false negatives. The difference was limited to four regions: region_14, region_20, region_30, and region_40.

These results indicate that the workflow maintains high formal benchmarking performance, with very high precision and strong sensitivity across the 50-region chr22 benchmark.

### Missed variant and low-recall region analysis

The 50-region benchmark missed 123 truth variants. Missed variants were dominated by indels, including 66 deletions and 56 insertions, with only 1 missed SNV. A total of 77 missed variants had difficult-region annotations.

Ten regions had recall below 92%. These low-recall regions contained 56 missed variants, including 31 deletions, 24 insertions, and 1 SNV. Thirty-two of these missed variants had difficult-region annotations.

This pattern indicates that the remaining limitations are not broad SNV-calling failures. Instead, the errors are concentrated in indel and difficult-region contexts, including repetitive or complex genomic regions.

### Summary of benchmark performance

The primary formal benchmark result was obtained using RTG vcfeval across 50 chr22 regions, achieving 99.84% precision, 95.10% sensitivity, and 97.41% F-measure.

The supporting normalized bcftools isec comparison achieved 100.00% precision, 95.25% recall, and 97.57% F1.

Together, these results support the reproducibility and benchmark validity of the regional WGS variant-calling workflow while identifying indel and difficult-region detection as the main remaining limitation.

## Methods

### Reference dataset and benchmark design

The benchmark used GIAB HG001 / NA12878 data aligned to the GRCh38 reference genome. The analysis focused on chromosome 22 high-confidence regions to create a tractable regional validation framework.

GIAB HG001 GRCh38 benchmark truth VCF and confident-region BED files were used as the reference standard. A chr22-specific benchmark subset was generated from the full GIAB resource to ensure consistency between the reference sequence, truth variants, confident intervals, and project callsets.

### Regional benchmark selection

Benchmark regions were selected from GIAB chr22 high-confidence intervals. The analysis was progressively scaled from 5 regions to 25 regions and finally to 50 chr22 regions. "This stepwise design allowed the workflow to be tested initially on a small validation set and subsequently expanded to increase the number of evaluated genomic contexts.

### Read extraction and variant calling

For each selected chr22 region, aligned reads were extracted from the GIAB HG001 high-depth BAM file. Regional BAM files were sorted and indexed. Variants were called for each region using the project variant-calling workflow, followed by filtering to retain high-confidence calls.

### VCF normalization

Both project callsets and GIAB truth VCFs were normalized before comparison. Normalization was performed to reduce differences caused by variant representation, especially for indels. Normalized truth and project VCFs were indexed before downstream benchmarking.

### Normalized bcftools isec comparison

Normalized project VCFs were compared against normalized GIAB truth VCFs using bcftools isec. For each region, shared variants, truth-only missed variants, and project-only extra variants were counted. Recall, precision, and F1 were calculated at the region level and combined across all regions.

### Formal RTG vcfeval benchmarking

RTG vcfeval was used as the formal benchmarking tool. The chr22 reference FASTA was converted into RTG SDF format. RTG vcfeval was run independently for each of the 50 benchmark regions using the normalized GIAB truth VCF as the baseline and the normalized project VCF as the callset.

Per-region RTG summary files were aggregated to calculate total true positives, false positives, false negatives, precision, sensitivity, and F-measure across the 50-region benchmark.

### Discrepancy analysis

A discrepancy analysis was performed to compare normalized bcftools isec results with RTG vcfeval results. Region-level differences in true positives, false negatives, and false positives were identified. Four regions showed differences between the two methods, indicating that RTG vcfeval produced a slightly stricter formal benchmark than the normalized record-based comparison.

### Missed variant and difficult-region analysis

Truth-only missed variants were classified by variant type, including deletion, insertion, and SNV. Difficult-region annotations were used to determine whether missed variants occurred in challenging genomic contexts. Low-recall regions were separately analyzed to identify whether reduced sensitivity was associated with variant type or difficult-region enrichment.

## Discussion

This study demonstrates a reproducible benchmark-aware workflow for regional WGS variant-calling validation using GIAB HG001 chr22 reference regions. The stepwise expansion from 5 to 25 and 50 regions showed that the workflow maintained stable performance as benchmark coverage increased. This reduces the risk that the result was driven by a small favorable region set.

The formal RTG vcfeval benchmark produced a slightly stricter result than normalized bcftools isec, identifying 4 false positives and 127 false negatives compared with 0 project-only and 123 truth-only variants from bcftools isec. This difference was small and limited to four regions, supporting strong agreement between the two evaluation approaches while justifying RTG vcfeval as the primary formal benchmark result.

The dominant limitation was missed indel detection. Among 123 missed variants in the 50-region benchmark, 122 were indels and only one was an SNV. This suggests that the workflow is not broadly failing at SNV detection. Instead, the remaining errors are concentrated in variant classes and genomic contexts that are known to be more challenging for short-read variant calling.

## Limitations

This study used a regional chr22 benchmark rather than a full whole-genome benchmark. Although the 50-region design provides stronger evidence than a small regional test, it does not represent all genomic contexts across the human genome.

The workflow also showed reduced sensitivity for indels in difficult genomic regions. Further improvement should focus on indel-sensitive variant calling, local realignment or assembly-based calling, and broader benchmarking across additional chromosomes or whole-genome truth sets.

This workflow should be considered a benchmark-aware research validation framework, not a clinical diagnostic pipeline.

## Conclusion

This work establishes a reproducible, benchmark-aware regional WGS variant-calling validation workflow using GIAB HG001 chr22 high-confidence regions. The final formal RTG vcfeval benchmark achieved 99.84% precision, 95.10% sensitivity, and 97.41% F-measure across 50 regions. Remaining limitations were concentrated in indel and difficult-region variant detection.

## Tables and Figures

- Table 1: Benchmark scale comparison
- Table 2: Formal RTG vcfeval result
- Table 3: Missed variant summary
- Table 4: Low-recall regions
- Table 5: bcftools isec vs RTG vcfeval discrepancy regions
- Figure 1: Benchmark scale performance
- Figure 2: bcftools isec vs RTG vcfeval comparison
- Figure 3: Missed variant type distribution
- Figure 4: Low-recall chr22 benchmark regions
- Figure 5: Benchmark workflow overview
