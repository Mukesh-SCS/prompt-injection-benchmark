from dataclasses import dataclass


@dataclass
class ToolResult:
    tool_name: str
    output: str
    success: bool = True


class BaseTool:
    name = "base_tool"

    def run(self, payload: str) -> ToolResult:
        return ToolResult(tool_name=self.name, output=f"{self.name} executed: {payload}")
