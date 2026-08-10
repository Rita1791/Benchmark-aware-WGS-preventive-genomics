# Day 3 Final Closing Summary — Human WGS Mini-Pipeline

## Date
2026-06-05

## Research Track
WGS/NGS-to-Variant Interpretation Research Framework for Precision Preventive Health

## Main Goal of the Day
To transition from the previously unsuitable Arabidopsis RNA-seq dataset to a verified human WGS dataset and complete a controlled human WGS mini-pipeline.

---

## 1. Dataset Correction and Selection

The previous dataset SRR4420293 was excluded because it was confirmed as Arabidopsis thaliana RNA-seq, not human WGS.

A new dataset was selected and verified:

- Experiment: SRX1049768
- Run: SRR2052337
- Sample: NIST HG001 / NA12878
- Organism: Homo sapiens
- Library strategy: WGS
- Library source: GENOMIC
- Library selection: RANDOM
- Platform: Illumina HiSeq 2500
- Study: PRJNA200694 / SRP047086

## Scientific Significance
This corrected the biological foundation of the project. The pipeline is now based on a valid human WGS benchmark-linked dataset.

---

## 2. SRA Download and FASTQ Extraction

The SRA file was successfully downloaded:

- data/human_wgs_sra/SRR2052337/SRR2052337.sra
- Size: approximately 6.5 GB

A controlled 100,000 paired-end read subset was extracted using fastq-dump.

Output FASTQ files:

- data/human_wgs_fastq_test/SRR2052337_1.fastq.gz
- data/human_wgs_fastq_test/SRR2052337_2.fastq.gz

Validation:

- R1 line count: 400,000
- R2 line count: 400,000
- Interpretation: 100,000 reads per mate file

## Scientific Significance
This confirmed that the selected human WGS dataset can be accessed locally and converted into valid paired-end FASTQ files.

---

## 3. FASTQ Quality Control

FastQC and MultiQC were run on the 100k paired-end human WGS subset.

Key QC results:

- R1 total sequences: 100,000
- R2 total sequences: 100,000
- Read length: 148 bp
- GC content: 39%
- Duplicate percentage: approximately 0.13%
- FastQC failed modules: 0%
- Adapter content: pass
- Per-base sequence quality: pass

Only warning:

- per-sequence GC content

## Interpretation
The FASTQ subset was acceptable for controlled alignment testing. No trimming was required before the first alignment test.

---

## 4. Controlled chr22 Alignment Test

The 100k paired-end human WGS subset was aligned to a GRCh38 chromosome 22 reference using bwa-mem2 and samtools.

Output files:

- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.sorted.bam
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.sorted.bam.bai
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.flagstat.txt
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.samtools_stats.txt
- results/human_wgs_alignment_100k/SRR2052337_100k_chr22.idxstats.txt

Key alignment statistics:

- Primary reads: 200,000
- Supplementary alignments: 7,459
- Primary mapped reads: 64,402
- Total mapped records: 71,861
- Primary mapping rate: 32.20%
- Properly paired reads: 25,854
- Properly paired rate: 12.93%
- Reads MQ0: 23,093

## Interpretation
The alignment module worked successfully. The mapping rate should not be interpreted as whole-genome mapping performance because the input reads were randomly sampled from WGS and aligned only to chr22.

## Scientific Significance
This confirmed that the pipeline can process verified human WGS FASTQ files into sorted and indexed BAM files under low-memory local conditions.

---

## 5. Variant Calling

Variant calling was performed using bcftools mpileup and bcftools call.

Raw VCF:

- results/human_wgs_variant_calling_100k_chr22/SRR2052337_100k_chr22.raw.vcf.gz

Raw variant count:

- 27,574

Initial observation:

Many raw calls had low read depth, including DP=1 and DP=2.

## Interpretation
The raw VCF proves that the technical BAM-to-VCF step worked. However, the raw variant set is not biologically reliable.

---

## 6. Variant Filtering

The raw VCF was filtered using:

- QUAL >= 30
- DP >= 5
- MQ >= 30

Filtered VCF:

- results/human_wgs_variant_calling_100k_chr22/SRR2052337_100k_chr22.filtered_QUAL30_DP5_MQ30.vcf.gz

Filtered variant count:

- 1,138

## Interpretation
Filtering reduced the callset from 27,574 raw variants to 1,138 higher-confidence technical calls.

## Scientific Limitation
The filtered VCF is still not suitable for clinical or biological interpretation because the alignment used a chr22-only reference with randomly sampled whole-genome reads.

---

## 7. Final Scientific Status

Completed technical mini-pipeline:

Human WGS SRA
→ FASTQ extraction
→ FastQC/MultiQC
→ bwa-mem2 alignment
→ sorted BAM
→ BAM index
→ BAM statistics
→ bcftools variant calling
→ filtered VCF

## Correct Use of Today’s Output
Today’s output is valid as a technical proof-of-pipeline.

## Incorrect Use of Today’s Output
Today’s VCF must not be used for:
- clinical variant interpretation
- nutrigenomics
- disease-risk scoring
- personalised recommendations
- benchmark-grade accuracy claims

---

## 8. PhD-Level Research Lesson

A FASTQ-to-VCF pipeline must be built in stages. Today’s work demonstrated staged, documented, reproducible computational genomics under limited local compute.

The key scientific correction was moving from an invalid RNA-seq dataset to a verified human WGS benchmark-linked dataset.

The key technical achievement was completing the first end-to-end human WGS mini-pipeline from FASTQ to filtered VCF.

---

## 9. Next Research Direction

The next stronger step is to improve biological validity by choosing one of the following:

1. Align to a full human reference genome on stronger compute.
2. Create a region-specific chr22 test using reads truly belonging to chr22.
3. Use GIAB truth sets and confident regions for benchmark comparison.
4. Increase read subset size after confirming compute feasibility.
5. Add annotation using VEP or SnpEff only after a biologically stronger VCF is produced.
