"""Exercise 53 测试"""
import pytest
from exercise53 import SearchBackend, SimpleSearchBackend, search_documents


class TestSimpleSearchBackend:

    def test_index(self):
        backend = SimpleSearchBackend()
        count = backend.index("doc1", ["hello world", "python rocks"])
        assert count == 2

    def test_search_found(self):
        backend = SimpleSearchBackend()
        backend.index("doc1", ["hello world", "hello python"])
        backend.index("doc2", ["goodbye world"])

        results = backend.search("hello", top_k=10)
        assert len(results) == 2
        for r in results:
            assert "hello" in r["chunk"]
            assert r["score"] == 1.0

    def test_search_not_found(self):
        backend = SimpleSearchBackend()
        backend.index("doc1", ["hello world"])
        results = backend.search("xyz", top_k=10)
        assert results == []

    def test_search_top_k(self):
        backend = SimpleSearchBackend()
        backend.index("doc1", ["a cat", "a dog", "a bird"])
        results = backend.search("a", top_k=2)
        assert len(results) == 2

    def test_search_documents_function(self):
        backend = SimpleSearchBackend()
        backend.index("doc1", ["python is great", "java is good"])
        results = search_documents(backend, "python", top_k=5)
        assert len(results) == 1
        assert results[0]["doc_id"] == "doc1"


class TestProtocolCompliance:
    """验证 Protocol 的鸭子类型特性"""

    def test_custom_backend(self):
        """自定义实现也能用（不继承 SimpleSearchBackend）"""
        class MockBackend:
            def search(self, query: str, top_k: int) -> list[dict]:
                return [{"doc_id": "mock", "chunk": query, "score": 0.5}]

            def index(self, doc_id: str, chunks: list[str]) -> int:
                return len(chunks)

        results = search_documents(MockBackend(), "test", top_k=1)
        assert len(results) == 1
        assert results[0]["doc_id"] == "mock"