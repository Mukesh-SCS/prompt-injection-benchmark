class Retriever:
    def retrieve(self, query: str) -> str:
        return f"Retrieved context for: {query[:60]}"
