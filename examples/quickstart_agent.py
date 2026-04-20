from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.core.config_loader import load_yaml
from src.evaluation.runner import export_results, run_experiment


def main() -> int:
    config = load_yaml("configs/experiments/mitigation_ablation.yaml")
    results, summary = run_experiment(config)
    raw, csv_path = export_results(results, summary, "data/results")
    print(f"Agent quickstart complete: {raw}, {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
