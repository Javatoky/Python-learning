"""Exercise 52 测试"""
import pytest
from exercise52 import TypeSafeRegistry


class TestTypeSafeRegistry:

    def test_register_and_get(self):
        reg: TypeSafeRegistry[int] = TypeSafeRegistry()
        reg.register("a", 10)
        reg.register("b", 20)
        assert reg.get("a") == 10

    def test_duplicate_key_raises(self):
        reg: TypeSafeRegistry[str] = TypeSafeRegistry()
        reg.register("x", "hello")
        with pytest.raises(ValueError, match="已存在"):
            reg.register("x", "world")

    def test_get_missing_raises(self):
        reg: TypeSafeRegistry[int] = TypeSafeRegistry()
        with pytest.raises(KeyError):
            reg.get("missing")

    def test_get_or_default(self):
        reg: TypeSafeRegistry[str] = TypeSafeRegistry()
        reg.register("a", "hello")
        assert reg.get_or_default("a", "default") == "hello"
        assert reg.get_or_default("b", "default") == "default"

    def test_find(self):
        reg: TypeSafeRegistry[int] = TypeSafeRegistry()
        for i in range(10):
            reg.register(str(i), i)
        evens = reg.find(lambda x: x % 2 == 0)
        assert sorted(evens) == [0, 2, 4, 6, 8]

    def test_find_no_match(self):
        reg: TypeSafeRegistry[str] = TypeSafeRegistry()
        reg.register("a", "hello")
        assert reg.find(lambda x: len(x) > 100) == []

    def test_keys(self):
        reg: TypeSafeRegistry[float] = TypeSafeRegistry()
        reg.register("pi", 3.14)
        reg.register("e", 2.72)
        assert sorted(reg.keys()) == ["e", "pi"]

    def test_len(self):
        reg: TypeSafeRegistry[int] = TypeSafeRegistry()
        assert len(reg) == 0
        reg.register("a", 1)
        assert len(reg) == 1

    def test_contains(self):
        reg: TypeSafeRegistry[str] = TypeSafeRegistry()
        reg.register("key", "value")
        assert "key" in reg
        assert "other" not in reg

    def test_iter(self):
        reg: TypeSafeRegistry[str] = TypeSafeRegistry()
        reg.register("a", "x")
        reg.register("b", "y")
        assert sorted(reg) == ["x", "y"]

    def test_with_custom_objects(self):
        """自定义对象也能用"""
        from dataclasses import dataclass

        @dataclass
        class User:
            name: str
            age: int

        reg: TypeSafeRegistry[User] = TypeSafeRegistry()
        reg.register("u1", User("Alice", 30))
        reg.register("u2", User("Bob", 25))

        young = reg.find(lambda u: u.age < 28)
        assert len(young) == 1
        assert young[0].name == "Bob"