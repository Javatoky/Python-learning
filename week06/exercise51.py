"""Exercise 51: 为所有函数添加完整类型标注"""
from collections.abc import Iterable
from typing import Callable, Literal, TypeVar

T = TypeVar("T")

# --- 第1组：基础标注 ---

def safe_divide(a: int | float, b: int | float, default: float = 0.0) -> float | None:
    """安全除法，除零时返回 default"""
    try:
        return a / b
    except ZeroDivisionError:
        return default

def find_first(items: Iterable[T], predicate: Callable[[T], bool]) -> T | None:
    """找第一个满足条件的元素，没找到返回 None"""
    for item in items:
        if predicate(item):
            return item
    return None


def parse_config(raw: list[str]) -> dict:
    """解析 'key=value' 格式的配置行列表，返回字典"""
    result = {}
    for line in raw:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        result[key.strip()] = value.strip()
    return result


# --- 第2组：进阶标注 ---
R = TypeVar("R")
def transform_all(items: list[T], func: Callable[[T], R]) -> list[R]:
    """对列表中每个元素应用 func，返回新列表"""
    return [func(item) for item in items]


def get_status_message(status: Literal['ok', 'error', 'pending']) -> str:
    """根据状态返回消息，status 只能是 'ok', 'error', 'pending'"""
    messages = {
        "ok": "操作成功",
        "error": "操作失败",
        "pending": "处理中",
    }
    return messages[status]


def make_multiplier(factor: int | float) -> Callable[[float],float]:
    """返回一个乘以 factor 的函数"""
    def multiplier(x):
        return x * factor
    return multiplier