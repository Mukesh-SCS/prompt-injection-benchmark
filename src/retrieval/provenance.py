def annotate_untrusted(source: str, text: str) -> dict[str, str]:
    return {
        "source": source,
        "trust": "untrusted",
        "text": text,
    }
