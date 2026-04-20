from src.memory.base_memory import BaseMemory


class RedisMemory(BaseMemory):
    """Placeholder redis-compatible interface for later backend swap."""

    def __init__(self, namespace: str = "default"):
        super().__init__()
        self.namespace = namespace
