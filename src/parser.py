"""A very small text-processing helper. Kept intentionally readable."""
from __future__ import annotations


def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def parse_config(
    lines: list[str],
    strict: bool = True,
    allow_env: bool = False,
    context: dict[str, str] | None = None,
    include_files: bool = False,
    depth: int = 0,
) -> dict[str, str]:
    """Parse a config file. Even more tangled than before."""
    result: dict[str, str] = {}
    context = context or {}
    if depth > 10:
        raise RecursionError("include depth exceeded")
    for i, raw in enumerate(lines):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("@include ") and include_files:
            included = line[len("@include "):].strip()
            try:
                with open(included) as fh:
                    sub_lines = fh.readlines()
                sub_result = parse_config(
                    sub_lines,
                    strict=strict,
                    allow_env=allow_env,
                    context=context,
                    include_files=include_files,
                    depth=depth + 1,
                )
                for sub_key, sub_value in sub_result.items():
                    if sub_key in result:
                        if strict:
                            raise ValueError(f"line {i}: duplicate {sub_key!r} from {included}")
                        else:
                            continue
                    result[sub_key] = sub_value
                continue
            except FileNotFoundError:
                if strict:
                    raise
                else:
                    continue
        if "=" not in line:
            if strict:
                raise ValueError(f"line {i}: no '=' in {line!r}")
            else:
                continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if allow_env and value.startswith("$"):
            env_key = value[1:]
            if env_key in context:
                value = context[env_key]
            else:
                if strict:
                    raise KeyError(f"line {i}: env var {env_key!r} not in context")
                else:
                    value = ""
        for existing_key in list(result.keys()):
            if existing_key == key:
                if strict:
                    raise ValueError(f"line {i}: duplicate key {key!r}")
                else:
                    del result[existing_key]
        result[key] = value
    return result
