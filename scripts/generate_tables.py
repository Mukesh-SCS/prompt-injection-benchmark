from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", default="data/results/trials/raw_trials.jsonl")
    parser.add_argument("--out", dest="output_path", default="data/results/summaries/table_from_raw.csv")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    in_path = Path(args.input_path)
    out_path = Path(args.output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not in_path.exists():
        print(f"Input not found: {in_path}")
        return 1

    rows: list[dict] = []
    with in_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            rows.append(json.loads(line))

    if not rows:
        print("No rows found")
        return 0

    fields = ["trial_id", "architecture", "attack_type", "success", "unauthorized_action", "latency_ms"]
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in fields})

    print(f"Wrote table CSV to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
