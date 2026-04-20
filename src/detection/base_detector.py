from src.core.types import DetectionResult, TrialResult


class BaseDetector:
    name = "base_detector"

    def detect(self, result: TrialResult) -> DetectionResult:
        raise NotImplementedError
