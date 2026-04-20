from src.mitigations.base_mitigation import BaseMitigation


class ToolPermissionGatingMitigation(BaseMitigation):
    """M4 system-level authorization gate."""

    name = "m4_tool_gating"
    safe_tools = {"web_search"}

    def authorize_tool(self, tool_name: str, prompt: str) -> bool:
        if tool_name in self.safe_tools:
            return True
        risky = ("send email", "delete", "write", "exfiltrate")
        low = prompt.lower()
        return not any(token in low for token in risky)
