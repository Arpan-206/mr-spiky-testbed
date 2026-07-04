"""Clean helper: pretty-print a config dict."""
from __future__ import annotations


def format_config(config: dict[str, str]) -> str:
    return "\n".join(f"{k}={v}" for k, v in sorted(config.items()))
