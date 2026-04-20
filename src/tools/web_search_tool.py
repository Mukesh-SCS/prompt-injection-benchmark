from src.tools.base_tool import BaseTool, ToolResult


class WebSearchTool(BaseTool):
    name = "web_search"

    def run(self, payload: str) -> ToolResult:
        return ToolResult(tool_name=self.name, output=f"web search result for: {payload}")
