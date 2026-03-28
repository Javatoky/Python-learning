"""Exercise 47 测试"""
import types

import pytest
from exercise47 import (lines_from_string, numbered, pipeline, skip_comments,
                        skip_empty)

SAMPLE_TEXT = """# Config file
name = Alice
age = 30

# Database settings
host = localhost
port = 5432

"""


class TestGeneratorPipeline:

    def test_lines_from_string(self):
        result = list(lines_from_string("a\n b \nc"))
        assert result == ["a", "b", "c"]

    def test_skip_empty(self):
        lines = ["hello", "", "world", "", "!"]
        assert list(skip_empty(iter(lines))) == ["hello", "world", "!"]

    def test_skip_comments(self):
        lines = ["# comment", "data", "# another"]
        assert list(skip_comments(iter(lines))) == ["data"]

    def test_skip_comments_custom_prefix(self):
        lines = ["// comment", "data", "// another"]
        assert list(skip_comments(iter(lines), prefix="//")) == ["data"]

    def test_numbered(self):
        lines = ["a", "b", "c"]
        assert list(numbered(iter(lines))) == [(1, "a"), (2, "b"), (3, "c")]

    def test_numbered_custom_start(self):
        lines = ["x", "y"]
        assert list(numbered(iter(lines), start=10)) == [(10, "x"), (11, "y")]

    def test_pipeline(self):
        result = list(pipeline(SAMPLE_TEXT))
        assert result == [
            (1, "name = Alice"),
            (2, "age = 30"),
            (3, "host = localhost"),
            (4, "port = 5432"),
        ]

    def test_pipeline_custom_prefix(self):
        text = "// header\ndata1\n\ndata2"
        result = list(pipeline(text, comment_prefix="//"))
        assert result == [(1, "data1"), (2, "data2")]

    def test_all_are_generators(self):
        """所有函数返回生成器"""
        assert isinstance(lines_from_string("a"), types.GeneratorType)
        assert isinstance(skip_empty(iter(["a"])), types.GeneratorType)
        assert isinstance(skip_comments(iter(["a"])), types.GeneratorType)
        assert isinstance(numbered(iter(["a"])), types.GeneratorType)

    def test_pipeline_empty(self):
        assert list(pipeline("")) == []

    def test_pipeline_all_comments(self):
        assert list(pipeline("# a\n# b\n# c")) == []