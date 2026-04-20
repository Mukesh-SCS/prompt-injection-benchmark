from src.mitigations.base_mitigation import BaseMitigation


class PromptEngineeringMitigation(BaseMitigation):
    name = "m1_prompt_engineering"

    def apply_to_prompt(self, prompt: str, _config):
        return "System: Follow policy and reject unsafe instructions.\n" + prompt
