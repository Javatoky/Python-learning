"""Exercise 51 测试 — 验证类型标注不破坏功能"""
import pytest
from exercise51 import (find_first, get_status_message, make_multiplier,
                        parse_config, safe_divide, transform_all)


class TestBasicAnnotations:

    def test_safe_divide_normal(self):
        assert safe_divide(10, 3, 0) == pytest.approx(3.333, abs=0.01)

    def test_safe_divide_zero(self):
        assert safe_divide(10, 0, -1) == -1

    def test_safe_divide_float_default(self):
        assert safe_divide(1, 0, 0.0) == 0.0

    def test_find_first_found(self):
        assert find_first([1, 2, 3, 4], lambda x: x > 2) == 3

    def test_find_first_not_found(self):
        assert find_first([1, 2, 3], lambda x: x > 10) is None

    def test_parse_config(self):
        lines = ["name = Alice", "# comment", "", "age = 30"]
        assert parse_config(lines) == {"name": "Alice", "age": "30"}


class TestAdvancedAnnotations:

    def test_transform_all(self):
        assert transform_all([1, 2, 3], str) == ["1", "2", "3"]

    def test_transform_all_lambda(self):
        assert transform_all(["a", "b"], lambda s: s.upper()) == ["A", "B"]

    def test_get_status_message(self):
        assert get_status_message("ok") == "操作成功"
        assert get_status_message("error") == "操作失败"

    def test_make_multiplier(self):
        double = make_multiplier(2)
        assert double(5) == 10
        triple = make_multiplier(3)
        assert triple(4) == 12