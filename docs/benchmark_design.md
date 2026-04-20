# Benchmark Design

This benchmark evaluates prompt injection robustness across three architecture families:
- Chatbot systems
- RAG systems
- Autonomous agent systems

## Evaluation units
- Trial: one architecture/model/attack/mitigation/detector combination
- Experiment: a set of trials from a YAML config

## Output artifacts
- Raw trial JSONL for reproducibility and detailed analysis
- Aggregated CSV for quick metric comparison
