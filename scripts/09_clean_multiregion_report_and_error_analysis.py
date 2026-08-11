#!/usr/bin/env python3

from pathlib import Path
import csv


BASE = Path("results/benchmark_valid_multi_region_v2")

ISEC_DIR = BASE / "isec"
REGION_FILE = BASE / "regions" / "selected_chr22_regions.tsv"
REPORT_DIR = BASE / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

CLEAN_TSV = REPORT_DIR / "clean_multi_region_benchmark_summary.tsv"
CLEAN_MD = REPORT_DIR / "clean_multi_region_benchmark_report.md"
MISSED_TSV = REPORT_DIR / "missed_truth_variant_analysis.tsv"


def count_vcf_records(path: Path) -> int:
    count = 0

    with path.open() as handle:
        for line in handle:
            if not line.startswith("#"):
                count += 1

    return count


def classify_variant(ref: str, alt: str) -> str:

    if len(ref) == 1 and len(alt) == 1:
        return "SNV"

    if len(ref) > len(alt):
        return "Deletion"

    if len(ref) < len(alt):
        return "Insertion"

    return "Complex/Substitution"


def extract_info_value(info: str, key: str) -> str:

    prefix = f"{key}="

    for item in info.split(";"):

        if item.startswith(prefix):
            return item.split("=", 1)[1]

    return ""


# ------------------------------------------------------------
# Load selected regions
# ------------------------------------------------------------

with REGION_FILE.open() as handle:

    regions = list(
        csv.DictReader(handle, delimiter="\t")
    )


summary_rows = []
missed_rows = []

total_truth_only = 0
total_project_only = 0
total_shared = 0


# ------------------------------------------------------------
# Process each region
# ------------------------------------------------------------

for region_row in regions:

    region_id = region_row["region_id"]

    chrom = region_row["chrom"]
    start = region_row["start"]
    end = region_row["end"]

    region = f"{chrom}:{start}-{end}"

    region_isec = ISEC_DIR / region_id

    truth_only_file = region_isec / "0000.vcf"
    project_only_file = region_isec / "0001.vcf"
    shared_file = region_isec / "0002.vcf"

    truth_only = count_vcf_records(truth_only_file)
    project_only = count_vcf_records(project_only_file)
    shared = count_vcf_records(shared_file)

    truth_total = truth_only + shared
    project_total = project_only + shared

    recall = (
        shared / truth_total * 100
        if truth_total
        else 0
    )

    precision = (
        shared / project_total * 100
        if project_total
        else 0
    )

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0
    )

    total_truth_only += truth_only
    total_project_only += project_only
    total_shared += shared

    summary_rows.append(
        {
            "region_id": region_id,
            "region": region,
            "length_bp": region_row["length_bp"],
            "original_truth_count": region_row[
                "truth_variant_count"
            ],
            "normalized_truth_total": truth_total,
            "normalized_project_total": project_total,
            "truth_only_missed": truth_only,
            "project_only_extra": project_only,
            "shared": shared,
            "recall_pct": f"{recall:.2f}",
            "precision_pct": f"{precision:.2f}",
            "f1_pct": f"{f1:.2f}",
        }
    )

    # --------------------------------------------------------
    # Missed truth variants
    # --------------------------------------------------------

    with truth_only_file.open() as handle:

        for line in handle:

            if line.startswith("#"):
                continue

            fields = line.rstrip("\n").split("\t")

            if len(fields) < 8:
                continue

            chrom_v, pos, vid, ref, alt, qual, filt, info = (
                fields[:8]
            )

            missed_rows.append(
                {
                    "region_id": region_id,
                    "chrom": chrom_v,
                    "pos": pos,
                    "ref": ref,
                    "alt": alt,
                    "variant_type": classify_variant(ref, alt),
                    "qual": qual,
                    "filter": filt,
                    "difficultregion": extract_info_value(
                        info,
                        "difficultregion",
                    ),
                    "platforms": extract_info_value(
                        info,
                        "platformnames",
                    ),
                    "datasets": extract_info_value(
                        info,
                        "datasetnames",
                    ),
                }
            )


# ------------------------------------------------------------
# Write summary TSV
# ------------------------------------------------------------

summary_fields = [
    "region_id",
    "region",
    "length_bp",
    "original_truth_count",
    "normalized_truth_total",
    "normalized_project_total",
    "truth_only_missed",
    "project_only_extra",
    "shared",
    "recall_pct",
    "precision_pct",
    "f1_pct",
]

with CLEAN_TSV.open("w", newline="") as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=summary_fields,
        delimiter="\t",
    )

    writer.writeheader()
    writer.writerows(summary_rows)


# ------------------------------------------------------------
# Write missed-variant TSV
# ------------------------------------------------------------

missed_fields = [
    "region_id",
    "chrom",
    "pos",
    "ref",
    "alt",
    "variant_type",
    "qual",
    "filter",
    "difficultregion",
    "platforms",
    "datasets",
]

with MISSED_TSV.open("w", newline="") as handle:

    writer = csv.DictWriter(
        handle,
        fieldnames=missed_fields,
        delimiter="\t",
    )

    writer.writeheader()
    writer.writerows(missed_rows)


# ------------------------------------------------------------
# Aggregate metrics
# ------------------------------------------------------------

truth_total = total_truth_only + total_shared
project_total = total_project_only + total_shared

recall = (
    total_shared / truth_total * 100
    if truth_total
    else 0
)

precision = (
    total_shared / project_total * 100
    if project_total
    else 0
)

f1 = (
    2 * precision * recall / (precision + recall)
    if precision + recall
    else 0
)


# ------------------------------------------------------------
# Error categories
# ------------------------------------------------------------

type_counts = {}

difficult_count = 0

for row in missed_rows:

    variant_type = row["variant_type"]

    type_counts[variant_type] = (
        type_counts.get(variant_type, 0) + 1
    )

    if row["difficultregion"]:
        difficult_count += 1


# ------------------------------------------------------------
# Markdown report
# ------------------------------------------------------------

with CLEAN_MD.open("w") as handle:

    handle.write(
        "# Multi-Region GIAB HG001 chr22 Benchmark Report\n\n"
    )

    handle.write(
        "## Scope\n\n"
    )

    handle.write(
        f"The analysis covers {len(regions)} selected "
        "GIAB HG001 GRCh38 chromosome 22 benchmark regions. "
        "The result represents regional validation and should "
        "not be interpreted as a whole-genome benchmark.\n\n"
    )

    handle.write("## Method\n\n")

    handle.write(
        "Normalized truth and project VCFs were compared using "
        "bcftools isec. Shared records were treated as concordant "
        "variants, truth-only records as missed variants, and "
        "project-only records as additional project calls.\n\n"
    )

    handle.write("## Per-Region Results\n\n")

    handle.write(
        "| Region | Truth | Project | Missed | Extra | "
        "Shared | Recall | Precision | F1 |\n"
    )

    handle.write(
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|\n"
    )

    for row in summary_rows:

        handle.write(
            f"| {row['region_id']} "
            f"| {row['normalized_truth_total']} "
            f"| {row['normalized_project_total']} "
            f"| {row['truth_only_missed']} "
            f"| {row['project_only_extra']} "
            f"| {row['shared']} "
            f"| {row['recall_pct']}% "
            f"| {row['precision_pct']}% "
            f"| {row['f1_pct']}% |\n"
        )

    handle.write("\n## Aggregate Results\n\n")

    handle.write(
        f"- Selected regions: {len(regions)}\n"
    )

    handle.write(
        f"- Normalized truth variants: {truth_total}\n"
    )

    handle.write(
        f"- Project variants: {project_total}\n"
    )

    handle.write(
        f"- Shared variants: {total_shared}\n"
    )

    handle.write(
        f"- Truth-only missed variants: {total_truth_only}\n"
    )

    handle.write(
        f"- Project-only variants: {total_project_only}\n"
    )

    handle.write(
        f"- Recall: {recall:.2f}%\n"
    )

    handle.write(
        f"- Precision: {precision:.2f}%\n"
    )

    handle.write(
        f"- F1: {f1:.2f}%\n\n"
    )

    handle.write("## Missed Variant Types\n\n")

    for variant_type, count in sorted(
        type_counts.items()
    ):

        handle.write(
            f"- {variant_type}: {count}\n"
        )

    handle.write(
        f"\nMissed variants with difficult-region "
        f"annotation: {difficult_count}\n\n"
    )

    handle.write("## Interpretation\n\n")

    handle.write(
        "The regional benchmark provides an empirical assessment "
        "of concordance between the project callset and the GIAB "
        "HG001 truth set. Missed-variant composition is reported "
        "separately to distinguish overall sensitivity from the "
        "sequence-context characteristics of discordant calls.\n\n"
    )

    handle.write("## Limitation\n\n")

    handle.write(
        "The benchmark is restricted to selected chromosome 22 "
        "regions. The findings therefore support regional "
        "pipeline validation rather than a claim of whole-genome "
        "variant-calling performance.\n"
    )


print("Created:")
print(CLEAN_TSV)
print(CLEAN_MD)
print(MISSED_TSV)

print()
print(f"Regions: {len(regions)}")
print(f"Truth variants: {truth_total}")
print(f"Project variants: {project_total}")
print(f"Shared variants: {total_shared}")
print(f"Missed variants: {total_truth_only}")
print(f"Extra variants: {total_project_only}")
print(f"Recall: {recall:.2f}%")
print(f"Precision: {precision:.2f}%")
print(f"F1: {f1:.2f}%")
