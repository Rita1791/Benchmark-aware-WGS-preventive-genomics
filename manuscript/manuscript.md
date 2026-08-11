# Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chromosome 22 reference regions

## Abstract

Accurate variant calling is essential for downstream genomic interpretation, but reproducibility and benchmark validation remain critical requirements before research or clinical translation. This study developed and evaluated a reproducible WGS variant-calling validation workflow using Genome in a Bottle HG001/NA12878 reference material and GRCh38 chromosome 22 high-confidence benchmark regions. The workflow was progressively evaluated across 5, 25, and 50 regional chr22 validation sets using normalized `bcftools isec` comparison and formal RTG `vcfeval` benchmarking. In the final 50-region normalized comparison, 2,592 truth variants were evaluated, with 2,469 shared variants, 123 truth-only missed variants, and 0 project-only extra variants, corresponding to 95.25% recall, 100.00% precision, and 97.57% F1. Formal RTG `vcfeval` benchmarking across the same 50 regions identified 2,465 true positives, 4 false positives, and 127 false negatives, corresponding to 99.84% precision, 95.10% sensitivity, and 97.41% F-measure. Missed variants were dominated by indels, including 66 deletions and 56 insertions, with one missed SNV. A total of 77 missed variants overlapped annotated difficult genomic regions. These results demonstrate a reproducible benchmark-aware regional validation framework and identify indel detection in difficult genomic contexts as the primary observed limitation.

## Keywords

Whole-genome sequencing; variant calling; Genome in a Bottle; HG001; NA12878; GRCh38; chromosome 22; RTG vcfeval; bcftools; benchmark validation; indel detection; bioinformatics workflow

## Introduction

Whole-genome sequencing has become a foundational technology for human genomics, precision medicine, population genetics, and translational bioinformatics. However, the utility of WGS depends heavily on the accuracy and reproducibility of variant-calling workflows. False positives can lead to overinterpretation, while false negatives can obscure biologically relevant variants. Benchmark-aware validation using well-characterized reference materials is therefore essential before applying variant-calling pipelines to downstream interpretation.

Genome in a Bottle provides high-confidence reference materials and benchmark callsets for human genome analysis. HG001/NA12878 is one of the widely used benchmark samples and enables systematic evaluation of variant-calling workflows against curated truth variants and confident genomic regions.

This study focuses on a reproducible regional WGS variant-calling validation workflow using GIAB HG001 GRCh38 chromosome 22 benchmark regions. Chromosome 22 was selected as a tractable benchmark target for iterative workflow development, formal validation, and error analysis. The workflow was progressively evaluated using 5, 25, and 50 benchmark regions. The final evaluation combined normalized `bcftools isec` comparison with formal RTG `vcfeval` benchmarking, followed by missed-variant, low-recall-region, and discrepancy analyses.

## Results

### Progressive expansion of GIAB chr22 regional benchmarking

Benchmarking was expanded from an initial 5-region chr22 validation set to 25 regions and finally to 50 GIAB HG001 GRCh38 chr22 high-confidence regions.

In the 5-region benchmark, 444 normalized truth variants were evaluated. The workflow recovered 428 shared variants, with 16 truth-only missed variants and 0 project-only extra variants. This resulted in 96.40% recall, 100.00% precision, and 98.17% F1.

In the 25-region benchmark, 1,504 normalized truth variants were evaluated. The workflow recovered 1,421 shared variants, with 83 truth-only missed variants and 0 project-only extra variants. This resulted in 94.48% recall, 100.00% precision, and 97.16% F1.

In the final 50-region benchmark, 2,592 normalized truth variants were evaluated. The workflow recovered 2,469 shared variants, with 123 truth-only missed variants and 0 project-only extra variants. This resulted in 95.25% recall, 100.00% precision, and 97.57% F1.

Performance remained within a relatively narrow range across the evaluated benchmark scales. Recall decreased from 96.40% at 5 regions to 94.48% at 25 regions before increasing to 95.25% at 50 regions.

### Formal RTG vcfeval benchmarking

RTG `vcfeval` was used as the primary formal benchmarking method across all 50 chr22 benchmark regions.

The formal benchmark identified 2,465 true positives, 4 false positives, and 127 false negatives. This corresponded to 99.84% precision, 95.10% sensitivity, and 97.41% F-measure.

The normalized `bcftools isec` comparison produced 2,469 shared variants, 0 project-only extra variants, and 123 truth-only missed variants. RTG `vcfeval` produced 2,465 true positives, 4 false positives, and 127 false negatives.

Differences were observed in four regions:

- region_14
- region_20
- region_30
- region_40

The two methods therefore showed high overall concordance, while RTG `vcfeval` produced a slightly stricter formal evaluation.

### Missed variant and low-recall region analysis

The normalized 50-region comparison identified 123 truth-only missed variants.

The missed variants consisted of:

| Variant class | Count |
|---|---:|
| Deletion | 66 |
| Insertion | 56 |
| SNV | 1 |

Thus, 122 of 123 missed variants were indels.

A total of 77 missed variants overlapped annotated difficult genomic regions.

Ten regions had recall below 92%. These low-recall regions contained 56 missed variants:

- 31 deletions
- 24 insertions
- 1 SNV

Thirty-two of these missed variants overlapped annotated difficult genomic regions.

Within the evaluated benchmark, the observed errors were concentrated in indel and difficult-region contexts rather than being broadly distributed across SNVs.

## Methods

### Reference dataset and benchmark design

The benchmark used GIAB HG001/NA12878 data and the GRCh38 reference genome. The analysis focused on chromosome 22 high-confidence regions to create a tractable regional validation framework.

GIAB HG001 GRCh38 benchmark truth VCF and confident-region BED files were used as the reference standard. A chromosome 22-specific benchmark subset was generated from the GIAB resources.

### Regional benchmark selection

Benchmark regions were selected from GIAB chromosome 22 high-confidence intervals. The analysis was progressively evaluated using 5, 25, and 50 benchmark regions.

This stepwise design allowed the workflow to be tested initially on a small validation set and subsequently expanded to increase the number of evaluated genomic contexts.

### Read processing and variant calling

Sequencing data were processed using the project WGS workflow, including quality control, trimming, alignment, alignment processing, variant calling, normalization, and benchmark evaluation.

For the benchmark analysis, aligned HG001 reads corresponding to selected chromosome 22 regions were used for regional analysis.

The exact software versions and parameters used for the final reported analysis are documented separately in the repository.

### VCF normalization

Project and GIAB truth VCFs were normalized before direct comparison to reduce differences caused by alternative variant representations, particularly for indels.

Normalized VCF files were indexed before downstream benchmarking.

### Normalized bcftools isec comparison

Normalized project VCFs were compared against normalized GIAB truth VCFs using `bcftools isec`.

The comparison tracked:

- shared variants,
- truth-only missed variants,
- project-only extra variants.

Metrics were calculated as:

$$
Recall = \frac{TP}{TP + FN}
$$

$$
Precision = \frac{TP}{TP + FP}
$$

$$
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
$$

### Formal RTG vcfeval benchmarking

RTG `vcfeval` was used as the primary formal benchmarking tool.

The GRCh38 chromosome 22 reference was prepared for RTG evaluation, and benchmarking was performed across the 50 selected regions using the normalized GIAB truth set and normalized project callset.

Per-region benchmark outputs were aggregated to calculate total true positives, false positives, false negatives, precision, sensitivity, and F-measure.

### Discrepancy analysis

Normalized `bcftools isec` results were compared with RTG `vcfeval` results.

Four regions showed differences between the two evaluation methods:

- region_14
- region_20
- region_30
- region_40

### Missed-variant analysis

Truth-only variants from the normalized 50-region comparison were classified by variant type.

The missed variants were categorized as deletions, insertions, or SNVs.

### Difficult-region analysis

Missed variants were examined for overlap with difficult-region annotations.

This analysis was used to characterize the genomic contexts associated with reduced benchmark sensitivity.

### Low-recall analysis

Regions with recall below 92% were analyzed separately to identify the contribution of variant class and difficult genomic context.

## Discussion

This study establishes a reproducible benchmark-aware workflow for regional WGS variant-calling validation using GIAB HG001 chromosome 22 reference regions.

The progressive evaluation across 5, 25, and 50 regions showed that performance remained high across the evaluated benchmark configurations. The 50-region normalized comparison achieved 95.25% recall, 100.00% precision, and 97.57% F1.

Formal RTG `vcfeval` benchmarking produced a slightly stricter result, with 99.84% precision, 95.10% sensitivity, and 97.41% F-measure. The difference from the normalized comparison was limited to four identified regions.

The dominant observed error category was indel detection. Of the 123 truth-only variants identified in the normalized 50-region comparison, 122 were indels and only one was an SNV.

A substantial proportion of missed variants also overlapped annotated difficult genomic regions. These observations identify indel detection and difficult genomic contexts as priorities for subsequent workflow optimization.

Potential future improvements include evaluation of alternative variant callers, local assembly-based approaches, improved indel representation and filtering, and expanded benchmarking across additional genomic regions and samples.

## Limitations

### Regional scope

The current analysis evaluates selected chromosome 22 benchmark regions rather than the complete human genome.

### Limited genomic representation

Chromosome 22 does not represent the full diversity of sequence complexity across all human chromosomes.

### Indel sensitivity

The principal observed limitation was indel detection. Of the 123 truth-only variants in the normalized 50-region comparison, 122 were indels.

### Difficult genomic contexts

Seventy-seven missed variants overlapped annotated difficult genomic regions.

### Benchmark dependence

Performance depends on the selected truth set, confident regions, reference genome, normalization procedure, and benchmarking methodology.

### Clinical interpretation

This work represents a research validation framework. It does not establish clinical diagnostic accuracy, clinical sensitivity, or clinical specificity and should not be interpreted as a validated clinical diagnostic pipeline.

### Future validation

Future work should include:

- additional chromosomes,
- whole-genome GIAB benchmarking,
- additional benchmark samples,
- independent sequencing datasets,
- alternative variant callers,
- improved indel detection,
- broader difficult-region analysis.

## Conclusion

This work establishes a reproducible benchmark-aware regional WGS variant-calling validation workflow using GIAB HG001 chromosome 22 high-confidence regions.

The final formal RTG `vcfeval` benchmark achieved 99.84% precision, 95.10% sensitivity, and 97.41% F-measure across 50 evaluated regions.

The dominant observed limitations were concentrated in indel and difficult-region variant detection.

The repository provides the computational framework, benchmark definitions, analysis methods, compact derived results, and reproducibility documentation required to inspect and extend the analysis.

## Tables and Figures

### Tables

- Table 1: Benchmark scale comparison
- Table 2: Formal RTG `vcfeval` result
- Table 3: Missed variant summary
- Table 4: Low-recall regions
- Table 5: `bcftools isec` versus RTG `vcfeval` discrepancy regions

### Figures

- Figure 1: Benchmark scale performance
- Figure 2: `bcftools isec` versus RTG `vcfeval` comparison
- Figure 3: Missed variant class distribution
- Figure 4: Low-recall benchmark regions
- Figure 5: WGS benchmark workflow overview
