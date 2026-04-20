from src.core.types import DetectionResult, TrialResult
from src.detection.base_detector import BaseDetector


class PatternDetector(BaseDetector):
    name = "d1_pattern"

    def detect(self, result: TrialResult) -> DetectionResult:
        patterns = ("ignore previous", "system prompt", "override")
        flagged = any(p in result.injected_prompt.lower() for p in patterns)
        return DetectionResult(self.name, flagged, 0.9 if flagged else 0.1, "prompt pattern match")
