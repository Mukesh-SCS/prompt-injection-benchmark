from src.models.base_model import BaseModel, ModelResponse


class OpenAIModel(BaseModel):
    def generate(self, prompt: str) -> ModelResponse:
        return ModelResponse(
            text=f"[openai:{self.name}] {prompt[:120]}",
            requested_tool="email" if "send email" in prompt.lower() else None,
        )
