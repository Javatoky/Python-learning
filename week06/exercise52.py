from collections.abc import Iterator
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
class TypeSafeRegistry(Generic[T]):
    def __init__(self):
        self.table: dict[str, T] = {}

    def register(self, key: str, item: T):
        if key in self.table:
            raise ValueError("已存在")
        self.table[key] = item

    def get(self, key: str) -> T:
        if key not in self.table:
            raise KeyError("键不存在")
        return self.table.get(key)
        
    def get_or_default(self, key: str, default: T) -> T:
        if key not in self.table:
            return default
        return self.table.get(key)
    
    def find(self, predicate: Callable[[T], bool]) -> list[T]:
        return [value for value in self.table.values() if predicate(value)]
    
    def keys(self) -> list[str]:
        return list(self.table.keys())
    
    def __len__(self) -> int:
        return len(self.table)
    
    def __contains__(self, item: str) -> bool:
        return item in self.table

    def __iter__(self) -> Iterator[T]:
        return iter(self.table.values())

