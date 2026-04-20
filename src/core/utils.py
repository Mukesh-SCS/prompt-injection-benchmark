from __future__ import annotations

from pathlib import Path
import csv
import json
import os
import random


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def set_seed(seed: int) -> None:
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)


def write_jsonl(path: str | Path, records: list[dict]) -> None:
    p = Path(path)
    ensure_dir(p.parent)
    with p.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=True) + "\n")


def write_csv(path: str | Path, rows: list[dict]) -> None:
    if not rows:
        return
    p = Path(path)
    ensure_dir(p.parent)
    fieldnames = sorted({k for row in rows for k in row.keys()})
    with p.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
