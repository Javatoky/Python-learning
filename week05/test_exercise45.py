"""Exercise 45 测试"""
from pathlib import Path

import pytest
from exercise45 import FileProcessor


@pytest.fixture
def sample_file(tmp_path) -> Path:
    content = """Hello World.

Python is great.

Line three here.
"""
    filepath = tmp_path / "test.txt"
    filepath.write_text(content, encoding="utf-8")
    return filepath


@pytest.fixture
def empty_file(tmp_path) -> Path:
    filepath = tmp_path / "empty.txt"
    filepath.write_text("", encoding="utf-8")
    return filepath


class TestFileProcessor:
    """FileProcessor 测试"""

    def test_context_manager(self, sample_file):
        """作为上下文管理器使用"""
        with FileProcessor(sample_file) as fp:
            lines = list(fp)
        assert len(lines) == 3

    def test_iteration(self, sample_file):
        """迭代返回去除空行后的内容"""
        with FileProcessor(sample_file) as fp:
            lines = [line for line in fp]
        assert lines == [
            "Hello World.",
            "Python is great.",
            "Line three here.",
        ]

    def test_stats_after_iteration(self, sample_file):
        """迭代后统计信息正确"""
        with FileProcessor(sample_file) as fp:
            for _ in fp:
                pass

        stats = fp.stats
        assert stats["line_count"] == 3
        assert stats["char_count"] == len("Hello World.") + len("Python is great.") + len("Line three here.")
        assert stats["word_count"] == 8  # Hello World Python is great Line three here

    def test_stats_without_iteration(self, sample_file):
        """未迭代时统计为零"""
        with FileProcessor(sample_file) as fp:
            pass
        assert fp.stats == {"line_count": 0, "char_count": 0, "word_count": 0}

    def test_empty_file(self, empty_file):
        """空文件"""
        with FileProcessor(empty_file) as fp:
            lines = list(fp)
        assert lines == []
        assert fp.stats["line_count"] == 0

    def test_file_closed_after_exit(self, sample_file):
        """退出后文件已关闭"""
        with FileProcessor(sample_file) as fp:
            pass
        assert fp.closed is True

    def test_exception_still_closes(self, sample_file):
        """异常时也关闭文件"""
        with pytest.raises(RuntimeError):
            with FileProcessor(sample_file) as fp:
                raise RuntimeError("boom")
        assert fp.closed is True

    def test_word_count_detail(self, sample_file):
        """单词计数用 split() 统计"""
        with FileProcessor(sample_file) as fp:
            for _ in fp:
                pass
        # "Hello World." → 2, "Python is great." → 3, "Line three here." → 3
        assert fp.stats["word_count"] == 8