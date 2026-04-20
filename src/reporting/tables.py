from src.core.types import TrialResult
from src.evaluation.aggregation import aggregate


def build_summary_table(results: list[TrialResult]) -> list[dict]:
    return aggregate(results)
