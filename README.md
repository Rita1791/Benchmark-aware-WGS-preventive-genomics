<div align="center">

🧬 Benchmark-Aware WGS

High accuracy is the headline. The error pattern is the finding.

<p>
  Regional analytical validation of a short-read small-variant workflow using<br />
  <strong>GIAB HG001 / NA12878</strong> · <strong>GRCh38 chromosome 22</strong> · <strong>5 → 25 → 50 regions</strong>
</p>

<p>
  <a href="#results-in-60-seconds">
    <img src="https://img.shields.io/badge/EXPLORE_RESULTS-0F766E?style=for-the-badge&logo=databricks&logoColor=white" alt="Explore benchmark results" />
  </a>
  <a href="results/publication_ready/README.md">
    <img src="https://img.shields.io/badge/OPEN_EVIDENCE-1D4ED8?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Open publication-ready evidence" />
  </a>
  <a href="docs/reviewer_summary.md">
    <img src="https://img.shields.io/badge/REVIEWER_BRIEF-6D28D9?style=for-the-badge&logo=academia&logoColor=white" alt="Open reviewer summary" />
  </a>
  <a href="CITATION.cff">
    <img src="https://img.shields.io/badge/CITE_PROJECT-B45309?style=for-the-badge" alt="Cite this project" />
  </a>
</p>

<p>
  <a href="environment.yml"><img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11" /></a>
  <a href="config/benchmark.yaml"><img src="https://img.shields.io/badge/GIAB-HG001-0057B8?style=flat-square" alt="GIAB HG001" /></a>
  <a href="config/benchmark.yaml"><img src="https://img.shields.io/badge/Reference-GRCh38_chr22-F28C28?style=flat-square" alt="GRCh38 chromosome 22" /></a>
  <a href="#reproducibility"><img src="https://img.shields.io/badge/Status-Research_Workflow-6F42C1?style=flat-square" alt="Research workflow" /></a>
  <a href="#scientific-boundaries"><img src="https://img.shields.io/badge/Clinical_Use-Not_Validated-C62828?style=flat-square" alt="Not clinically validated" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2EA44F?style=flat-square" alt="MIT License" /></a>
</p>

<p>
  <a href="https://github.com/Rita1791"><img src="https://img.shields.io/badge/GitHub-Rita1791-181717?style=flat-square&logo=github&logoColor=white" alt="Ritika Rawat on GitHub" /></a>
  <a href="https://in.linkedin.com/in/ritika-rawat-551107219"><img src="https://img.shields.io/badge/LinkedIn-Ritika_Rawat-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="Ritika Rawat on LinkedIn" /></a>
  <a href="mailto:ritika.rawat27@outlook.com?subject=Benchmark-Aware%20WGS%20Research%20Enquiry"><img src="https://img.shields.io/badge/Email-Connect_with_the_Researcher-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Connect with the researcher by email" /></a>
</p>

<strong><code>bcftools isec</code> + RTG <code>vcfeval</code> + regional error analysis</strong>

</div>

<p align="center">
  <a href="results/publication_ready/figures/figure_1_benchmark_scale_performance.png">
    <img src="results/publication_ready/figures/figure_1_benchmark_scale_performance.png" alt="Recall, precision and F1 across the 5-region, 25-region and 50-region benchmark scopes" width="92%" />
  </a>
</p>

<p align="center">
  <sub>👆 Select the figure to inspect the full-resolution evidence.</sub>
</p>

[!IMPORTANT]This is a regional analytical-validation study, not a clinical genomics product. It evaluates selected GIAB HG001 high-confidence regions on chromosome 22; it does not establish whole-genome or clinical performance.

<a id="navigate"></a>

🧭 Choose your route

<table>
  <tr>
    <td align="center" width="33%">
      <strong>🎯 <a href="#research-question">Understand the question</a></strong><br />
      Why one benchmark score is not enough
    </td>
    <td align="center" width="33%">
      <strong>📊 <a href="#results-in-60-seconds">Inspect the result</a></strong><br />
      Read the benchmark in sixty seconds
    </td>
    <td align="center" width="33%">
      <strong>🧪 <a href="#workflow">Follow the workflow</a></strong><br />
      Trace FASTQ to regional error analysis
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <strong>🖼️ <a href="#visual-evidence">Open the figures</a></strong><br />
      View every defensible result at full size
    </td>
    <td align="center" width="33%">
      <strong>🧾 <a href="#evidence-explorer">Audit the evidence</a></strong><br />
      Jump directly to CSV, TSV, methods, and code
    </td>
    <td align="center" width="33%">
      <strong>👩‍💻 <a href="#connect">Connect with the researchers</a></strong><br />
      Contact the project lead or inspect contributions
    </td>
  </tr>
</table>

<a id="research-question"></a>

🎯 The research question

Most variant-calling benchmarks end with a single aggregate score. That score is useful—but incomplete.

When a WGS small-variant workflow performs well overall, which variants are still missed, where do those misses occur, and does the benchmarking method change the conclusion?

The first five-region result was not treated as the final answer. The same benchmark sample was challenged at progressively broader regional scopes:

<div align="center">

5 regions → 25 regions → 50 regions

initial validation → broader challenge → primary regional analysis

</div>

[!NOTE]These are nested evaluation scopes from the same benchmark sample—not independent biological replicates.

<a id="results-in-60-seconds"></a>

⚡ The result in 60 seconds

<table>
  <tr>
    <td align="center" width="20%">
      <a href="results/benchmark_metrics.csv"><strong>2,592</strong></a><br />
      <sub>truth variants<br />in 50 regions</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/final_summary.csv"><strong>95.10%</strong></a><br />
      <sub>formal RTG<br />sensitivity</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/final_summary.csv"><strong>99.84%</strong></a><br />
      <sub>formal RTG<br />precision</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/final_summary.csv"><strong>97.41%</strong></a><br />
      <sub>formal RTG<br />F-measure</sub>
    </td>
    <td align="center" width="20%">
      <a href="results/variant_class_summary.csv"><strong>122 / 123</strong></a><br />
      <sub>normalized misses<br />were indels</sub>
    </td>
  </tr>
</table>

The result is not “the pipeline is perfect.”

The formal RTG benchmark remained strong, but the normalized error profile exposed a specific weakness:

66 deletions were missed.

56 insertions were missed.

Only 1 missed variant was an SNV.

The narrative analysis records 77 of 123 misses in annotated difficult contexts.

10 regions were documented below the configured 92% recall threshold.

bcftools isec and RTG vcfeval differed in 4 of 50 regions.

[!TIP]The next optimization target is not “variant calling” in general. It is indel sensitivity in difficult local contexts.

The first three statements above are directly rebuildable from committed compact CSVs. The difficult-region, low-recall, and region-discrepancy statements are preserved in the analysis documentation, but their optional compact region-level source files are not currently committed. See Reproducibility.

<a id="workflow"></a>

🧪 The experiment in one view

flowchart TB
    A["🧬 Paired-end WGS reads"] --> B["🔍 QC + trimming"]
    B --> C["🧭 GRCh38 alignment"]
    C --> D["🧪 Small-variant calling"]
    D --> E["🧹 Filter + normalize"]
    E --> F{"Two benchmark lenses"}
    F --> G["bcftools isec<br/>record-level concordance"]
    F --> H["RTG vcfeval<br/>formal comparison"]
    G --> I["📊 Regional evidence"]
    H --> I
    I --> J["Misses · contexts · discrepancies"]

<details>
<summary><strong>🔬 Open the complete method in plain language</strong></summary>

<br />

Inspect paired-end reads with FastQC and MultiQC.

Trim and clean the reads with fastp.

Align reads to GRCh38 with BWA-MEM2.

Process alignment files with samtools.

Call small variants with bcftools mpileup + bcftools call.

Apply QUAL >= 30 and DP >= 10 filters.

Normalize truth and query VCFs using the matching GRCh38 reference.

Compare normalized records with bcftools isec.

Run the primary formal comparison with RTG vcfeval.

Characterize missed variants by class, region, difficult-context overlap, and method disagreement.

Method routes: experimental design · methodology · configuration · data provenance

</details>

<details>
<summary><strong>⚙️ Open the exact benchmark configuration</strong></summary>

<br />

Component

Configured study setting

Benchmark genome

GIAB HG001 / NA12878

Truth release

GIAB v4.2.1

Reference

GRCh38

Scope

Selected high-confidence chr22 regions

Regional stages

5, 25, and 50 regions

Caller

bcftools mpileup + bcftools call

Calling model

Multiallelic

Filters

QUAL >= 30; DP >= 10

Record comparison

bcftools isec after normalization

Formal benchmark

RTG vcfeval

Low-recall threshold

92%

Open config/benchmark.yaml →

</details>

<a id="benchmark-performance"></a>

📈 Performance under increasing scope

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
  <a href="results/publication_ready/tables/table_1_benchmark_scale_comparison.tsv"><strong>Open machine-readable Table 1 →</strong></a>
  &nbsp;·&nbsp;
  <a href="results/benchmark_metrics.csv"><strong>Open source metrics →</strong></a>
</p>

The apparent 100% precision belongs only to the normalized record-level comparison inside these selected regions. It is not a clinical specificity estimate and does not survive unchanged under RTG's more representation-aware matching.

Two tools, two matching philosophies

50-region comparison

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

<p align="center">
  <a href="results/publication_ready/tables/table_2_formal_rtg_vcfeval_result.tsv"><strong>Open formal RTG table →</strong></a>
  &nbsp;·&nbsp;
  <a href="results/final_summary.csv"><strong>Compare both methods →</strong></a>
</p>

<details>
<summary><strong>🤔 Why can the methods disagree after normalization?</strong></summary>

<br />

bcftools isec compares normalized VCF records directly. RTG vcfeval performs a more representation-aware truth-versus-query evaluation. Equivalent biological variation can still be encoded differently in VCF, so the benchmark logic can reclassify a small number of records.

Here, RTG reported four fewer true positives, four more false negatives, and four false positives. That is why RTG is treated as the primary formal benchmark.

</details>

<a id="error-fingerprint"></a>

🔎 The error fingerprint

pie showData
    title Composition of 123 normalized truth-only misses
    "Deletions" : 66
    "Insertions" : 56
    "SNVs" : 1

Signal

Observed evidence

Defensible interpretation

Truth-only misses

123

A residual sensitivity gap remains

Missed indels

122 / 123

The normalized error is overwhelmingly indel-associated

Documented difficult-context overlap

77 / 123

Many misses occurred in annotated difficult contexts; formal enrichment was not tested

Documented low-recall regions

10

Aggregate performance hides local weaknesses

Documented method-discrepant regions

4 / 50

Matching logic affected some regional classifications

<details>
<summary><strong>🧬 What can—and cannot—be inferred from 77 difficult-context overlaps?</strong></summary>

<br />

The overlap is descriptively important, but it is not a statistical enrichment result. A valid enrichment claim would require an appropriate genomic background, the proportion of callable truth variants within difficult contexts, and a prespecified statistical comparison.

Read the error analysis →

</details>

<a id="visual-evidence"></a>

🖼️ Visual evidence

<p align="center">Select a figure to open it at full resolution.</p>

<table>
  <tr>
    <td width="50%" align="center">
      <a href="results/publication_ready/figures/figure_1_benchmark_scale_performance.png">
        <img src="results/publication_ready/figures/figure_1_benchmark_scale_performance.png" alt="Performance across increasing benchmark scopes" width="100%" />
      </a><br />
      <strong>📈 Scale test</strong><br />
      <sub>Recall, precision, and F1 across 5, 25, and 50 regions</sub>
    </td>
    <td width="50%" align="center">
      <a href="results/publication_ready/figures/figure_2_bcftools_vs_rtg_vcfeval.png">
        <img src="results/publication_ready/figures/figure_2_bcftools_vs_rtg_vcfeval.png" alt="Comparison of bcftools isec and RTG vcfeval" width="100%" />
      </a><br />
      <strong>⚖️ Method test</strong><br />
      <sub>Normalized record matching versus formal benchmarking</sub>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <a href="results/publication_ready/figures/figure_3_missed_variant_type_distribution.png">
        <img src="results/publication_ready/figures/figure_3_missed_variant_type_distribution.png" alt="Distribution of missed deletions, insertions and SNVs" width="62%" />
      </a><br />
      <strong>🧩 Failure-mode test</strong><br />
      <sub>Nearly every normalized miss was an insertion or deletion</sub>
    </td>
  </tr>
</table>

[!NOTE]The committed figure_4_low_recall_regions.png is a placeholder because results/low_recall_regions.csv is absent. It is intentionally excluded from this evidence gallery.

<a id="evidence-explorer"></a>

🧾 Evidence explorer

You want to inspect…

Open this

Evidence type

Headline staged metrics

results/benchmark_metrics.csv

Compact source CSV

Formal RTG result

results/final_summary.csv

Compact source CSV

Missed-variant classes

results/variant_class_summary.csv

Compact source CSV

Consolidated interpretation

docs/results_summary.md

Results narrative

Study logic and endpoints

docs/experimental_design.md

Experimental design

Indel and context analysis

docs/error_analysis.md

Error interpretation

Dataset identity

docs/data_provenance.md

Provenance record

Known scope limits

docs/limitations.md

Scientific boundaries

Pipeline code

pipeline/

Modular FASTQ → VCF stages

Analysis code

scripts/

Benchmarking, aggregation, figures

Research chronology

docs/lab_notebook/

Dated research record

Manuscript draft

manuscript/manuscript.md

Research narrative

<details>
<summary><strong>🗂️ Open the repository anatomy</strong></summary>

Benchmark-aware-WGS-preventive-genomics/
├── config/       # Benchmark identity, thresholds, and settings
├── pipeline/     # QC, trimming, alignment, and variant calling
├── scripts/      # Benchmarking, aggregation, analysis, and figures
├── docs/         # Design, provenance, limitations, and lab notebook
├── results/      # Compact metrics, tables, and rendered figures
├── reports/      # FastQC, fastp, and MultiQC reports
├── manuscript/   # Draft research material
└── tests/        # Lightweight structural/configuration checks

</details>

<a id="quick-start"></a>

🚀 Quick start

1 · Clone and create the environment

git clone https://github.com/Rita1791/Benchmark-aware-WGS-preventive-genomics.git
cd Benchmark-aware-WGS-preventive-genomics
conda env create -f environment.yml
conda activate benchmark-aware-wgs

2 · Rebuild the committed core tables and figures

python scripts/19_create_publication_tables.py
python scripts/20_create_publication_figures.py

These scripts rebuild the core staged-benchmark tables and Figures 1–3 from committed compact CSVs. The low-recall and discrepancy outputs require optional region-level inputs that are not currently committed.

3 · Run the modular FASTQ → chr22 VCF stages on your own data

Input reads should follow SAMPLE_R1.fastq.gz and SAMPLE_R2.fastq.gz naming.

RAW_DIR=/path/to/fastq \
bash pipeline/01_qc.sh

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

[!CAUTION]The reference FASTA must be indexed for BWA-MEM2 and samtools. A complete benchmark also requires matched GIAB truth resources and RTG reference preparation; the four commands above do not recreate the full study.

<details>
<summary><strong>📦 External resources required for full benchmarking</strong></summary>

<br />

Matching GRCh38 reference FASTA and indexes

GIAB HG001 v4.2.1 GRCh38 small-variant truth VCF and index

Corresponding GIAB high-confidence BED

HG001/NA12878 reads or the documented alignment resource

RTG-compatible sequence dictionary

Sufficient compute and storage for WGS BAM/VCF processing

Authoritative starting points: NIST Genome in a Bottle · bcftools · RTG Tools · BWA-MEM2

</details>

<a id="reproducibility"></a>

🧪 Reproducibility dashboard

Capability

Status

Honest interpretation

Inspect headline metrics

✅

Supported by committed compact CSVs

Rebuild staged tables and Figures 1–3

✅

Supported by committed scripts and compact inputs

Run modular FASTQ → chr22 VCF stages

🟡

Requires user-supplied data, paths, and reference indexes

Rebuild low-recall Figure 4

❌

results/low_recall_regions.csv is absent; committed image is a placeholder

Rebuild region-discrepancy outputs

❌

Compact discrepancy rows are absent from the committed TSV

Recreate the complete 50-region isec + RTG study from a clean clone

🟡

External resources and manual orchestration remain necessary

Verify the exact historical software stack

❌

Core versions remain TBD in docs/software_versions.md

Run all committed tests successfully

❌

The structure test expects an absent reference_datasets/ directory

Use for diagnosis or treatment decisions

❌

Not clinically validated

<details>
<summary><strong>🧱 Open the known technical gaps</strong></summary>

<br />

No single portable Snakemake or Nextflow workflow orchestrates the complete benchmark.

Several development scripts still depend on local paths and historical working directories.

Exact tool versions, input URLs, download dates, and checksums are incomplete.

table_3_missed_variant_summary.tsv still contains a placeholder for the difficult-region count.

table_4_low_recall_regions.tsv contains placeholder rows.

table_5_bcftools_vs_rtg_discrepancy_regions.tsv contains only a header.

The tests verify repository structure/configuration, not biological correctness or end-to-end execution.

Read the reproducibility notes →

</details>

<a id="scientific-boundaries"></a>

⚠️ What this project proves—and does not prove

✅ Supported

❌ Not supported

Regional analytical validation

Whole-genome performance claims

Evaluation in selected HG001 chr22 high-confidence regions

Multi-sample clinical validation

Normalized isec and formal RTG comparison

Clinical sensitivity or specificity

Descriptive error analysis by variant class and context

Statistical enrichment without a genomic background

A research foundation for broader benchmarking

Pathogenicity, disease risk, diagnosis, or treatment advice

The repository name uses preventive genomics as a longer-term application context. The current implementation ends at small-variant analytical benchmarking and regional error analysis.

❓ Frequently asked questions

<details>
<summary><strong>Does 100% normalized precision mean the workflow is clinically accurate?</strong></summary>

<br />

No. It is a record-level result inside selected HG001 chromosome 22 high-confidence regions. RTG precision was 99.84% in the same regional scope. Neither value is a clinical specificity estimate.

</details>

<details>
<summary><strong>Why benchmark 5, 25, and 50 regions?</strong></summary>

<br />

The staged design tests whether an encouraging small-scope result remains stable as more variants and contexts are introduced. The scopes are nested evaluation stages, not biological replicates.

</details>

<details>
<summary><strong>Can the full study be recreated with one command?</strong></summary>

<br />

No. Core tables and Figures 1–3 can be regenerated, and FASTQ-to-VCF stages are modular. The complete 50-region benchmark still requires external datasets, RTG preparation, local paths, and manual orchestration.

</details>

<details>
<summary><strong>Why are large genomic resources not bundled?</strong></summary>

<br />

Reference genomes, truth resources, reads, and alignments are large and externally governed. The repository preserves code, compact outputs, and documentation while directing users to authoritative sources.

</details>

🛣️ Roadmap

Pin every software version and record all external input checksums.

Replace local path assumptions with configuration-driven execution.

Add a portable Snakemake or Nextflow workflow.

Commit explicit region definitions and compact region-level source outputs.

Replace placeholder Tables 3–5 and Figure 4 with generated evidence.

Repair tests and add fixture-based CI execution.

Compare additional small-variant callers.

Expand beyond selected chromosome 22 regions.

Validate additional GIAB samples and independent datasets.

Add stratified evaluation for difficult contexts and variant classes.

<a id="connect"></a>

👩‍💻 Connect with the researchers

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🧬 Ritika Rajendra Rawat</h3>
      <strong>Project Lead · Bioinformatics Research Assistant · Bioinformatics Lead</strong><br /><br />
      Study design · Workflow development · Benchmarking strategy · Analysis · Interpretation · Visualization · Documentation<br /><br />
      <a href="https://github.com/Rita1791"><strong>GitHub ↗</strong></a> ·
      <a href="https://in.linkedin.com/in/ritika-rawat-551107219"><strong>LinkedIn ↗</strong></a> ·
      <a href="mailto:ritika.rawat27@outlook.com?subject=Benchmark-Aware%20WGS%20Research%20Enquiry"><strong>Email ↗</strong></a>
    </td>
    <td width="50%" valign="top">
      <h3>🔬 Farheena Azim Faridi</h3>
      <strong>Contributor · Bioinformatics Research Intern · M.Sc. Bioinformatics</strong><br /><br />
      Workflow support · Benchmarking assistance · Testing · Refinement · Documentation<br /><br />
      <a href="CONTRIBUTORS.md"><strong>View verified contribution statement →</strong></a>
    </td>
  </tr>
</table>

<p align="center">
  <a href="mailto:ritika.rawat27@outlook.com?subject=Benchmark-Aware%20WGS%20Research%20Collaboration">
    <img src="https://img.shields.io/badge/CONNECT_WITH_THE_PROJECT_LEAD-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email the project lead" />
  </a>
  <a href="https://github.com/Rita1791/Benchmark-aware-WGS-preventive-genomics/issues/new">
    <img src="https://img.shields.io/badge/OPEN_A_RESEARCH_DISCUSSION-181717?style=for-the-badge&logo=github&logoColor=white" alt="Open a GitHub issue" />
  </a>
</p>

Developed within the research and computational environment of Nainsense Labs Private Limited. Detailed roles are recorded in CONTRIBUTORS.md.

📖 Citation & license

If this repository or its analysis contributes to your work, use GitHub's Cite this repository menu or the metadata in CITATION.cff:

Rawat, R. R. (2026). Benchmark-aware regional validation of a reproducible WGS variant-calling workflow using GIAB HG001 chr22 reference regions [Software].

Released under the MIT License.

<div align="center">

🧬 High accuracy is the beginning of the investigation—not the end.

<sub>Built to turn a benchmark score into a traceable evidence trail.</sub>

<br /><br />

<a href="#navigate">Back to the project navigator ↑</a> · <a href="#connect">Connect with the researchers</a> · <a href="https://github.com/Rita1791/Benchmark-aware-WGS-preventive-genomics">Star the repository ⭐</a>

</div>
