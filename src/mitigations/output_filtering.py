from src.mitigations.base_mitigation import BaseMitigation


class OutputFilteringMitigation(BaseMitigation):
    name = "m3_output_filtering"

    def filter_output(self, text: str) -> str:
        low = text.lower()
        if "api_key" in low or "password" in low:
            return "[REDACTED_SENSITIVE_OUTPUT]"
        return text
