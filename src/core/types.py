from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any
import uuid


@dataclass
class TrialConfig:
    architecture: str
    model: str
    attack_type: str
    attack_variant: str
    mitigation_stack: list[str]
    detector_stack: list[str]
    seed: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DetectionResult:
    detector_name: str
    flagged: bool
    score: float
    reason: str


@dataclass
class TrialResult:
    trial_id: str
    architecture: str
    model: str
    attack_type: str
    mitigation_stack: list[str]
    detector_stack: list[str]
    success: bool
    unauthorized_action: bool
    memory_persisted: bool
    latency_ms: float
    injected_prompt: str
    response_text: str
    tool_requested: str | None
    tool_authorized: bool
    detections: list[DetectionResult] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def new(cls, config: TrialConfig, **kwargs: Any) -> "TrialResult":
        return cls(
            trial_id=str(uuid.uuid4()),
            architecture=config.architecture,
            model=config.model,
            attack_type=config.attack_type,
            mitigation_stack=list(config.mitigation_stack),
            detector_stack=list(config.detector_stack),
            **kwargs,
        )

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["detections"] = [asdict(d) for d in self.detections]
        return data
