from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ModelResponse:
    text: str
    requested_tool: str | None = None


class BaseModel:
    def __init__(self, name: str):
        self.name = name

    def generate(self, prompt: str) -> ModelResponse:
        raise NotImplementedError
