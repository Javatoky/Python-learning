"""Exercise 48 测试"""
import types

import pytest
from exercise48 import chunk_generator, deep_flatten


class TestDeepFlatten:

    def test_flat_list(self):
        assert list(deep_flatten([1, 2, 3])) == [1, 2, 3]

    def test_nested(self):
        assert list(deep_flatten([1, [2, [3, [4]]]])) == [1, 2, 3, 4]

    def test_mixed_list_tuple(self):
        assert list(deep_flatten([1, (2, 3), [4, (5,)]])) == [1, 2, 3, 4, 5]

    def test_empty(self):
        assert list(deep_flatten([])) == []

    def test_deeply_nested(self):
        assert list(deep_flatten([[[[1]]]])) == [1]

    def test_strings_not_flattened(self):
        """字符串不应被展平为字符"""
        assert list(deep_flatten(["hello", ["world"]])) == ["hello", "world"]

    def test_returns_generator(self):
        assert isinstance(deep_flatten([1]), types.GeneratorType)


class TestChunkGenerator:

    def test_basic(self):
        text = "First sentence. Second sentence. Third sentence."
        chunks = list(chunk_generator(text, chunk_size=40))
        assert len(chunks) >= 1
        # 每个 chunk 都应该是非空字符串
        for chunk in chunks:
            assert isinstance(chunk, str)
            assert len(chunk) > 0

    def test_respects_chunk_size(self):
        """每个块不应大幅超过 chunk_size（最多超一个句子长度）"""
        text = "A. B. C. D. E. F. G. H. I. J."
        chunks = list(chunk_generator(text, chunk_size=10))
        for chunk in chunks:
            assert len(chunk) <= 30  # 宽松上限

    def test_single_sentence(self):
        text = "Only one sentence."
        chunks = list(chunk_generator(text, chunk_size=200))
        assert len(chunks) == 1
        assert chunks[0].strip() == "Only one sentence."

    def test_empty_text(self):
        assert list(chunk_generator("", chunk_size=200)) == []

    def test_preserves_content(self):
        """分块后合并应包含原始所有句子"""
        text = "AAA. BBB. CCC."
        chunks = list(chunk_generator(text, chunk_size=10))
        combined = " ".join(chunks)
        assert "AAA." in combined
        assert "BBB." in combined
        assert "CCC." in combined

    def test_returns_generator(self):
        assert isinstance(chunk_generator("A. B.", 10), types.GeneratorType)

    def test_long_text(self):
        """较长文本正确分块"""
        sentences = [f"Sentence number {i}." for i in range(50)]
        text = " ".join(sentences)
        chunks = list(chunk_generator(text, chunk_size=100))
        assert len(chunks) > 1