from pathlib import Path
import csv
from collections import Counter

OUT = Path("results/publication_ready/tables")
OUT.mkdir(parents=True, exist_ok=True)

# ---------- Table 1: benchmark scale comparison ----------
scale_rows = [
    ["5-region chr22", 444, 428, 428, 16, 0, "96.40%", "100.00%", "98.17%"],
    ["25-region chr22", 1504, 1421, 1421, 83, 0, "94.48%", "100.00%", "97.16%"],
    ["50-region chr22", 2592, 2469, 2469, 123, 0, "95.25%", "100.00%", "97.57%"],
]

with open(OUT / "table_1_benchmark_scale_comparison.tsv", "w") as f:
    f.write("Benchmark\tTruth variants\tProject variants\tShared\tMissed truth\tExtra project\tRecall\tPrecision\tF1\n")
    for r in scale_rows:
        f.write("\t".join(map(str, r)) + "\n")

with open(OUT / "table_1_benchmark_scale_comparison.md", "w") as f:
    f.write("# Table 1. Benchmark Scale Comparison\n\n")
    f.write("| Benchmark | Truth variants | Project variants | Shared | Missed truth | Extra project | Recall | Precision | F1 |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in scale_rows:
        f.write(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {r[8]} |\n")

# ---------- Table 2: formal RTG vcfeval result ----------
vcfeval_rows = [
    ["RTG vcfeval 50-region chr22", 2465, 2465, 4, 127, "99.84%", "95.10%", "97.41%"]
]

with open(OUT / "table_2_formal_rtg_vcfeval_result.tsv", "w") as f:
    f.write("Benchmark\tTP baseline\tTP call\tFalse positives\tFalse negatives\tPrecision\tSensitivity\tF-measure\n")
    for r in vcfeval_rows:
        f.write("\t".join(map(str, r)) + "\n")

with open(OUT / "table_2_formal_rtg_vcfeval_result.md", "w") as f:
    f.write("# Table 2. Formal RTG vcfeval Benchmark Result\n\n")
    f.write("| Benchmark | TP baseline | TP call | False positives | False negatives | Precision | Sensitivity | F-measure |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in vcfeval_rows:
        f.write(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |\n")

# ---------- Table 3: missed variant summary ----------
missed_file = Path("results/benchmark_valid_chr22_50_region/reports/missed_truth_variant_analysis.tsv")
type_counts = Counter()
difficult_count = 0
total_missed = 0

with open(missed_file) as f:
    reader = csv.reader(f, delimiter="\t")
    header = next(reader)
    for row in reader:
        if not row:
            continue
        total_missed += 1
        # field 6 from earlier analysis = variant type
        if len(row) > 5:
            type_counts[row[5]] += 1
        # field 9 from earlier analysis = difficult annotation
        if len(row) > 8 and row[8].strip():
            difficult_count += 1

with open(OUT / "table_3_missed_variant_summary.tsv", "w") as f:
    f.write("Category\tCount\n")
    f.write(f"Total missed variants\t{total_missed}\n")
    for k, v in sorted(type_counts.items()):
        f.write(f"{k}\t{v}\n")
    f.write(f"Difficult-region missed variants\t{difficult_count}\n")

with open(OUT / "table_3_missed_variant_summary.md", "w") as f:
    f.write("# Table 3. Missed Variant Summary\n\n")
    f.write("| Category | Count |\n")
    f.write("|---|---:|\n")
    f.write(f"| Total missed variants | {total_missed} |\n")
    for k, v in sorted(type_counts.items()):
        f.write(f"| {k} | {v} |\n")
    f.write(f"| Difficult-region missed variants | {difficult_count} |\n")

# ---------- Table 4: low-recall regions ----------
low_file = Path("results/benchmark_valid_chr22_50_region/reports/low_recall_region_summary.tsv")
low_rows = []
with open(low_file) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        low_rows.append(row)

with open(OUT / "table_4_low_recall_regions.tsv", "w") as f:
    f.write("Region\tCoordinates\tTruth total\tProject total\tMissed\tShared\tRecall\tPrecision\tF1\n")
    for r in low_rows:
        f.write(
            f"{r['region_id']}\t{r['region']}\t{r['normalized_truth_total']}\t"
            f"{r['normalized_project_total']}\t{r['truth_only_missed']}\t{r['shared']}\t"
            f"{r['recall_pct']}%\t{r['precision_pct']}%\t{r['f1_pct']}%\n"
        )

with open(OUT / "table_4_low_recall_regions.md", "w") as f:
    f.write("# Table 4. Low-Recall Regions\n\n")
    f.write("| Region | Coordinates | Truth total | Project total | Missed | Shared | Recall | Precision | F1 |\n")
    f.write("|---|---|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in low_rows:
        f.write(
            f"| {r['region_id']} | {r['region']} | {r['normalized_truth_total']} | "
            f"{r['normalized_project_total']} | {r['truth_only_missed']} | {r['shared']} | "
            f"{r['recall_pct']}% | {r['precision_pct']}% | {r['f1_pct']}% |\n"
        )

# ---------- Table 5: discrepancy regions ----------
disc_file = Path("results/final_comparison/bcftools_vs_vcfeval_50_region_discrepancy.tsv")
disc_rows = []
with open(disc_file) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        if int(row["fp_difference"]) != 0 or int(row["fn_difference"]) != 0 or int(row["tp_difference"]) != 0:
            disc_rows.append(row)

with open(OUT / "table_5_bcftools_vs_rtg_discrepancy_regions.tsv", "w") as f:
    f.write("Region\tbcftools shared\tRTG TP\tTP diff\tbcftools FN\tRTG FN\tFN diff\tbcftools FP\tRTG FP\tFP diff\n")
    for r in disc_rows:
        f.write(
            f"{r['region_id']}\t{r['bcftools_shared']}\t{r['vcfeval_tp']}\t{r['tp_difference']}\t"
            f"{r['bcftools_truth_only']}\t{r['vcfeval_fn']}\t{r['fn_difference']}\t"
            f"{r['bcftools_project_only']}\t{r['vcfeval_fp']}\t{r['fp_difference']}\n"
        )

with open(OUT / "table_5_bcftools_vs_rtg_discrepancy_regions.md", "w") as f:
    f.write("# Table 5. bcftools isec vs RTG vcfeval Discrepancy Regions\n\n")
    f.write("| Region | bcftools shared | RTG TP | TP diff | bcftools FN | RTG FN | FN diff | bcftools FP | RTG FP | FP diff |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in disc_rows:
        f.write(
            f"| {r['region_id']} | {r['bcftools_shared']} | {r['vcfeval_tp']} | {r['tp_difference']} | "
            f"{r['bcftools_truth_only']} | {r['vcfeval_fn']} | {r['fn_difference']} | "
            f"{r['bcftools_project_only']} | {r['vcfeval_fp']} | {r['fp_difference']} |\n"
        )

print("Publication-ready tables created in:", OUT)
for path in sorted(OUT.glob("table_*")):
    print(path)
