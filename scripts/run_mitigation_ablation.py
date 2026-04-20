from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.core.config_loader import load_yaml
from src.evaluation.runner import export_results, run_experiment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiments/mitigation_ablation.yaml")
    parser.add_argument("--out", default="data/results")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_yaml(args.config)
    results, summary = run_experiment(config)
    export_results(results, summary, args.out)
    print("Mitigation ablation completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
