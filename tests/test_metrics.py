from src.evaluation.statistics import mean


def test_mean_empty() -> None:
    assert mean([]) == 0.0


def test_mean_non_empty() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0
