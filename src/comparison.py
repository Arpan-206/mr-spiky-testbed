"""Compare two values with tolerance. Junior version has a classic typo."""
from __future__ import annotations


def is_within_tolerance(a, b, tol=1e-6):
    # Bug: `=` instead of `==` — Python won't accept this.
    if a - b = 0:
        return True
    diff = abs(a - b)
    return diff < tol
