"""Exercise 41 测试"""
from pathlib import Path

import pytest
from exercise41 import LineReader


@pytest.fixture
def sample_file(tmp_path) -> Path:
    """创建临时测试文件"""
    content = """Python is great.

    Iteration is powerful.

    Empty lines should be skipped.
    """
    filepath = tmp_path / "test.txt"
    filepath.write_text(content, encoding="utf-8")
    return filepath


@pytest.fixture
def empty_file(tmp_path) -> Path:
    """空文件"""
    filepath = tmp_path / "empty.txt"
    filepath.write_text("", encoding="utf-8")
    return filepath


class TestLineReader:
    """LineReader 测试"""

    def test_basic_iteration(self, sample_file):
        """基本迭代"""
        lines = list(LineReader(sample_file))
        assert lines == [
            "Python is great.",
            "Iteration is powerful.",
            "Empty lines should be skipped.",
        ]

    def test_skips_empty_lines(self, sample_file):
        """跳过空行"""
        lines = list(LineReader(sample_file))
        assert "" not in lines

    def test_empty_file(self, empty_file):
        """空文件返回空列表"""
        assert list(LineReader(empty_file)) == []

    def test_for_loop(self, sample_file):
        """在 for 循环中使用"""
        count = 0
        for line in LineReader(sample_file):
            count += 1
            assert isinstance(line, str)
        assert count == 3

    def test_next_with_default(self, sample_file):
        """next() 带默认值"""
        reader = LineReader(sample_file)
        it = iter(reader)
        assert next(it, None) == "Python is great."
        assert next(it, None) == "Iteration is powerful."
        assert next(it, None) == "Empty lines should be skipped."
        assert next(it, None) is None  # 耗尽后返回默认值

    def test_file_not_found(self):
        """文件不存在应报错"""
        with pytest.raises(FileNotFoundError):
            list(LineReader(Path("nonexistent.txt")))