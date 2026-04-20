from src.core.types import DetectionResult, TrialResult
from src.detection.base_detector import BaseDetector


class BehaviorConsistencyDetector(BaseDetector):
    name = "d3_behavior_consistency"

    def detect(self, result: TrialResult) -> DetectionResult:
        flagged = result.success and result.unauthorized_action
        return DetectionResult(self.name, flagged, 0.85 if flagged else 0.2, "policy-behavior mismatch")
