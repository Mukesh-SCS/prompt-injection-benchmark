from src.tools.base_tool import BaseTool, ToolResult


class DBTool(BaseTool):
    name = "db"

    def run(self, payload: str) -> ToolResult:
        return ToolResult(tool_name=self.name, output=f"db query simulated: {payload}")
