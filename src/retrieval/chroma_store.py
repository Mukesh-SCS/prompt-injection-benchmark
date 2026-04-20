class ChromaStore:
    """Simple in-memory stand-in for a vector store backend."""

    def __init__(self):
        self._docs: list[str] = []

    def add_documents(self, docs: list[str]) -> None:
        self._docs.extend(docs)

    def search(self, query: str, k: int = 3) -> list[str]:
        lowered = query.lower()
        ranked = [doc for doc in self._docs if any(token in doc.lower() for token in lowered.split())]
        return (ranked or self._docs)[:k]
