#!/usr/bin/env python3

"""
Compare normalized bcftools isec results with formal RTG vcfeval
results across the 50 chromosome 22 benchmark regions.

Inputs:
    results/benchmark_valid_chr22_50_region/reports/
        clean_multi_region_benchmark_summary.tsv

    results/formal_vcfeval_chr22_50_region/reports/
        vcfeval_50_region_summary.tsv

Outputs:
    results/final_comparison/
        bcftools_vs_vcfeval_50_region_discrepancy.tsv
        bcftools_vs_vcfeval_50_region_discrepancy.md

    results/discrepancy_regions.csv
"""

from pathlib import Path
import csv


BCFTOOLS_SUMMARY = Path(
    "results/benchmark_valid_chr22_50_region/"
    "reports/clean_multi_region_benchmark_summary.tsv"
)

VCFEVAL_SUMMARY = Path(
    "results/formal_vcfeval_chr22_50_region/"
    "reports/vcfeval_50_region_summary.tsv"
)

OUT_DIR = Path("results/final_comparison")
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_TSV = (
    OUT_DIR
    / "bcftools_vs_vcfeval_50_region_discrepancy.tsv"
)

OUT_MD = (
    OUT_DIR
    / "bcftools_vs_vcfeval_50_region_discrepancy.md"
)

COMPACT_CSV = Path(
    "results/discrepancy_regions.csv"
)


# ------------------------------------------------------------
# Read TSV
# ------------------------------------------------------------

def read_tsv(path):

    if not path.exists():
        raise FileNotFoundError(
            f"Input file not found: {path}"
        )

    with path.open(
        "r",
        newline="",
        encoding="utf-8",
    ) as handle:

        return list(
            csv.DictReader(
                handle,
                delimiter="\t",
            )
        )


bcftools_rows = read_tsv(
    BCFTOOLS_SUMMARY
)

vcfeval_rows = read_tsv(
    VCFEVAL_SUMMARY
)


# ------------------------------------------------------------
# Index by region
# ------------------------------------------------------------

bcftools = {
    row["region_id"]: row
    for row in bcftools_rows
}

vcfeval = {
    row["region_id"]: row
    for row in vcfeval_rows
}


common_regions = sorted(
    set(bcftools)
    & set(vcfeval),
    key=lambda value: int(
        value.split("_")[1]
    ),
)


if len(common_regions) != 50:
    raise ValueError(
        f"Expected 50 common regions, found "
        f"{len(common_regions)}."
    )


# ------------------------------------------------------------
# Compare regions
# ------------------------------------------------------------

rows = []

for region_id in common_regions:

    b = bcftools[region_id]
    v = vcfeval[region_id]

    bcftools_shared = int(
        b["shared"]
    )

    bcftools_truth_only = int(
        b["truth_only_missed"]
    )

    bcftools_project_only = int(
        b["project_only_extra"]
    )

    rtg_tp = int(
        v["tp_baseline"]
    )

    rtg_fn = int(
        v["fn"]
    )

    rtg_fp = int(
        v["fp"]
    )

    row = {
        "region_id": region_id,

        "bcftools_shared": bcftools_shared,
        "rtg_tp": rtg_tp,
        "tp_difference": rtg_tp - bcftools_shared,

        "bcftools_fn": bcftools_truth_only,
        "rtg_fn": rtg_fn,
        "fn_difference": rtg_fn - bcftools_truth_only,

        "bcftools_fp": bcftools_project_only,
        "rtg_fp": rtg_fp,
        "fp_difference": rtg_fp - bcftools_project_only,

        "bcftools_recall_percent": b[
            "recall_pct"
        ],

        "bcftools_precision_percent": b[
            "precision_pct"
        ],

        "rtg_sensitivity_percent": (
            float(v["sensitivity"]) * 100
        ),

        "rtg_precision_percent": (
            float(v["precision"]) * 100
        ),
    }

    rows.append(row)


# ------------------------------------------------------------
# Identify discrepancy regions
# ------------------------------------------------------------

difference_rows = [
    row
    for row in rows
    if (
        row["tp_difference"] != 0
        or row["fn_difference"] != 0
        or row["fp_difference"] != 0
    )
]


# ------------------------------------------------------------
# Write detailed TSV
# ------------------------------------------------------------

fieldnames = [
    "region_id",
    "bcftools_shared",
    "rtg_tp",
    "tp_difference",
    "bcftools_fn",
    "rtg_fn",
    "fn_difference",
    "bcftools_fp",
    "rtg_fp",
    "fp_difference",
    "bcftools_recall_percent",
    "bcftools_precision_percent",
    "rtg_sensitivity_percent",
    "rtg_precision_percent",
]


with OUT_TSV.open(
    "w",
    newline="",
    encoding="utf-8",
) as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=fieldnames,
        delimiter="\t",
    )

    writer.writeheader()

    for row in rows:

        writer.writerow(
            {
                key: row[key]
                for key in fieldnames
            }
        )


# ------------------------------------------------------------
# Write compact discrepancy CSV
# ------------------------------------------------------------

compact_fields = [
    "region_id",
    "bcftools_shared",
    "rtg_tp",
    "tp_difference",
    "bcftools_fn",
    "rtg_fn",
    "fn_difference",
    "bcftools_fp",
    "rtg_fp",
    "fp_difference",
]


with COMPACT_CSV.open(
    "w",
    newline="",
    encoding="utf-8",
) as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=compact_fields,
    )

    writer.writeheader()

    for row in difference_rows:

        writer.writerow(
            {
                key: row[key]
                for key in compact_fields
            }
        )


# ------------------------------------------------------------
# Aggregate metrics directly from region counts
# ------------------------------------------------------------

bcftools_shared_total = sum(
    row["bcftools_shared"]
    for row in rows
)

bcftools_fn_total = sum(
    row["bcftools_fn"]
    for row in rows
)

bcftools_fp_total = sum(
    row["bcftools_fp"]
    for row in rows
)

rtg_tp_total = sum(
    row["rtg_tp"]
    for row in rows
)

rtg_fn_total = sum(
    row["rtg_fn"]
    for row in rows
)

rtg_fp_total = sum(
    row["rtg_fp"]
    for row in rows
)


# ------------------------------------------------------------
# Markdown report
# ------------------------------------------------------------

with OUT_MD.open(
    "w",
    encoding="utf-8",
) as handle:

    handle.write(
        "# bcftools isec vs RTG vcfeval Discrepancy Report — 50 chr22 Regions\n\n"
    )

    handle.write("## Goal\n\n")

    handle.write(
        "To identify region-level differences between normalized "
        "`bcftools isec` comparison and formal RTG `vcfeval` "
        "benchmarking across the 50 evaluated chromosome 22 regions.\n\n"
    )

    handle.write("## Aggregate comparison\n\n")

    handle.write(
        "| Metric | bcftools isec | RTG vcfeval |\n"
    )

    handle.write(
        "|---|---:|---:|\n"
    )

    handle.write(
        f"| True/shared positives | "
        f"{bcftools_shared_total} | {rtg_tp_total} |\n"
    )

    handle.write(
        f"| False negatives | "
        f"{bcftools_fn_total} | {rtg_fn_total} |\n"
    )

    handle.write(
        f"| False positives | "
        f"{bcftools_fp_total} | {rtg_fp_total} |\n\n"
    )

    handle.write("## Regions with differences\n\n")

    handle.write(
        "| Region | bcftools Shared | RTG TP | TP Diff | "
        "bcftools FN | RTG FN | FN Diff | "
        "bcftools FP | RTG FP | FP Diff |\n"
    )

    handle.write(
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n"
    )

    for row in difference_rows:

        handle.write(
            f"| {row['region_id']} "
            f"| {row['bcftools_shared']} "
            f"| {row['rtg_tp']} "
            f"| {row['tp_difference']} "
            f"| {row['bcftools_fn']} "
            f"| {row['rtg_fn']} "
            f"| {row['fn_difference']} "
            f"| {row['bcftools_fp']} "
            f"| {row['rtg_fp']} "
            f"| {row['fp_difference']} |\n"
        )

    if not difference_rows:

        handle.write(
            "\nNo region-level discrepancies were detected.\n"
        )

    handle.write("\n## Interpretation\n\n")

    handle.write(
        "The normalized and formal benchmark results are compared "
        "at the region level. Differences are reported explicitly "
        "rather than being hidden through aggregate averaging.\n\n"
    )

    handle.write(
        f"{len(difference_rows)} of the 50 evaluated regions "
        "contained at least one difference between the two methods.\n"
    )


# ------------------------------------------------------------
# Completion
# ------------------------------------------------------------

print("Created:")
print(OUT_TSV)
print(OUT_MD)
print(COMPACT_CSV)

print()
print(
    f"Regions with discrepancies: "
    f"{len(difference_rows)} / 50"
)

for row in difference_rows:

    print(
        f"{row['region_id']}: "
        f"TP diff={row['tp_difference']}, "
        f"FN diff={row['fn_difference']}, "
        f"FP diff={row['fp_difference']}"
    )
