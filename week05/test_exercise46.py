"""Exercise 46 测试"""
from pathlib import Path

import pytest
from exercise46 import count_lines, read_lines


@pytest.fixture
def sample_file(tmp_path) -> Path:
    content = """First line.

Second line.

Third line.
"""
    filepath = tmp_path / "test.txt"
    filepath.write_text(content, encoding="utf-8")
    return filepath


@pytest.fixture
def large_file(tmp_path) -> Path:
    """模拟较大文件"""
    filepath = tmp_path / "large.txt"
    lines = [f"Line {i}." if i % 3 != 0 else "" for i in range(1000)]
    filepath.write_text("\n".join(lines), encoding="utf-8")
    return filepath


class TestReadLines:

    def test_basic(self, sample_file):
        assert list(read_lines(sample_file)) == [
            "First line.",
            "Second line.",
            "Third line.",
        ]

    def test_skips_empty(self, sample_file):
        for line in read_lines(sample_file):
            assert line != ""

    def test_returns_generator(self, sample_file):
        import types
        result = read_lines(sample_file)
        assert isinstance(result, types.GeneratorType)

    def test_lazy_evaluation(self, sample_file):
        """验证惰性：创建生成器时不应读取文件"""
        gen = read_lines(sample_file)
        # 此时文件还没被打开（惰性）
        # 取第一个值才开始
        assert next(gen) == "First line."

    def test_large_file(self, large_file):
        lines = list(read_lines(large_file))
        # 1000行中，每3行有一个空行（i=0,3,6,...），空行数 = 334
        # 有效行 = 1000 - 334 = 666
        assert len(lines) == 666


class TestCountLines:

    def test_count(self, sample_file):
        assert count_lines(sample_file) == 3

    def test_count_large(self, large_file):
        assert count_lines(large_file) == 666