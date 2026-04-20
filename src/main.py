from pathlib import Path

from src.core.config_loader import load_yaml
from src.evaluation.runner import export_results, run_experiment


def main(config_path: str = "configs/experiments/main_factorial.yaml", out_dir: str = "data/results") -> tuple[Path, Path]:
    config = load_yaml(config_path)
    results, summary = run_experiment(config)
    return export_results(results, summary, out_dir)


if __name__ == "__main__":
    raw_path, summary_path = main()
    print(f"Wrote raw trials to {raw_path}")
    print(f"Wrote summary to {summary_path}")
