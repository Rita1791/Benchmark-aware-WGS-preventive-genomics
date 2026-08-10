from pathlib import Path
import csv

BCFTOOLS_SUMMARY = Path("results/benchmark_valid_chr22_50_region/reports/clean_multi_region_benchmark_summary.tsv")
VCFEVAL_SUMMARY = Path("results/formal_vcfeval_chr22_50_region/reports/vcfeval_50_region_summary.tsv")

OUTDIR = Path("results/final_comparison")
OUTDIR.mkdir(parents=True, exist_ok=True)

out_tsv = OUTDIR / "bcftools_vs_vcfeval_50_region_discrepancy.tsv"
out_md = OUTDIR / "bcftools_vs_vcfeval_50_region_discrepancy.md"

bcf = {}
with open(BCFTOOLS_SUMMARY) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        bcf[row["region_id"]] = row

vcf = {}
with open(VCFEVAL_SUMMARY) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        vcf[row["region_id"]] = row

rows = []

for region_id in sorted(bcf.keys(), key=lambda x: int(x.split("_")[1])):
    b = bcf[region_id]
    v = vcf[region_id]

    b_shared = int(b["shared"])
    b_truth_only = int(b["truth_only_missed"])
    b_project_only = int(b["project_only_extra"])

    v_tp = int(v["tp_baseline"])
    v_fn = int(v["fn"])
    v_fp = int(v["fp"])

    row = {
        "region_id": region_id,
        "bcftools_shared": b_shared,
        "vcfeval_tp": v_tp,
        "tp_difference": v_tp - b_shared,
        "bcftools_truth_only": b_truth_only,
        "vcfeval_fn": v_fn,
        "fn_difference": v_fn - b_truth_only,
        "bcftools_project_only": b_project_only,
        "vcfeval_fp": v_fp,
        "fp_difference": v_fp - b_project_only,
        "bcftools_recall_pct": b["recall_pct"],
        "bcftools_precision_pct": b["precision_pct"],
        "vcfeval_sensitivity_pct": f"{float(v['sensitivity']) * 100:.2f}",
        "vcfeval_precision_pct": f"{float(v['precision']) * 100:.2f}",
    }
    rows.append(row)

with open(out_tsv, "w", newline="") as f:
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)

diff_rows = [
    r for r in rows
    if r["tp_difference"] != 0 or r["fn_difference"] != 0 or r["fp_difference"] != 0
]

fp_rows = [r for r in rows if r["vcfeval_fp"] > 0]

with open(out_md, "w") as f:
    f.write("# bcftools isec vs RTG vcfeval Discrepancy Report — 50 chr22 Regions\n\n")

    f.write("## Goal\n")
    f.write("To identify region-level differences between normalized bcftools isec comparison and formal RTG vcfeval benchmarking.\n\n")

    f.write("## Aggregate Difference\n\n")
    f.write("bcftools isec aggregate result:\n")
    f.write("- Shared variants: 2469\n")
    f.write("- Project-only extra variants: 0\n")
    f.write("- Truth-only missed variants: 123\n")
    f.write("- Recall: 95.25%\n")
    f.write("- Precision: 100.00%\n")
    f.write("- F1: 97.57%\n\n")

    f.write("RTG vcfeval aggregate result:\n")
    f.write("- True positives: 2465\n")
    f.write("- False positives: 4\n")
    f.write("- False negatives: 127\n")
    f.write("- Sensitivity: 95.10%\n")
    f.write("- Precision: 99.84%\n")
    f.write("- F-measure: 97.41%\n\n")

    f.write("## Regions with Any Difference\n\n")
    f.write("| Region | bcftools Shared | vcfeval TP | TP Diff | bcftools FN | vcfeval FN | FN Diff | bcftools FP | vcfeval FP | FP Diff |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in diff_rows:
        f.write(
            f"| {r['region_id']} | {r['bcftools_shared']} | {r['vcfeval_tp']} | {r['tp_difference']} | "
            f"{r['bcftools_truth_only']} | {r['vcfeval_fn']} | {r['fn_difference']} | "
            f"{r['bcftools_project_only']} | {r['vcfeval_fp']} | {r['fp_difference']} |\n"
        )

    f.write("\n## Regions with RTG vcfeval False Positives\n\n")
    if fp_rows:
        f.write("| Region | vcfeval FP | vcfeval Precision | bcftools Project-only |\n")
        f.write("|---|---:|---:|---:|\n")
        for r in fp_rows:
            f.write(
                f"| {r['region_id']} | {r['vcfeval_fp']} | {r['vcfeval_precision_pct']}% | {r['bcftools_project_only']} |\n"
            )
    else:
        f.write("No RTG vcfeval false-positive regions were detected.\n")

    f.write("\n\n## Scientific Interpretation\n")
    f.write(
        "RTG vcfeval produced a slightly stricter formal benchmark than bcftools isec. "
        "The total difference was small: 4 fewer true positives, 4 additional false negatives, and 4 false positives. "
        "This reduced precision from 100.00% to 99.84% and F-measure from 97.57% to 97.41%. "
        "The agreement remains strong, but RTG vcfeval should be reported as the more formal benchmark result.\n"
    )

print("Created:")
print(out_tsv)
print(out_md)

print()
print("Regions with differences:")
for r in diff_rows:
    print(
        f"{r['region_id']}: TPdiff={r['tp_difference']}, "
        f"FNdiff={r['fn_difference']}, FPdiff={r['fp_difference']}"
    )

print()
print("Regions with vcfeval false positives:")
for r in fp_rows:
    print(f"{r['region_id']}: FP={r['vcfeval_fp']}, vcfeval_precision={r['vcfeval_precision_pct']}%")
