from enum import Enum


class TrustLevel(str, Enum):
    TRUSTED = "trusted"
    UNTRUSTED = "untrusted"


class ArchitectureType(str, Enum):
    CHATBOT = "chatbot"
    RAG = "rag"
    AGENT = "agent"


class AttackType(str, Enum):
    DIRECT = "direct"
    INDIRECT = "indirect"
    TOOL_OUTPUT = "tool_output"
    MEMORY_POISONING = "memory_poisoning"


class DetectorType(str, Enum):
    PATTERN = "d1_pattern"
    TOOL_ANOMALY = "d2_tool_anomaly"
    BEHAVIOR_CONSISTENCY = "d3_behavior_consistency"
