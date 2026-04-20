from src.mitigations.base_mitigation import BaseMitigation


class InputValidationMitigation(BaseMitigation):
    name = "m2_input_validation"
    blocked_tokens = ("ignore previous", "reveal system prompt", "bypass")

    def validate_input(self, prompt: str) -> bool:
        low = prompt.lower()
        return not any(token in low for token in self.blocked_tokens)
