# Manuscript Draft — Results and Methods

## Working Title
Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chr22 reference regions

## Results

### Expansion of GIAB chr22 regional benchmarking from 5 to 50 regions

To evaluate the robustness of the variant-calling workflow, benchmarking was expanded from an initial 5-region chr22 validation set to 25 regions and finally to 50 GIAB HG001 GRCh38 chr22 high-confidence regions.

In the 5-region benchmark, 444 normalized truth variants were evaluated. The workflow recovered 428 shared variants, with 16 truth-only missed variants and 0 project-only extra variants. This resulted in 96.40% recall, 100.00% precision, and 98.17% F1.

In the 25-region benchmark, 1504 normalized truth variants were evaluated. The workflow recovered 1421 shared variants, with 83 truth-only missed variants and 0 project-only extra variants. This resulted in 94.48% recall, 100.00% precision, and 97.16% F1.

In the final 50-region benchmark, 2592 normalized truth variants were evaluated. The workflow recovered 2469 shared variants, with 123 truth-only missed variants and 0 project-only extra variants. This resulted in 95.25% recall, 100.00% precision, and 97.57% F1.

Overall, the benchmark remained stable as the number of evaluated regions increased. The 50-region result provided the strongest normalized comparison because it evaluated the largest number of truth variants and genomic contexts.

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

Benchmark regions were selected from GIAB chr22 high-confidence intervals. The analysis was progressively scaled from 5 regions to 25 regions and finally to 50 chr22 regions. This stepwise design allowed the workflow to be tested first on a small validation set and then expanded to reduce cherry-picking bias and improve robustness.

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

## Limitations

This study used a regional chr22 benchmark rather than a full whole-genome benchmark. Although the 50-region design provides stronger evidence than a small regional test, it does not represent all genomic contexts across the human genome.

The workflow also showed reduced sensitivity for indels in difficult genomic regions. Further improvement should focus on indel-sensitive variant calling, local realignment or assembly-based calling, and broader benchmarking across additional chromosomes or whole-genome truth sets.

## Conclusion

This work establishes a reproducible, benchmark-aware regional WGS variant-calling validation workflow using GIAB HG001 chr22 high-confidence regions. The final formal RTG vcfeval benchmark achieved 99.84% precision, 95.10% sensitivity, and 97.41% F-measure across 50 regions. Remaining limitations were concentrated in indel and difficult-region variant detection.
