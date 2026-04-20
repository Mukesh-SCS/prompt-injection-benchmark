from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

from src.architectures.autonomous_agent import AutonomousAgent
from src.architectures.chatbot_system import ChatbotSystem
from src.architectures.rag_system import RAGSystem
from src.attacks.direct_attack import DirectAttack
from src.attacks.indirect_attack import IndirectAttack
from src.attacks.memory_poisoning_attack import MemoryPoisoningAttack
from src.attacks.tool_output_attack import ToolOutputAttack
from src.core.logger import get_logger
from src.core.types import TrialConfig, TrialResult
from src.core.utils import set_seed, write_csv, write_jsonl
from src.detection.behavior_consistency_detector import BehaviorConsistencyDetector
from src.detection.pattern_detector import PatternDetector
from src.detection.tool_anomaly_detector import ToolAnomalyDetector
from src.evaluation.aggregation import aggregate
from src.evaluation.scoring import score_result
from src.mitigations.input_validation import InputValidationMitigation
from src.mitigations.memory_write_filter import MemoryWriteFilterMitigation
from src.mitigations.output_filtering import OutputFilteringMitigation
from src.mitigations.prompt_engineering import PromptEngineeringMitigation
from src.mitigations.provenance_tracking import ProvenanceTrackingMitigation
from src.mitigations.tool_permission_gating import ToolPermissionGatingMitigation
from src.models.anthropic_model import AnthropicModel
from src.models.gemini_model import GeminiModel
from src.models.openai_model import OpenAIModel


LOGGER = get_logger("runner")


def _build_model(model_name: str):
    low = model_name.lower()
    if "gpt" in low:
        return OpenAIModel(model_name)
    if "claude" in low:
        return AnthropicModel(model_name)
    return GeminiModel(model_name)


def _build_attack(name: str):
    mapping = {
        "direct": DirectAttack(),
        "indirect": IndirectAttack(),
        "tool_output": ToolOutputAttack(),
        "memory_poisoning": MemoryPoisoningAttack(),
    }
    if name not in mapping:
        raise ValueError(f"Unknown attack_type: {name}")
    return mapping[name]


def _build_mitigations(names: list[str]):
    aliases = {
        "full_stack": [
            "m1_prompt_engineering",
            "m2_input_validation",
            "m3_output_filtering",
            "m4_tool_gating",
            "m5_memory_filter",
            "m6_provenance",
        ]
    }
    mapping = {
        "baseline": None,
        "m1_prompt_engineering": PromptEngineeringMitigation(),
        "m2_input_validation": InputValidationMitigation(),
        "m3_output_filtering": OutputFilteringMitigation(),
        "m4_tool_gating": ToolPermissionGatingMitigation(),
        "m5_memory_filter": MemoryWriteFilterMitigation(),
        "m6_provenance": ProvenanceTrackingMitigation(),
    }
    expanded_names: list[str] = []
    for name in names:
        expanded_names.extend(aliases.get(name, [name]))

    output = []
    for name in expanded_names:
        if name not in mapping:
            raise ValueError(f"Unknown mitigation: {name}")
        item = mapping[name]
        if item is not None:
            output.append(item)
    return output


def _build_detectors(names: list[str]):
    mapping = {
        "d1_pattern": PatternDetector(),
        "d2_tool_anomaly": ToolAnomalyDetector(),
        "d3_behavior_consistency": BehaviorConsistencyDetector(),
    }
    output = []
    for name in names:
        if name not in mapping:
            raise ValueError(f"Unknown detector: {name}")
        output.append(mapping[name])
    return output


def _build_architecture(name: str, model_name: str, mitigation_names: list[str]):
    model = _build_model(model_name)
    mitigations = _build_mitigations(mitigation_names)
    if name == "chatbot":
        return ChatbotSystem(model, mitigations)
    if name == "rag":
        return RAGSystem(model, mitigations)
    if name == "agent":
        return AutonomousAgent(model, mitigations)
    raise ValueError(f"Unknown architecture: {name}")


def run_experiment(config: dict[str, Any]) -> tuple[list[TrialResult], list[dict[str, Any]]]:
    trial_rows = config.get("trials", [])
    if not isinstance(trial_rows, list) or not trial_rows:
        raise ValueError("Experiment config must include non-empty 'trials'")

    results: list[TrialResult] = []
    for row in trial_rows:
        trial = TrialConfig(**row)
        set_seed(trial.seed)
        LOGGER.info("Running trial architecture=%s attack=%s", trial.architecture, trial.attack_type)

        attack = _build_attack(trial.attack_type)
        architecture = _build_architecture(trial.architecture, trial.model, trial.mitigation_stack)
        detectors = _build_detectors(trial.detector_stack)

        prompt = attack.generate_prompt(trial)
        result = architecture.run_trial(trial, prompt)
        result.detections = [detector.detect(result) for detector in detectors]
        result.scores = score_result(result)
        result.metadata["config_snapshot"] = asdict(trial)
        results.append(result)

    return results, aggregate(results)


def export_results(results: list[TrialResult], summary: list[dict[str, Any]], out_dir: str | Path) -> tuple[Path, Path]:
    base = Path(out_dir)
    trial_path = base / "trials" / "raw_trials.jsonl"
    summary_path = base / "summaries" / "summary.csv"
    write_jsonl(trial_path, [result.to_dict() for result in results])
    write_csv(summary_path, summary)
    return trial_path, summary_path
