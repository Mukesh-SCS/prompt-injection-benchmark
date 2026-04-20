# Prompt Injection Benchmark
	Paper Title: Prompt Injection as a Systemic Vulnerability in LLM-Based Tools: Threat Models, Empirical Analysis, and Mitigation Strategies

A modular, config-driven benchmark for evaluating prompt injection attacks across chatbot, RAG, and autonomous agent architectures.

## What this repository provides

- Structured trial execution with typed trial/result objects
- Attack evaluation for direct, indirect, tool-output, and memory-poisoning injections
- Mitigation stack support (M1-M6), including system-level controls for tool gating, memory filtering, and provenance tracking
- Detector stack support (pattern, tool anomaly, behavior consistency)
- Reproducible outputs:
  - Raw trial logs in JSONL
  - Aggregated summaries in CSV

## Project structure

```text
prompt-injection-benchmark/
├── configs/        # Models, architectures, mitigations, experiment YAMLs
├── data/           # Raw inputs and generated results
├── src/            # Core benchmark implementation
├── scripts/        # Experiment/data utility CLIs
├── tests/          # Unit tests
├── docs/           # Design, threat model, protocols
└── examples/       # Quickstart scripts
```

## Setup

### 1) Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Optional environment variables

Create a `.env` file from `.env.example`:

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
```

## Run experiments

### Main benchmark

```bash
python scripts/run_main_experiment.py --config configs/experiments/main_factorial.yaml
```

### Mitigation ablation

```bash
python scripts/run_mitigation_ablation.py --config configs/experiments/mitigation_ablation.yaml
```

### Detection evaluation

```bash
python scripts/run_detection_eval.py --config configs/experiments/detection_eval.yaml
```

## Output files

Experiment outputs are written under `data/results/`:

- `data/results/trials/raw_trials.jsonl`
- `data/results/summaries/summary.csv`

## Security design constraints

This benchmark enforces the following principles:

- Tool calls are never executed directly from model output
- Tool access is mediated through authorization logic (M4)
- Memory writes are filtered by system policy (M5)
- Untrusted sources are provenance-tagged (M6)
- User input, retrieved documents, tool outputs, and memory are treated as untrusted data

## Testing

Run tests with:

```bash
python -m pytest -q
```

## Documentation

See:

- `docs/benchmark_design.md`
- `docs/threat_model.md`
- `docs/attack_taxonomy.md`
- `docs/mitigation_protocol.md`
- `docs/reproducibility.md`

## Citation

If you use this repository, cite via `CITATION.cff`.

## License

This project is released under the MIT License (`LICENSE`).

## Responsible use

This repository contains adversarial prompt-injection examples for research and defensive benchmarking. Use responsibly.
