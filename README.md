<h1 align="center">Benchmark-Aware WGS</h1>

<p align="center">
  <strong>A regional GIAB study of where small-variant calling succeeds—and where it breaks.</strong>
</p>

<p align="center">
  HG001 / NA12878 · GRCh38 chromosome 22 · 5 → 25 → 50 regions<br />
  <code>bcftools isec</code> + RTG <code>vcfeval</code> + regional error analysis
</p>

<p align="center">
  <a href="#01--the-question">
    <img src="assets/README_Hero_Benchmark_Aware_WGS.gif" alt="Animated Benchmark-Aware WGS research overview" width="100%" />
  </a>
</p>

<p align="center">
  <sub>Animated research overview · <a href="assets/README_Hero_Benchmark_Aware_WGS.svg">open the editable vector master</a></sub>
</p>

<p align="center">
  <a href="#02--the-answer-in-60-seconds"><img src="https://img.shields.io/badge/READ_THE_RESULT-E30613?style=for-the-badge" alt="Read the result" /></a>
  <a href="results/publication_ready/README.md"><img src="https://img.shields.io/badge/OPEN_THE_EVIDENCE-111111?style=for-the-badge&logo=databricks&logoColor=white" alt="Open the evidence" /></a>
  <a href="#06--reproduce-the-study"><img src="https://img.shields.io/badge/REPRODUCE-FFFFFF?style=for-the-badge&logo=anaconda&logoColor=111111" alt="Reproduce the study" /></a>
  <a href="#09--connect"><img src="https://img.shields.io/badge/CONNECT_WITH_RESEARCHERS-E30613?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect with the researchers" /></a>
</p>

<p align="center">
  <a href="config/benchmark.yaml"><img src="https://img.shields.io/badge/GIAB-HG001-111111?style=flat-square" alt="GIAB HG001" /></a>
  <a href="config/benchmark.yaml"><img src="https://img.shields.io/badge/Reference-GRCh38_chr22-111111?style=flat-square" alt="GRCh38 chromosome 22" /></a>
  <a href="environment.yml"><img src="https://img.shields.io/badge/Python-3.11-111111?style=flat-square&logo=python&logoColor=white" alt="Python 3.11" /></a>
  <a href="#07--reproducibility-audit"><img src="https://img.shields.io/badge/Status-Research_Workflow-E30613?style=flat-square" alt="Research workflow" /></a>
  <a href="#08--scientific-boundary"><img src="https://img.shields.io/badge/Clinical_Use-Not_Validated-E30613?style=flat-square" alt="Not clinically validated" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-111111?style=flat-square" alt="MIT License" /></a>
</p>

[!IMPORTANT]Scope before score. This repository reports regional analytical validation within selected GIAB HG001 high-confidence regions on chromosome 22. It is not whole-genome validation, a clinical diagnostic pipeline, or evidence of clinical sensitivity or specificity.

<a id="navigator"></a>

Research navigator

<table>
  <tr>
    <td width="33%" valign="top">
      <strong>01 — <a href="#01--the-question">QUESTION</a></strong><br /><br />
      Why a high aggregate score is not the end of a benchmark.
    </td>
    <td width="33%" valign="top">
      <strong>02 — <a href="#02--the-answer-in-60-seconds">RESULT</a></strong><br /><br />
      The formal benchmark and the failure signature in one minute.
    </td>
    <td width="33%" valign="top">
      <strong>03 — <a href="#03--experimental-design">DESIGN</a></strong><br /><br />
      The staged regional experiment and two comparison lenses.
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <strong>04 — <a href="#04--visual-evidence">FIGURES</a></strong><br /><br />
      Full-resolution, evidence-linked result figures.
    </td>
    <td width="33%" valign="top">
      <strong>05 — <a href="#05--evidence-index">EVIDENCE</a></strong><br /><br />
      Direct routes to compact data, methods, code, and limitations.
    </td>
    <td width="33%" valign="top">
      <strong>09 — <a href="#09--connect">RESEARCHERS</a></strong><br /><br />
      Roles, contributions, and verified contact routes.
    </td>
  </tr>
</table>

<a id="01--the-question"></a>

01 — The question

Most variant-calling benchmarks stop at a single score. This study does not.

When a short-read WGS workflow performs well overall, which variants are still missed, where do those misses occur, and does the benchmarking method change the conclusion?

The first result was deliberately challenged at broader regional scopes:

<div align="center">

5 REGIONS → 25 REGIONS → 50 REGIONS

initial validation → broader challenge → primary regional analysis

</div>

The three scopes are progressive expansions within the same benchmark genome. They are not independent samples or biological replicates.

<a id="02--the-answer-in-60-seconds"></a>

02 — The answer in 60 seconds

<table>
  <tr>
    <td align="center" width="20%">
      <a href="results/benchmark_metrics.csv"><strong>2,592</strong></a><br />
      <sub>truth variants<br />50-region scope</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/final_summary.csv"><strong>99.84%</strong></a><br />
      <sub>RTG formal<br />precision</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/final_summary.csv"><strong>95.10%</strong></a><br />
      <sub>RTG formal<br />sensitivity</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/final_summary.csv"><strong>97.41%</strong></a><br />
      <sub>RTG formal<br />F-measure</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/variant_class_summary.csv"><strong>122 / 123</strong></a><br />
      <sub>normalized misses<br />were indels</sub>
    </td>
  </tr>
</table>

One-sentence result

The workflow achieved strong regional performance, but its residual error was not random: 122 of 123 normalized truth-only misses were insertions or deletions, identifying indel sensitivity in difficult local contexts as the principal optimization target.

Staged normalized comparison

Scope

Truth

Shared

Missed

Extra

Recall

Precision

F1

5 regions

444

428

16

0

96.40%

100.00%

98.17%

25 regions

1,504

1,421

83

0

94.48%

100.00%

97.16%

50 regions

2,592

2,469

123

0

95.25%

100.00%

97.57%

<p align="center">
  <a href="results/benchmark_metrics.csv"><strong>Source CSV</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="results/publication_ready/tables/table_1_benchmark_scale_comparison.tsv"><strong>Machine-readable Table 1</strong></a>
</p>

Formal comparison: two matching philosophies

50-region benchmark

TP / shared

FP

FN

Precision

Recall / sensitivity

F1 / F-measure

Normalized bcftools isec

2,469

0

123

100.00%

95.25%

97.57%

Primary RTG vcfeval

2,465

4

127

99.84%

95.10%

97.41%

[!NOTE]The normalized 100% precision is a record-level result inside selected HG001 chr22 high-confidence regions. It is not a clinical specificity estimate. RTG vcfeval, the primary formal benchmark, was slightly more conservative.

<details>
<summary><strong>Why can the methods disagree after VCF normalization?</strong></summary>

<br />

bcftools isec directly compares normalized VCF records. RTG vcfeval performs a more representation-aware truth-versus-query comparison. Biologically equivalent variation can still be encoded differently, allowing the matching method to reclassify a small number of records.

Here, RTG reported four fewer true positives, four additional false negatives, and four false positives.

</details>

Failure signature

pie showData
    title Normalized truth-only misses (n = 123)
    "Deletions" : 66
    "Insertions" : 56
    "SNVs" : 1

Signal

Observation

Interpretation boundary

Missed indels

122 / 123

The normalized residual error is overwhelmingly indel-associated

Documented difficult-context overlap

77 / 123

Descriptive overlap; not a formal enrichment test

Documented low-recall regions

10

Aggregate scores conceal regional weakness

Documented method-discrepant regions

4 / 50

Benchmark logic changes some classifications

The first row is directly reconstructable from committed compact data. The remaining region/context statements are preserved in the analysis documentation, but their optional compact region-level inputs are not currently committed.

<a id="03--experimental-design"></a>

03 — Experimental design

flowchart TB
    A["GIAB HG001 truth<br/>v4.2.1 · GRCh38"] --> B["Paired-end WGS<br/>QC · trim · align"]
    B --> C["Small variants<br/>call · filter · normalize"]
    C --> D{"Two benchmark lenses"}
    D --> E["bcftools isec<br/>record concordance"]
    D --> F["RTG vcfeval<br/>formal validation"]
    E --> G["Regional evidence<br/>errors · contexts · discrepancies"]
    F --> G

<details open>
<summary><strong>Method, from reads to evidence</strong></summary>

<br />

Inspect paired-end reads with FastQC and MultiQC.

Trim and clean reads with fastp.

Align to GRCh38 with BWA-MEM2.

Process alignment files with samtools.

Call small variants using bcftools mpileup + bcftools call.

Apply QUAL >= 30 and DP >= 10 filters.

Normalize truth and query VCFs against the same reference.

Compare normalized records using bcftools isec.

Run the primary formal comparison using RTG vcfeval.

Characterize errors by variant class, region, context, and benchmark disagreement.

</details>

<details>
<summary><strong>Exact configured study setting</strong></summary>

<br />

Component

Setting

Benchmark sample

GIAB HG001 / NA12878

Truth release

GIAB v4.2.1

Reference

GRCh38 chromosome 22

Scope

Selected high-confidence regions

Regional stages

5, 25, and 50 regions

Caller

bcftools mpileup + bcftools call

Calling model

Multiallelic

Filters

QUAL >= 30; DP >= 10

Normalized comparison

bcftools isec

Formal benchmark

RTG vcfeval

Low-recall threshold

92%

Open the canonical configuration →

</details>

<a id="04--visual-evidence"></a>

04 — Visual evidence

<p align="center">Select any panel to inspect the full-resolution figure.</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="results/publication_ready/figures/figure_1_benchmark_scale_performance.png">
        <img src="results/publication_ready/figures/figure_1_benchmark_scale_performance.png" alt="Variant-calling performance across benchmark scales" width="100%" />
      </a><br />
      <strong>01 / Scale stability</strong><br />
      <sub>Recall, precision, and F1 across expanding scopes</sub>
    </td>
    <td width="50%" align="center">
      <a href="results/publication_ready/figures/figure_2_bcftools_vs_rtg_vcfeval.png">
        <img src="results/publication_ready/figures/figure_2_bcftools_vs_rtg_vcfeval.png" alt="Normalized comparison versus RTG vcfeval" width="100%" />
      </a><br />
      <strong>02 / Benchmark agreement</strong><br />
      <sub>Record-level matching versus formal evaluation</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <a href="results/publication_ready/figures/figure_3_missed_variant_type_distribution.png">
        <img src="results/publication_ready/figures/figure_3_missed_variant_type_distribution.png" alt="Distribution of missed variant classes" width="62%" />
      </a><br />
      <strong>03 / Error composition</strong><br />
      <sub>Nearly every normalized miss was an insertion or deletion</sub>
    </td>
  </tr>
</table>

[!CAUTION]The committed figure_4_low_recall_regions.png is a placeholder because its compact source CSV is absent. It is deliberately excluded from the evidence gallery.

<a id="05--evidence-index"></a>

05 — Evidence index

Research route

Direct evidence

Role

Headline metrics

results/benchmark_metrics.csv

Compact staged-benchmark source

Formal comparison

results/final_summary.csv

isec versus RTG metrics

Error classes

results/variant_class_summary.csv

Missed deletions, insertions, and SNVs

Result interpretation

docs/results_summary.md

Consolidated research narrative

Experimental logic

docs/experimental_design.md

Scope, endpoints, and progression

Error analysis

docs/error_analysis.md

Indels, contexts, and discrepancies

Provenance

docs/data_provenance.md

Dataset and reference identity

Limitations

docs/limitations.md

Scientific and clinical boundaries

Processing code

pipeline/

Modular QC → VCF stages

Analysis code

scripts/

Benchmarking, aggregation, and figures

Research record

docs/lab_notebook/

Dated development history

Manuscript

manuscript/manuscript.md

Draft research output

<details>
<summary><strong>Repository anatomy</strong></summary>

Benchmark-aware-WGS-preventive-genomics/
├── config/       benchmark identity, thresholds, settings
├── pipeline/     QC, trimming, alignment, variant calling
├── scripts/      benchmarking, aggregation, analysis, figures
├── docs/         design, provenance, limitations, lab notebook
├── results/      compact metrics, tables, rendered figures
├── reports/      FastQC, fastp, and MultiQC reports
├── manuscript/   draft research material
└── tests/        structural and configuration checks

</details>

<a id="06--reproduce-the-study"></a>

06 — Reproduce the study

Rebuild compact evidence

git clone https://github.com/Rita1791/Benchmark-aware-WGS-preventive-genomics.git
cd Benchmark-aware-WGS-preventive-genomics

conda env create -f environment.yml
conda activate benchmark-aware-wgs

python scripts/19_create_publication_tables.py
python scripts/20_create_publication_figures.py

This rebuilds core staged tables and Figures 1–3 from committed compact CSVs. It does not recreate the missing optional region-level outputs.

Run modular FASTQ → chr22 VCF stages

RAW_DIR=/path/to/fastq bash pipeline/01_qc.sh

RAW_DIR=/path/to/fastq \
TRIM_DIR=/path/to/trimmed \
bash pipeline/02_trim.sh

REFERENCE=/path/to/GRCh38.fa \
TRIM_DIR=/path/to/trimmed \
BAM_DIR=/path/to/bam \
bash pipeline/03_align.sh

REFERENCE=/path/to/GRCh38.fa \
BAM_DIR=/path/to/bam \
VCF_DIR=/path/to/vcf \
REGION=chr22 \
bash pipeline/04_variant_calling.sh

<details>
<summary><strong>External resources required for full benchmarking</strong></summary>

<br />

Matching GRCh38 reference FASTA and indexes

GIAB HG001 v4.2.1 GRCh38 truth VCF and index

Corresponding GIAB high-confidence BED

HG001/NA12878 reads or documented alignment resource

RTG-compatible sequence dictionary

Sufficient compute and storage for WGS BAM/VCF processing

Authoritative starting points: NIST Genome in a Bottle · bcftools · RTG Tools · BWA-MEM2

</details>

<a id="07--reproducibility-audit"></a>

07 — Reproducibility audit

Capability

Status

Interpretation

Inspect headline metrics

●

Ready from committed compact CSVs

Rebuild Tables 1–2 and Figures 1–3

●

Ready from committed inputs and scripts

Run modular FASTQ → chr22 VCF stages

◐

Requires external data, paths, and indexed reference

Rebuild low-recall Figure 4

○

Source results/low_recall_regions.csv is absent

Rebuild region-discrepancy outputs

○

Compact discrepancy rows are not committed

Recreate full 50-region isec + RTG study

◐

External resources and manual orchestration remain

Verify exact historical tool versions

○

Core versions remain TBD

Use for clinical diagnosis

○

Not validated

<sub>● ready · ◐ partial · ○ not ready</sub>

<details>
<summary><strong>Known technical gaps</strong></summary>

<br />

No portable Snakemake or Nextflow workflow orchestrates the complete study.

Some scripts retain local-path and historical-workspace assumptions.

Exact tool versions, URLs, dates, and checksums are incomplete.

Table 3 contains a placeholder for the difficult-region count.

Table 4 contains placeholder rows; Table 5 contains only its header.

The structure test expects an absent reference_datasets/ directory.

Current tests do not establish biological correctness or clean-clone execution.

Read the reproducibility record →

</details>

<a id="08--scientific-boundary"></a>

08 — Scientific boundary

This repository supports

This repository does not support

Regional analytical validation

Whole-genome performance claims

Selected HG001 chr22 high-confidence regions

Multi-sample clinical validation

Normalized isec and formal RTG comparison

Clinical sensitivity or specificity

Descriptive error analysis

Statistical enrichment without a background model

A foundation for broader benchmarking

Pathogenicity, disease-risk, diagnosis, or treatment claims

The term preventive genomics describes a longer-term application context. The implementation currently ends at regional small-variant benchmarking and error analysis.

<details>
<summary><strong>Frequently asked questions</strong></summary>

<br />

Does normalized 100% precision mean clinical accuracy?No. It is a regional record-level result. RTG precision was 99.84% in the same scope, and neither number is clinical specificity.

Are the 5-, 25-, and 50-region stages replicates?No. They are nested expansions of one benchmark sample.

Can the full study run with one command?No. Compact outputs can be rebuilt, but complete benchmarking still requires external resources and manual orchestration.

Why are large resources absent?Reference genomes, truth sets, reads, and alignments are large and externally governed. The repository preserves compact evidence and computational logic.

</details>

<a id="09--connect"></a>

09 — Connect

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Ritika Rajendra Rawat</h3>
      <strong>Project Lead · Bioinformatics Research Assistant · Bioinformatics Lead</strong><br /><br />
      Study design · Workflow development · Benchmarking strategy · Analysis · Interpretation · Visualization · Documentation<br /><br />
      <a href="https://github.com/Rita1791"><strong>GitHub ↗</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
      <a href="https://in.linkedin.com/in/ritika-rawat-551107219"><strong>LinkedIn ↗</strong></a>&nbsp;&nbsp;·&nbsp;&nbsp;
      <a href="mailto:ritikarvl2627@gmail.com?subject=Benchmark-Aware%20WGS%20Research%20Enquiry"><strong>Email ↗</strong></a>
    </td>
    <td width="50%" valign="top">
      <h3>Farheena Azim Faridi</h3>
      <strong>Contributor · Bioinformatics Research Intern · M.Sc. Bioinformatics</strong><br /><br />
      Workflow support · Benchmarking assistance · Testing · Refinement · Documentation<br /><br />
      <a href="CONTRIBUTORS.md"><strong>Verified contribution statement →</strong></a>
    </td>
  </tr>
</table>

<p align="center">
  <a href="mailto:ritikarvl2627@gmail.com?subject=Benchmark-Aware%20WGS%20Research%20Collaboration"><img src="https://img.shields.io/badge/EMAIL_THE_PROJECT_LEAD-E30613?style=for-the-badge&logo=gmail&logoColor=white" alt="Email the project lead" /></a>
  <a href="https://github.com/Rita1791/Benchmark-aware-WGS-preventive-genomics/issues/new"><img src="https://img.shields.io/badge/OPEN_A_RESEARCH_DISCUSSION-111111?style=for-the-badge&logo=github&logoColor=white" alt="Open a research discussion" /></a>
</p>

Developed within the research and computational environment of Nainsense Labs Private Limited. See CONTRIBUTORS.md for transparent attribution.

Citation

Use GitHub's Cite this repository menu or CITATION.cff:

Rawat, R. R. (2026). Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chr22 reference regions [Software].

Released under the MIT License.

<p align="center">
  <strong>HIGH ACCURACY IS THE BEGINNING OF THE INVESTIGATION — NOT THE END.</strong><br />
  <sub>Built to turn a benchmark score into a traceable evidence trail.</sub>
</p>

<p align="center">
  <a href="#navigator">Research navigator ↑</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#09--connect">Connect with researchers</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Rita1791/Benchmark-aware-WGS-preventive-genomics">Star the repository</a>
</p>
