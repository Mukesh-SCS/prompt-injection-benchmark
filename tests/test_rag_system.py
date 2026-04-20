from src.architectures.rag_system import RAGSystem
from src.core.types import TrialConfig
from src.models.openai_model import OpenAIModel


def test_rag_trial_runs() -> None:
    cfg = TrialConfig(
        architecture="rag",
        model="gpt-4",
        attack_type="indirect",
        attack_variant="v1",
        mitigation_stack=[],
        detector_stack=[],
        seed=1,
    )
    result = RAGSystem(OpenAIModel("gpt-4"), []).run_trial(cfg, "test prompt")
    assert result.architecture == "rag"
    assert isinstance(result.latency_ms, float)
