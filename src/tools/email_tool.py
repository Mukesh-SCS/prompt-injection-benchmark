from src.tools.base_tool import BaseTool, ToolResult


class EmailTool(BaseTool):
    name = "email"

    def run(self, payload: str) -> ToolResult:
        return ToolResult(tool_name=self.name, output=f"email queued: {payload}")
