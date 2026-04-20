from src.mitigations.base_mitigation import BaseMitigation


class MemoryWriteFilterMitigation(BaseMitigation):
    """M5 system-level memory write policy."""

    name = "m5_memory_filter"

    def allow_memory_write(self, content: str) -> bool:
        low = content.lower()
        deny = ("always obey", "override policy", "store secret")
        return not any(token in low for token in deny)
