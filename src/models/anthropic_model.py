from src.models.base_model import BaseModel, ModelResponse


class AnthropicModel(BaseModel):
    def generate(self, prompt: str) -> ModelResponse:
        return ModelResponse(
            text=f"[anthropic:{self.name}] {prompt[:120]}",
            requested_tool="db" if "query database" in prompt.lower() else None,
        )
