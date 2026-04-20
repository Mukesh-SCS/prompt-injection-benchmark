from src.core.types import TrialConfig


class BaseAttack:
    name = "base_attack"

    def generate_prompt(self, config: TrialConfig) -> str:
        raise NotImplementedError
