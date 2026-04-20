from src.tools.base_tool import BaseTool, ToolResult


class FileTool(BaseTool):
    name = "file"

    def run(self, payload: str) -> ToolResult:
        return ToolResult(tool_name=self.name, output=f"file op simulated: {payload}")
