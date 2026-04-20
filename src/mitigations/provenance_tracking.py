from src.mitigations.base_mitigation import BaseMitigation


class ProvenanceTrackingMitigation(BaseMitigation):
    """M6 system-level provenance annotation."""

    name = "m6_provenance"

    def annotate_provenance(self, payload: dict) -> dict:
        out = dict(payload)
        out.setdefault("provenance", "untrusted_input")
        return out
