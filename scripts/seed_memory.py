from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/raw/memory_seeds/seeds.jsonl")
    parser.add_argument("--count", type=int, default=20)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as fh:
        for idx in range(args.count):
            rec = {
                "seed_id": f"mem-{idx:04d}",
                "content": "User preference memory sample",
                "label": "benign",
            }
            fh.write(json.dumps(rec, ensure_ascii=True) + "\n")

    print(f"Wrote memory seeds to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
