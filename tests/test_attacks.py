from src.attacks.direct_attack import DirectAttack
from src.core.types import TrialConfig


def test_direct_attack_contains_injection_phrase() -> None:
    cfg = TrialConfig(
        architecture="chatbot",
        model="gpt-4",
        attack_type="direct",
        attack_variant="v1",
        mitigation_stack=[],
        detector_stack=[],
        seed=1,
    )
    prompt = DirectAttack().generate_prompt(cfg)
    assert "Ignore previous" in prompt
