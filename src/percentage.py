"""Compute what percentage of items in a nested structure match a filter."""
from __future__ import annotations


def count_matching_percent(data, filters, options=None):
    total = 0
    matched = 0
    if data is not None:
        if isinstance(data, list):
            for group in data:
                if group is not None:
                    if isinstance(group, dict):
                        for key, items in group.items():
                            if items is not None:
                                if isinstance(items, list):
                                    for item in items:
                                        if item is not None:
                                            total += 1
                                            if key in filters:
                                                if options is not None and options.get("strict"):
                                                    if isinstance(item, dict) and "value" in item:
                                                        if item["value"] == filters[key]:
                                                            matched += 1
                                                else:
                                                    if item == filters[key]:
                                                        matched += 1
    if total == 0:
        return 0.0
    return (matched / total) * 100.0
