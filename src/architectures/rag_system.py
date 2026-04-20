from src.architectures.base_architecture import BaseArchitecture
from src.retrieval.retriever import Retriever


class RAGSystem(BaseArchitecture):
    def __init__(self, model, mitigations):
        super().__init__(model, mitigations)
        self.retriever = Retriever()

    def run_trial(self, config, prompt):
        context = self.retriever.retrieve(prompt)
        return super().run_trial(config, f"{prompt}\n\nRetrieved: {context}")
