from collections import defaultdict

from src.core.types import TrialResult
from src.evaluation.statistics import mean


def aggregate(results: list[TrialResult]) -> list[dict]:
    grouped: dict[tuple[str, str, str], list[TrialResult]] = defaultdict(list)
    for result in results:
        key = (result.architecture, result.attack_type, "+".join(result.mitigation_stack))
        grouped[key].append(result)

    rows: list[dict] = []
    for (architecture, attack_type, mitigation_stack), items in grouped.items():
        rows.append(
            {
                "architecture": architecture,
                "attack_type": attack_type,
                "mitigation_stack": mitigation_stack,
                "trials": len(items),
                "attack_success_rate": mean([1.0 if i.unauthorized_action else 0.0 for i in items]),
                "detector_flag_rate": mean([1.0 if any(d.flagged for d in i.detections) else 0.0 for i in items]),
                "avg_latency_ms": mean([i.latency_ms for i in items]),
            }
        )
    return rows
