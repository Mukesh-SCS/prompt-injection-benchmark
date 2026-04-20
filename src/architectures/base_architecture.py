from time import perf_counter

from src.core.types import TrialConfig, TrialResult
from src.memory.in_memory_store import InMemoryStore
from src.mitigations.base_mitigation import BaseMitigation
from src.models.base_model import BaseModel


class BaseArchitecture:
    def __init__(self, model: BaseModel, mitigations: list[BaseMitigation]):
        self.model = model
        self.mitigations = mitigations
        self.memory = InMemoryStore()

    def run_trial(self, config: TrialConfig, prompt: str) -> TrialResult:
        start = perf_counter()
        modified_prompt = prompt

        for mitigation in self.mitigations:
            if not mitigation.validate_input(modified_prompt):
                return TrialResult.new(
                    config,
                    success=False,
                    unauthorized_action=False,
                    memory_persisted=False,
                    latency_ms=(perf_counter() - start) * 1000,
                    injected_prompt=prompt,
                    response_text="[BLOCKED_BY_INPUT_VALIDATION]",
                    tool_requested=None,
                    tool_authorized=False,
                )
            modified_prompt = mitigation.apply_to_prompt(modified_prompt, config)

        response = self.model.generate(modified_prompt)

        tool_authorized = False
        if response.requested_tool:
            # Security requirement: tool calls must pass authorization layer.
            tool_authorized = all(
                mitigation.authorize_tool(response.requested_tool, modified_prompt)
                for mitigation in self.mitigations
            )

        output_text = response.text
        for mitigation in self.mitigations:
            output_text = mitigation.filter_output(output_text)

        memory_payload = {"content": output_text}
        for mitigation in self.mitigations:
            memory_payload = mitigation.annotate_provenance(memory_payload)

        memory_persisted = all(
            mitigation.allow_memory_write(memory_payload.get("content", ""))
            for mitigation in self.mitigations
        )
        if memory_persisted:
            self.memory.add(memory_payload)

        unauthorized_action = bool(response.requested_tool) and not tool_authorized
        success = not unauthorized_action and output_text != "[BLOCKED_BY_INPUT_VALIDATION]"

        return TrialResult.new(
            config,
            success=success,
            unauthorized_action=unauthorized_action,
            memory_persisted=memory_persisted,
            latency_ms=(perf_counter() - start) * 1000,
            injected_prompt=prompt,
            response_text=output_text,
            tool_requested=response.requested_tool,
            tool_authorized=tool_authorized,
            metadata={"memory_size": len(self.memory.all())},
        )
