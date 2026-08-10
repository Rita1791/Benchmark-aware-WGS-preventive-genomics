#!/usr/bin/env bash
set -euo pipefail

# =========================================================
# Nainfit WGS/NGS Research Pipeline
# Step 04: Controlled FASTQ Subsampling
#
# Purpose:
# Create a 1-million-read-pair subset from trimmed paired-end FASTQ files.
#
# Why:
# This creates a smaller paired-end dataset for controlled testing of
# alignment and variant calling under limited compute resources.
# =========================================================

SAMPLE="SRR4420293"

R1_IN="data/real_trimmed_fastq/SRR4420293_1.trimmed.fastq.gz"
R2_IN="data/real_trimmed_fastq/SRR4420293_2.trimmed.fastq.gz"

OUTDIR="data/subsampled_fastq"
REPORTDIR="reports/subsampling"

R1_OUT="${OUTDIR}/SRR4420293_1.subsample_1M.fastq.gz"
R2_OUT="${OUTDIR}/SRR4420293_2.subsample_1M.fastq.gz"

READS=1000000

mkdir -p "${OUTDIR}" "${REPORTDIR}"

echo "[INFO] Starting controlled paired-end FASTQ subsampling"
echo "[INFO] Sample: ${SAMPLE}"
echo "[INFO] Number of read pairs: ${READS}"
echo "[INFO] R1 input: ${R1_IN}"
echo "[INFO] R2 input: ${R2_IN}"

if [[ ! -f "${R1_IN}" ]]; then
  echo "[ERROR] R1 input file not found: ${R1_IN}"
  exit 1
fi

if [[ ! -f "${R2_IN}" ]]; then
  echo "[ERROR] R2 input file not found: ${R2_IN}"
  exit 1
fi

python3 - <<EOF
import gzip

r1_in = "${R1_IN}"
r2_in = "${R2_IN}"
r1_out = "${R1_OUT}"
r2_out = "${R2_OUT}"
reads = ${READS}

def copy_fastq_records(input_path, output_path, n_reads):
    written = 0
    with gzip.open(input_path, "rt") as fin, gzip.open(output_path, "wt") as fout:
        for _ in range(n_reads):
            record = [fin.readline() for _ in range(4)]
            if not record[0]:
                break
            if any(line == "" for line in record):
                raise ValueError(f"Incomplete FASTQ record found in {input_path}")
            fout.writelines(record)
            written += 1
    return written

r1_written = copy_fastq_records(r1_in, r1_out, reads)
r2_written = copy_fastq_records(r2_in, r2_out, reads)

if r1_written != reads:
    raise RuntimeError(f"R1 wrote {r1_written} reads, expected {reads}")

if r2_written != reads:
    raise RuntimeError(f"R2 wrote {r2_written} reads, expected {reads}")

if r1_written != r2_written:
    raise RuntimeError("R1 and R2 read counts do not match")

print(f"[PYTHON] R1 reads written: {r1_written}")
print(f"[PYTHON] R2 reads written: {r2_written}")
EOF

echo "[INFO] Counting output lines..."

R1_LINES=$(zcat "${R1_OUT}" | wc -l)
R2_LINES=$(zcat "${R2_OUT}" | wc -l)

EXPECTED_LINES=$((READS * 4))

echo "[INFO] Expected lines per FASTQ: ${EXPECTED_LINES}"
echo "[INFO] R1 output lines: ${R1_LINES}"
echo "[INFO] R2 output lines: ${R2_LINES}"

if [[ "${R1_LINES}" -ne "${EXPECTED_LINES}" ]]; then
  echo "[ERROR] R1 line count mismatch"
  exit 1
fi

if [[ "${R2_LINES}" -ne "${EXPECTED_LINES}" ]]; then
  echo "[ERROR] R2 line count mismatch"
  exit 1
fi

cat > "${REPORTDIR}/subsample_1M_summary.md" <<REPORT
# Subsampled FASTQ Summary

## Project
Nainfit WGS/NGS Research Pipeline

## Purpose
A 1-million-read-pair subset was created from trimmed paired-end FASTQ files to enable controlled downstream alignment and variant-calling tests under limited local compute resources.

## Input Files
- ${R1_IN}
- ${R2_IN}

## Output Files
- ${R1_OUT}
- ${R2_OUT}

## Method
A Python gzip-based streaming script copied the first ${READS} complete FASTQ records from both R1 and R2. Each FASTQ record contains 4 lines.

## Validation
- Expected lines per file: ${EXPECTED_LINES}
- R1 output lines: ${R1_LINES}
- R2 output lines: ${R2_LINES}
- R1 and R2 read-pair counts match.

## Scientific Reasoning
Subsampling allows controlled testing of pipeline modules before scaling to larger WGS datasets. It reduces computational burden, improves debugging, and preserves paired-end synchronization.

## Limitation
This is a deterministic first-N-read subset, not a random subsample. For formal benchmarking, random subsampling with seqtk or equivalent tools should be used later.

## Next Step
Use the 1M read-pair subset for full-reference alignment testing.
REPORT

echo "[DONE] FASTQ subsampling completed successfully."
echo "[OUTPUT] ${R1_OUT}"
echo "[OUTPUT] ${R2_OUT}"
echo "[REPORT] ${REPORTDIR}/subsample_1M_summary.md"
