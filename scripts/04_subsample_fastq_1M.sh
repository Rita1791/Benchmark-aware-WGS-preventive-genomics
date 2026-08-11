#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Benchmark-aware WGS Preventive Genomics
# Step 04: Controlled FASTQ subsampling
#
# Creates a deterministic 1-million-read-pair subset.
# ============================================================

SAMPLE="SRR4420293"

R1_IN="data/real_trimmed_fastq/SRR4420293_1.trimmed.fastq.gz"
R2_IN="data/real_trimmed_fastq/SRR4420293_2.trimmed.fastq.gz"

OUTDIR="data/subsampled_fastq"
REPORTDIR="results/subsampling"

READS="${READS:-1000000}"

R1_OUT="${OUTDIR}/${SAMPLE}_1.subsample_1M.fastq.gz"
R2_OUT="${OUTDIR}/${SAMPLE}_2.subsample_1M.fastq.gz"

mkdir -p "${OUTDIR}" "${REPORTDIR}"

echo "============================================================"
echo "Controlled FASTQ subsampling"
echo "============================================================"
echo "[INFO] Sample: ${SAMPLE}"
echo "[INFO] Read pairs: ${READS}"

for file in "${R1_IN}" "${R2_IN}"; do
    if [[ ! -f "${file}" ]]; then
        echo "[ERROR] Input file not found: ${file}"
        exit 1
    fi
done

python3 - <<PY
import gzip

r1_in = "${R1_IN}"
r2_in = "${R2_IN}"

r1_out = "${R1_OUT}"
r2_out = "${R2_OUT}"

reads = ${READS}


def copy_records(input_path, output_path, n_reads):
    written = 0

    with gzip.open(input_path, "rt") as fin, \
         gzip.open(output_path, "wt") as fout:

        for _ in range(n_reads):

            record = [fin.readline() for _ in range(4)]

            if not record[0]:
                break

            if any(line == "" for line in record):
                raise RuntimeError(
                    f"Incomplete FASTQ record in {input_path}"
                )

            fout.writelines(record)
            written += 1

    return written


r1_written = copy_records(r1_in, r1_out, reads)
r2_written = copy_records(r2_in, r2_out, reads)

if r1_written != reads:
    raise RuntimeError(
        f"R1 contains only {r1_written} reads; "
        f"{reads} were requested."
    )

if r2_written != reads:
    raise RuntimeError(
        f"R2 contains only {r2_written} reads; "
        f"{reads} were requested."
    )

if r1_written != r2_written:
    raise RuntimeError(
        "R1 and R2 read counts are not synchronized."
    )

print(f"R1 reads written: {r1_written}")
print(f"R2 reads written: {r2_written}")
PY

EXPECTED_LINES=$((READS * 4))

R1_LINES=$(zcat "${R1_OUT}" | wc -l)
R2_LINES=$(zcat "${R2_OUT}" | wc -l)

if [[ "${R1_LINES}" -ne "${EXPECTED_LINES}" ]]; then
    echo "[ERROR] R1 FASTQ line count mismatch."
    exit 1
fi

if [[ "${R2_LINES}" -ne "${EXPECTED_LINES}" ]]; then
    echo "[ERROR] R2 FASTQ line count mismatch."
    exit 1
fi

cat > "${REPORTDIR}/subsample_1M_summary.md" <<EOF
# 1M Paired-End FASTQ Subsample

## Dataset

Sample: ${SAMPLE}

## Input

- ${R1_IN}
- ${R2_IN}

## Output

- ${R1_OUT}
- ${R2_OUT}

## Method

A deterministic first-N-record extraction was performed using
Python gzip streaming.

Requested read pairs: ${READS}

## Validation

Expected FASTQ lines per file: ${EXPECTED_LINES}

R1 lines: ${R1_LINES}

R2 lines: ${R2_LINES}

R1 and R2 read counts were verified to be equal.

## Limitation

This is a deterministic first-N-read subset rather than a
randomized subsample. It is intended for computationally
controlled pipeline testing and not for estimating population-level
sampling properties.

## Next Step

The resulting paired-end subset can be used for controlled
alignment and variant-calling experiments.
EOF

echo "[DONE] FASTQ subsampling completed."
echo "[OUTPUT] ${R1_OUT}"
echo "[OUTPUT] ${R2_OUT}"
echo "[REPORT] ${REPORTDIR}/subsample_1M_summary.md"
