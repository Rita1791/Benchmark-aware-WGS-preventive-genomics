# Daily Research Log — 2026-06-05

## Research Goal for Today
To select a verified human WGS benchmark dataset for the main WGS/NGS variant discovery workflow.

## Starting Scientific Context
SRR4420293 was identified as Arabidopsis thaliana RNA-seq, not human WGS. Therefore, it was excluded from the human WGS variant-calling workflow.

## Why This Step Was Needed Scientifically
The reference genome, alignment strategy, variant calling method, and benchmarking design depend on the organism and sequencing strategy. For a human WGS pipeline, the dataset must be confirmed as Homo sapiens genomic DNA sequencing.

## Why This Step Matters for Swiss PhD-Level Research
Swiss PhD-level computational genomics requires dataset provenance, benchmarkability, and validation. A verified benchmark dataset such as Genome in a Bottle enables comparison of called variants against high-confidence truth sets.

## Dataset Selection Criteria
The new dataset must satisfy:
- Organism: Homo sapiens
- Library strategy: WGS
- Library source: genomic DNA
- Layout: paired-end preferred
- Publicly accessible
- Benchmarkable against truth data
- Compatible with GRCh38 or GRCh37

## Preferred Dataset Direction
Genome in a Bottle / HG001 / NA12878 benchmark data.

## Commands Run
Pending.

## Key Result
Pending.

## Interpretation
Pending.

## Next Step
Pending.

---

# GIAB Dataset Source Selection

## Step Performed
Selected Genome in a Bottle HG001 / NA12878 as the preferred benchmark direction for the human WGS workflow.

## Why This Step Was Needed Scientifically
A verified human benchmark dataset is required to develop and later validate the WGS variant discovery pipeline. SRR4420293 was excluded because it was Arabidopsis thaliana RNA-seq.

## Why This Matters for Swiss PhD-Level Research
GIAB enables future comparison of called variants against high-confidence truth sets. Benchmarkability is essential for demonstrating variant-calling accuracy, reproducibility, and methodological rigor.

## Local Compute Constraint
The current WSL environment has limited RAM, so full WGS data will not be downloaded blindly. Dataset indexes will be inspected first to identify manageable data sources or subsets.

## Output Files Generated
- reports/dataset_selection/GIAB_HG001_source_selection.md
- reports/dataset_selection/GIAB_HG001_index_files_found.txt

## Interpretation
The project is transitioning from technical FASTQ practice to a verified human WGS benchmark workflow.

## Next Step
Inspect GIAB HG001 / NA12878 index files and choose a manageable Illumina WGS data source for controlled local testing.

---

# GIAB NA12878 Index Inspection

## Step Performed
Inspected available GIAB NA12878 / HG001 index files after cloning the GIAB data index repository.

## Key Candidate Indexes Found
- alignment.index.NA12878_HiSeq_downsampled30X_GRCh37_10262015
- alignment.index.NA12878_Illumina300X_wgs_novoalign_GRCh37_GRCh38_NHGRI_03082016

## Scientific Interpretation
The 300X Illumina WGS dataset is likely too large for the current local WSL environment. The downsampled 30X dataset is more realistic for research design, but the file contents must be inspected before download.

## PhD-Level Reasoning
Dataset choice must consider biological validity, benchmarkability, reference build, file type, and local compute constraints. Blind downloading of large WGS data is not methodologically sound.

## Output File Generated
- reports/dataset_selection/GIAB_NA12878_index_inspection.md

## Next Step
Inspect the contents of the candidate index files and identify whether raw sequence FASTQ data or aligned BAM/CRAM data is most suitable for the next controlled test.

---

# Selected Human WGS Dataset

## Step Performed
Queried metadata for GIAB/NIST HG001 experiment SRX1049768 and identified run SRR2052337.

## Key Metadata
- Experiment: SRX1049768
- Run: SRR2052337
- Sample: NIST HG001 / NA12878
- Organism: Homo sapiens
- Library strategy: WGS
- Library source: GENOMIC
- Library selection: RANDOM
- Platform: Illumina HiSeq 2500
- Total bases: 10,781,482,096
- SRA size: approximately 6.87 GB

## Interpretation
SRR2052337 is a valid human WGS dataset and is suitable for the main FASTQ-to-variant discovery workflow.

## Why This Matters for Swiss PhD-Level Research
The project now uses a verified human WGS benchmark-linked dataset rather than an unsuitable RNA-seq dataset. This enables future alignment, variant calling, annotation, and benchmarking in a scientifically valid human genomics framework.

## Scientific Decision
SRR2052337 is selected as the first verified human WGS dataset for controlled local pipeline development.

## Next Step
Install SRA Toolkit and perform a small controlled FASTQ extraction test before scaling to larger subsets.

---

# 100k Human WGS FASTQ Extraction Result

## Step Performed
Used fastq-dump to extract 100,000 paired-end spots from the locally downloaded SRR2052337 SRA file.

## Command Used
fastq-dump --split-files --gzip -X 100000 -O data/human_wgs_fastq_test data/human_wgs_sra/SRR2052337/SRR2052337.sra

## Output Files
- data/human_wgs_fastq_test/SRR2052337_1.fastq.gz
- data/human_wgs_fastq_test/SRR2052337_2.fastq.gz

## Validation
- R1: 400,000 lines
- R2: 400,000 lines
- Interpretation: 100,000 reads per mate file

## Scientific Interpretation
The selected GIAB HG001 / NA12878 human WGS dataset is accessible and can be used for controlled FASTQ-based pipeline development.

## PhD-Level Significance
This completes the transition from an unsuitable RNA-seq dataset to a validated human WGS benchmark-linked dataset. The pipeline can now proceed with biologically appropriate human genomic data.

## Next Step
Perform FastQC and MultiQC on the 100k human WGS FASTQ subset.

---

# Human WGS 100k QC Completed

## Step Performed
Ran FastQC and MultiQC on the 100,000 paired-end read subset extracted from SRR2052337.

## Input Files
- data/human_wgs_fastq_test/SRR2052337_1.fastq.gz
- data/human_wgs_fastq_test/SRR2052337_2.fastq.gz

## Output Files
- reports/human_wgs_fastqc_100k/SRR2052337_1_fastqc.html
- reports/human_wgs_fastqc_100k/SRR2052337_2_fastqc.html
- reports/human_wgs_multiqc_100k/multiqc_report.html
- reports/human_wgs_multiqc_100k/multiqc_data/multiqc_general_stats.txt
- reports/human_wgs_multiqc_100k/multiqc_data/multiqc_fastqc.txt

## Result
QC report generation completed successfully.

## Interpretation
Pending detailed review of MultiQC statistics.

## Next Step
Inspect MultiQC text outputs and determine whether trimming is required before alignment.


---

# Controlled Human WGS chr22 Alignment Test

## Step Performed
Aligned the 100,000 paired-end read subset from SRR2052337 to a GRCh38 chromosome 22 reference using bwa-mem2 and samtools.

## Output Files
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.sorted.bam
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.sorted.bam.bai
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.flagstat.txt
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.samtools_stats.txt

## Key Results
- Primary reads: 200,000
- Supplementary alignments: 7,459
- Primary mapped reads: 64,402
- Primary mapping rate: 32.20%
- Properly paired reads: 25,854
- Properly paired rate: 12.93%

## Interpretation
The alignment module completed successfully. The mapping rate should not be interpreted as whole-genome alignment performance because the reference used was chromosome 22 only, while the reads were randomly extracted from a whole-genome sequencing run.

## PhD-Level Significance
This confirms that the project can process a verified human WGS dataset from FASTQ to sorted BAM under constrained local computing conditions. It establishes a reproducible, staged alignment checkpoint.

## Limitation
This is a technical validation test, not final whole-genome biological analysis.

## Next Step
Design the next stage: either region-specific read extraction for chr22-focused variant calling or full-reference alignment on a more suitable compute environment.


---

# Technical Variant Calling Test

## Step Performed
Performed variant calling on the SRR2052337 100k chr22 BAM using bcftools mpileup and bcftools call.

## Output Files
- results/human_wgs_variant_calling_100k_chr22/SRR2052337_100k_chr22.raw.vcf.gz
- results/human_wgs_variant_calling_100k_chr22/SRR2052337_100k_chr22.raw.vcf.gz.csi

## Raw Variant Count
27,574

## Initial Observation
The first raw VCF records showed very low depth values, including DP=1 and DP=2. Therefore, these raw calls are not reliable for biological interpretation.

## Scientific Interpretation
The technical VCF-generation step succeeded. However, because the BAM was generated from a small random whole-genome subset aligned only to chr22, this VCF is a technical proof-of-pipeline output, not a final biological callset.

## PhD-Level Significance
This completes the first end-to-end human WGS mini-pipeline from FASTQ to VCF under local low-memory constraints. The next research requirement is to improve biological validity through better region-specific extraction, full-reference alignment, or benchmark-compatible data design.

## Next Step
Apply basic quality filtering and compare raw versus filtered variant counts.


---

# VCF Filtering Completed

## Step Performed
Filtered the raw bcftools VCF generated from the SRR2052337 100k chr22 alignment test.

## Filter Criteria
- QUAL >= 30
- DP >= 5
- MQ >= 30

## Raw Variant Count
27,574

## Filtered Variant Count
1,138

## Output Files
- results/human_wgs_variant_calling_100k_chr22/SRR2052337_100k_chr22.raw.vcf.gz
- results/human_wgs_variant_calling_100k_chr22/SRR2052337_100k_chr22.filtered_QUAL30_DP5_MQ30.vcf.gz

## Interpretation
The filtering step successfully reduced the raw VCF from 27,574 variants to 1,138 higher-confidence technical calls.

## Scientific Meaning
This confirms that the pipeline can proceed from verified human WGS FASTQ files through QC, alignment, BAM generation, variant calling, and variant filtering.

## Limitation
This is not a final biological variant callset because the input reads were randomly sampled from a whole-genome run and aligned only to chr22.

## PhD-Level Significance
The work demonstrates a staged and reproducible mini-pipeline under constrained local computing conditions. The project now has a validated technical pathway from human WGS FASTQ to filtered VCF.

## Next Step
Design a stronger benchmark-compatible test using either full human reference alignment, region-specific extraction, or GIAB truth-set comparison.
