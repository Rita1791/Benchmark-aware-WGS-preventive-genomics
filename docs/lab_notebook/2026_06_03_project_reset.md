# Daily Research Log — 2026-06-03

## Research Goal for Today
To formally reset the WGS/NGS work as an international-level, Swiss PhD-oriented computational genomics research project.

## Step Performed
Created a structured documentation system for tracking methodology, daily progress, PhD positioning, and pipeline development.

## Why This Step Was Needed Scientifically
A computational genomics project requires reproducible documentation. Without proper records, tool versions, command history, outputs, and scientific interpretation, the work cannot be audited, repeated, or converted into a manuscript or PhD proposal.

## Why This Step Matters for Swiss PhD-Level Research
Swiss PhD supervisors evaluate scientific maturity, methodological clarity, reproducibility, and the ability to communicate research rigorously. A professional lab notebook and methodology tracker demonstrate that this project is being developed as a research framework, not as casual command-line practice.

## Commands Run
Created directories:

- docs/research_tracking
- docs/methodology
- docs/phd_positioning
- docs/lab_notebook
- reports/final_summaries

Created documents:

- MASTER_RESEARCH_LOG.md
- WGS_NGS_PIPELINE_METHODOLOGY.md
- SWISS_PHD_RESEARCH_POSITIONING.md
- 2026_06_03_project_reset.md

## Output Files Generated
- docs/research_tracking/MASTER_RESEARCH_LOG.md
- docs/methodology/WGS_NGS_PIPELINE_METHODOLOGY.md
- docs/phd_positioning/SWISS_PHD_RESEARCH_POSITIONING.md
- docs/lab_notebook/2026_06_03_project_reset.md

## Key Result
The project now has a formal research tracking structure.

## Interpretation
This step establishes the documentation backbone required for reproducible computational genomics research.

## Error / Problem Faced
The first attempt using heredoc caused the terminal to enter continuation mode. This was resolved by using nano to create the file safely.

## Solution Applied
Used manual file creation through nano to avoid incomplete heredoc input.

## Limitation
Technical WGS/NGS analysis was not performed in this step. This was a project organization and documentation step.

## Next Step
Proceed with controlled subsampling of trimmed FASTQ files and document the process as part of staged pipeline development.

## Reflection
A strong WGS/NGS project is not built only by running tools. It is built by making every step reproducible, explainable, and scientifically justified.

---

# Additional Work: Controlled FASTQ Subsampling

## Step Performed
Created a validated 1-million-read-pair subsample from trimmed paired-end FASTQ files.

## Why This Step Was Needed Scientifically
The local compute environment has limited RAM, so full-scale WGS processing may fail if attempted immediately. Subsampling enables controlled testing of downstream alignment and variant-calling modules before scaling to larger datasets.

## Why This Matters for Swiss PhD-Level Research
This demonstrates staged, resource-aware pipeline development. It shows that the workflow is being built with reproducibility, validation, and computational constraints in mind, rather than by running tools blindly.

## Commands / Script Used
- scripts/04_subsample_fastq_1M.sh

## Output Files Generated
- data/subsampled_fastq/SRR4420293_1.subsample_1M.fastq.gz
- data/subsampled_fastq/SRR4420293_2.subsample_1M.fastq.gz
- reports/subsampling/subsample_1M_summary.md

## Key Results
- R1 output lines: 4,000,000
- R2 output lines: 4,000,000
- R1 reads: 1,000,000
- R2 reads: 1,000,000
- Paired-end read counts match.

## Interpretation
The paired-end subsampling step succeeded. The output dataset is valid for downstream controlled alignment testing.

## Error / Problem Faced
The first subsampling attempt produced only 41 lines for R1 and no R2 file. This happened because the earlier shell pipeline was unsafe under strict pipe settings.

## Solution Applied
Replaced the unsafe shell-based extraction with a Python gzip-based streaming method that copies complete FASTQ records and validates R1/R2 counts.

## Limitation
This is a deterministic first-N-read subset, not a random subsample. For formal benchmarking, random subsampling using seqtk or equivalent tools should be used later.

## Next Step
Decide and prepare the full-reference alignment strategy for the 1M paired-end read subset.
