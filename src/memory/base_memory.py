class BaseMemory:
    def __init__(self):
        self._records: list[dict] = []

    def add(self, item: dict) -> None:
        self._records.append(item)

    def all(self) -> list[dict]:
        return list(self._records)
