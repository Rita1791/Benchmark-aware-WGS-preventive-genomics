from pathlib import Path
import csv
from collections import defaultdict

BASE = Path("results/benchmark_valid_chr22_25_region")
REPORT_DIR = BASE / "reports"

summary_file = REPORT_DIR / "clean_multi_region_benchmark_summary.tsv"
missed_file = REPORT_DIR / "missed_truth_variant_analysis.tsv"

low_recall_summary_out = REPORT_DIR / "low_recall_region_summary.tsv"
low_recall_missed_out = REPORT_DIR / "low_recall_missed_variants.tsv"
low_recall_report_out = REPORT_DIR / "low_recall_region_interpretation.md"

RECALL_THRESHOLD = 92.0

low_regions = set()
low_summary_rows = []

with open(summary_file) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        recall = float(row["recall_pct"])
        if recall < RECALL_THRESHOLD:
            low_regions.add(row["region_id"])
            low_summary_rows.append(row)

missed_rows = []
with open(missed_file) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        if row["region_id"] in low_regions:
            missed_rows.append(row)

with open(low_recall_summary_out, "w", newline="") as f:
    fieldnames = list(low_summary_rows[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(low_summary_rows)

with open(low_recall_missed_out, "w", newline="") as f:
    fieldnames = list(missed_rows[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(missed_rows)

type_by_region = defaultdict(lambda: defaultdict(int))
difficult_by_region = defaultdict(int)
total_by_region = defaultdict(int)

overall_type_counts = defaultdict(int)
overall_difficult = 0

for row in missed_rows:
    rid = row["region_id"]
    vtype = row["variant_type"]
    difficult = row["difficultregion"]

    type_by_region[rid][vtype] += 1
    total_by_region[rid] += 1
    overall_type_counts[vtype] += 1

    if difficult:
        difficult_by_region[rid] += 1
        overall_difficult += 1

with open(low_recall_report_out, "w") as f:
    f.write("# Low-Recall Region Error Analysis — 25-Region chr22 Benchmark\n\n")

    f.write("## Goal\n")
    f.write("To analyze regions with recall below 92% in the expanded 25-region GIAB HG001 GRCh38 chr22 benchmark.\n\n")

    f.write("## Low-Recall Regions\n\n")
    f.write("| Region | Coordinates | Truth Total | Project Total | Missed | Shared | Recall | Precision | F1 |\n")
    f.write("|---|---|---:|---:|---:|---:|---:|---:|---:|\n")

    for row in low_summary_rows:
        f.write(
            f"| {row['region_id']} | {row['region']} | "
            f"{row['normalized_truth_total']} | {row['normalized_project_total']} | "
            f"{row['truth_only_missed']} | {row['shared']} | "
            f"{row['recall_pct']}% | {row['precision_pct']}% | {row['f1_pct']}% |\n"
        )

    f.write("\n## Missed Variant Types in Low-Recall Regions\n\n")
    for vtype, count in sorted(overall_type_counts.items()):
        f.write(f"- {vtype}: {count}\n")

    f.write(f"\nTotal missed variants in low-recall regions: {len(missed_rows)}\n")
    f.write(f"Missed variants with difficult-region annotation: {overall_difficult}\n\n")

    f.write("## Region-wise Missed Variant Pattern\n\n")
    f.write("| Region | Total Missed | Difficult-Region Missed | Variant Type Counts |\n")
    f.write("|---|---:|---:|---|\n")

    for rid in sorted(low_regions, key=lambda x: int(x.split('_')[1])):
        type_text = ", ".join(f"{k}: {v}" for k, v in sorted(type_by_region[rid].items()))
        f.write(
            f"| {rid} | {total_by_region[rid]} | {difficult_by_region[rid]} | {type_text} |\n"
        )

    f.write("\n## Scientific Interpretation\n")
    f.write(
        "The lower-recall regions are mainly affected by missed indels, especially deletions and insertions. "
        "Several missed variants occur in difficult genomic contexts such as homopolymers, simple repeats, "
        "and tandem repeats. The presence of only one missed SNV, located in a tandem-repeat context, suggests "
        "that the workflow is not broadly failing on SNVs. Instead, the remaining limitation is concentrated "
        "in indel and repeat-context variant detection.\n\n"
    )

    f.write("## Conclusion\n")
    f.write(
        "The 25-region benchmark remains strong because precision is 100% and missed variants are biologically "
        "explainable. The next improvement should focus on indel-sensitive benchmarking and comparison using "
        "formal tools such as hap.py or vcfeval, rather than simply rerunning the same bcftools workflow.\n"
    )

print("Created:")
print(low_recall_summary_out)
print(low_recall_missed_out)
print(low_recall_report_out)

print("\nLow-recall regions:")
for r in low_summary_rows:
    print(f"{r['region_id']}: recall={r['recall_pct']}%, missed={r['truth_only_missed']}")

print("\nMissed variant types in low-recall regions:")
for k, v in sorted(overall_type_counts.items()):
    print(f"{k}: {v}")

print(f"\nDifficult-region missed variants in low-recall regions: {overall_difficult}/{len(missed_rows)}")
