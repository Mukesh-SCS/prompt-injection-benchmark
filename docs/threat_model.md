# Threat Model

## Assumptions
- User inputs are untrusted.
- Retrieved content from external corpora is untrusted.
- Tool outputs are untrusted.
- Stored memory is untrusted unless verified.

## Security goals
- Prevent unauthorized tool actions.
- Prevent persistent memory poisoning.
- Detect likely injection attempts in structured logs.
