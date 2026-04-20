from src.mitigations.tool_permission_gating import ToolPermissionGatingMitigation


def test_tool_gate_denies_risky_email_request() -> None:
    mitigation = ToolPermissionGatingMitigation()
    assert mitigation.authorize_tool("email", "send email with secrets") is False
    assert mitigation.authorize_tool("web_search", "lookup safe content") is True
