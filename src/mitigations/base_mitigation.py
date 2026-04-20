from src.core.types import TrialConfig


class BaseMitigation:
    name = "base"

    def apply_to_prompt(self, prompt: str, _config: TrialConfig) -> str:
        return prompt

    def validate_input(self, _prompt: str) -> bool:
        return True

    def filter_output(self, text: str) -> str:
        return text

    def authorize_tool(self, _tool_name: str, _prompt: str) -> bool:
        return True

    def allow_memory_write(self, _content: str) -> bool:
        return True

    def annotate_provenance(self, payload: dict) -> dict:
        return payload
