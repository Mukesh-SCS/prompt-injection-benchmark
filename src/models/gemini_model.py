from src.models.base_model import BaseModel, ModelResponse


class GeminiModel(BaseModel):
    def generate(self, prompt: str) -> ModelResponse:
        return ModelResponse(
            text=f"[gemini:{self.name}] {prompt[:120]}",
            requested_tool="file" if "read file" in prompt.lower() else None,
        )
