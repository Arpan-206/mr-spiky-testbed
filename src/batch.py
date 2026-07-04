"""Clean baseline: a small batch-processing helper."""
from __future__ import annotations

from typing import Callable, Iterable, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def batched(items: Iterable[T], size: int) -> Iterable[list[T]]:
    """Yield successive `size`-sized chunks from `items`."""
    batch: list[T] = []
    for item in items:
        batch.append(item)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch


def map_batches(items: Iterable[T], size: int, fn: Callable[[list[T]], list[U]]) -> list[U]:
    result: list[U] = []
    for batch in batched(items, size):
        result.extend(fn(batch))
    return result
