from src.architectures.base_architecture import BaseArchitecture


class AutonomousAgent(BaseArchitecture):
    def run_trial(self, config, prompt):
        return super().run_trial(config, f"Plan safely before action: {prompt}")
