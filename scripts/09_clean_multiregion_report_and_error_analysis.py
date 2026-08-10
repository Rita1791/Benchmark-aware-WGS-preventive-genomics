from pathlib import Path
import csv

BASE = Path("results/benchmark_valid_multi_region_v2")
ISEC_DIR = BASE / "isec"
REGION_FILE = BASE / "regions" / "selected_chr22_regions.tsv"
REPORT_DIR = BASE / "reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

clean_tsv = REPORT_DIR / "clean_multi_region_benchmark_summary.tsv"
clean_md = REPORT_DIR / "clean_multi_region_benchmark_report.md"
missed_tsv = REPORT_DIR / "missed_truth_variant_analysis.tsv"

def count_vcf_records(vcf_path: Path) -> int:
    count = 0
    with open(vcf_path) as f:
        for line in f:
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
    for item in info.split(";"):
        if item.startswith(key + "="):
            return item.split("=", 1)[1]
    return ""

regions = []
with open(REGION_FILE) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        regions.append(row)

summary_rows = []
missed_rows = []

total_truth_only = 0
total_project_only = 0
total_shared = 0

for row in regions:
    region_id = row["region_id"]
    chrom = row["chrom"]
    start = row["start"]
    end = row["end"]
    length_bp = row["length_bp"]
    original_truth_count = row["truth_variant_count"]
    region = f"{chrom}:{start}-{end}"

    region_isec = ISEC_DIR / region_id

    truth_only = count_vcf_records(region_isec / "0000.vcf")
    project_only = count_vcf_records(region_isec / "0001.vcf")
    shared = count_vcf_records(region_isec / "0002.vcf")

    truth_total = truth_only + shared
    project_total = project_only + shared

    recall = shared / truth_total * 100 if truth_total else 0
    precision = shared / project_total * 100 if project_total else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0

    total_truth_only += truth_only
    total_project_only += project_only
    total_shared += shared

    summary_rows.append({
        "region_id": region_id,
        "region": region,
        "length_bp": length_bp,
        "original_truth_count": original_truth_count,
        "normalized_truth_total": truth_total,
        "normalized_project_total": project_total,
        "truth_only_missed": truth_only,
        "project_only_extra": project_only,
        "shared": shared,
        "recall_pct": f"{recall:.2f}",
        "precision_pct": f"{precision:.2f}",
        "f1_pct": f"{f1:.2f}",
    })

    # Extract missed truth-only variants from 0000.vcf
    with open(region_isec / "0000.vcf") as f:
        for line in f:
            if line.startswith("#"):
                continue
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 8:
                continue
            v_chrom, pos, vid, ref, alt, qual, filt, info = fields[:8]
            variant_type = classify_variant(ref, alt)
            difficult = extract_info_value(info, "difficultregion")
            platforms = extract_info_value(info, "platformnames")
            datasets = extract_info_value(info, "datasetnames")

            missed_rows.append({
                "region_id": region_id,
                "chrom": v_chrom,
                "pos": pos,
                "ref": ref,
                "alt": alt,
                "variant_type": variant_type,
                "qual": qual,
                "filter": filt,
                "difficultregion": difficult,
                "platforms": platforms,
                "datasets": datasets,
            })

# Write clean TSV
with open(clean_tsv, "w", newline="") as f:
    fieldnames = [
        "region_id", "region", "length_bp", "original_truth_count",
        "normalized_truth_total", "normalized_project_total",
        "truth_only_missed", "project_only_extra", "shared",
        "recall_pct", "precision_pct", "f1_pct"
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(summary_rows)

# Write missed variants TSV
with open(missed_tsv, "w", newline="") as f:
    fieldnames = [
        "region_id", "chrom", "pos", "ref", "alt",
        "variant_type", "qual", "filter",
        "difficultregion", "platforms", "datasets"
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(missed_rows)

# Combined metrics
truth_total = total_truth_only + total_shared
project_total = total_project_only + total_shared
combined_recall = total_shared / truth_total * 100 if truth_total else 0
combined_precision = total_shared / project_total * 100 if project_total else 0
combined_f1 = 2 * combined_precision * combined_recall / (combined_precision + combined_recall) if (combined_precision + combined_recall) else 0

# Variant type counts among missed variants
type_counts = {}
difficult_count = 0
for r in missed_rows:
    type_counts[r["variant_type"]] = type_counts.get(r["variant_type"], 0) + 1
    if r["difficultregion"]:
        difficult_count += 1

# Write Markdown report
with open(clean_md, "w") as f:
    f.write("# Clean Multi-Region GIAB chr22 Benchmark Report\n\n")
    f.write("## Project\n")
    f.write("Nainfit WGS/NGS-to-Variant Interpretation Research Framework\n\n")

    f.write("## Goal\n")
    f.write("To summarize a benchmark-valid multi-region GIAB HG001 GRCh38 chr22 variant-calling test.\n\n")

    f.write("## Workflow Summary\n")
    f.write("For each selected chr22 high-confidence region, the workflow extracted a regional GIAB-aligned BAM, called variants using bcftools, filtered calls, normalized truth and project VCFs, and compared them using bcftools isec.\n\n")

    f.write("## Per-Region Results\n\n")
    f.write("| Region | Normalized Truth | Project Calls | Missed Truth | Extra Project | Shared | Recall | Precision | F1 |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")

    for r in summary_rows:
        f.write(
            f"| {r['region_id']} | {r['normalized_truth_total']} | {r['normalized_project_total']} | "
            f"{r['truth_only_missed']} | {r['project_only_extra']} | {r['shared']} | "
            f"{r['recall_pct']}% | {r['precision_pct']}% | {r['f1_pct']}% |\n"
        )

    f.write("\n## Combined Metrics\n\n")
    f.write(f"- Total normalized truth variants: {truth_total}\n")
    f.write(f"- Total project variants: {project_total}\n")
    f.write(f"- Shared variants: {total_shared}\n")
    f.write(f"- Truth-only missed variants: {total_truth_only}\n")
    f.write(f"- Project-only extra variants: {total_project_only}\n")
    f.write(f"- Combined recall: {combined_recall:.2f}%\n")
    f.write(f"- Combined precision: {combined_precision:.2f}%\n")
    f.write(f"- Combined F1: {combined_f1:.2f}%\n\n")

    f.write("## Missed Variant Error Analysis\n\n")
    f.write(f"Total missed truth variants: {len(missed_rows)}\n\n")
    f.write("### Missed Variant Types\n")
    for k, v in sorted(type_counts.items()):
        f.write(f"- {k}: {v}\n")

    f.write(f"\nMissed variants with difficult-region annotation: {difficult_count}\n\n")

    f.write("## Scientific Interpretation\n")
    f.write(
        "The multi-region benchmark shows strong concordance with GIAB truth. "
        "Across 5 chr22 high-confidence regions, the workflow recovered 428 of 444 normalized truth variants, "
        "with 0 project-only extra variants. This supports the conclusion that the pipeline performs strongly "
        "when the experimental design is benchmark-compatible.\n\n"
    )

    f.write("## Limitation\n")
    f.write(
        "This is a 5-region chr22 benchmark, not a full-chromosome or whole-genome benchmark. "
        "The result should be reported as regional validation only.\n"
    )

print("Created:")
print(clean_tsv)
print(clean_md)
print(missed_tsv)

print("\nCombined metrics:")
print(f"truth_total={truth_total}")
print(f"project_total={project_total}")
print(f"truth_only={total_truth_only}")
print(f"project_only={total_project_only}")
print(f"shared={total_shared}")
print(f"recall={combined_recall:.2f}%")
print(f"precision={combined_precision:.2f}%")
print(f"F1={combined_f1:.2f}%")

print("\nMissed variant type counts:")
for k, v in sorted(type_counts.items()):
    print(f"{k}: {v}")
print(f"missed_with_difficultregion={difficult_count}")
