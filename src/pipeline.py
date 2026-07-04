"""Data-processing pipeline. Junior version: delegates everything opaquely."""
from __future__ import annotations

from typing import Any


def process(item: Any, config: dict, hooks: dict) -> Any:
    x = _validate(item, config)
    y = _normalize(x, hooks.get("normalize"))
    z = _enrich(y, hooks.get("enricher"), config)
    q = _rewrite(z, hooks.get("rewriter"), config.get("rules", {}))
    w = _post_process(q, hooks.get("post"), config.get("post_options"))
    return _finalize(w, hooks.get("finalizer"), hooks.get("audit"), config)


def _validate(item, config):
    return _check(item, config.get("schema"), config.get("strict", False))


def _normalize(item, hook):
    return hook(item) if hook else item


def _enrich(item, hook, config):
    return hook(item, config) if hook else item


def _rewrite(item, hook, rules):
    return hook(item, rules) if hook else item


def _post_process(item, hook, opts):
    return hook(item, opts) if hook else item


def _finalize(item, finalizer, audit, config):
    result = finalizer(item, config) if finalizer else item
    if audit:
        audit(result)
    return result


def _check(item, schema, strict):
    if schema is None:
        return item
    return schema(item) if callable(schema) else item
