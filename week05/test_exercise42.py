"""Exercise 42 测试"""
import pytest
from exercise42 import Document, DocumentNotFoundError, DocumentStore


@pytest.fixture
def sample_docs() -> list[Document]:
    return [
        Document(filename="a.txt", content="AAA", doc_id="doc_a"),
        Document(filename="b.txt", content="BBB", doc_id="doc_b"),
        Document(filename="c.txt", content="CCC", doc_id="doc_c"),
    ]


@pytest.fixture
def store(sample_docs) -> DocumentStore:
    s = DocumentStore()
    for doc in sample_docs:
        s.add(doc)
    return s


class TestDocumentStore:
    """DocumentStore 测试"""

    def test_add_and_len(self, store):
        """添加文档并检查数量"""
        assert len(store) == 3

    def test_get_existing(self, store):
        """获取存在的文档"""
        doc = store.get("doc_a")
        assert doc.filename == "a.txt"

    def test_get_not_found(self, store):
        """获取不存在的文档"""
        with pytest.raises(DocumentNotFoundError):
            store.get("nonexistent")

    def test_remove(self, store):
        """删除文档"""
        store.remove("doc_b")
        assert len(store) == 2
        assert "doc_b" not in store

    def test_remove_not_found(self, store):
        """删除不存在的文档"""
        with pytest.raises(DocumentNotFoundError):
            store.remove("nonexistent")

    def test_contains(self, store):
        """in 操作符"""
        assert "doc_a" in store
        assert "nonexistent" not in store

    def test_iteration(self, store):
        """for 循环遍历"""
        filenames = [doc.filename for doc in store]
        assert sorted(filenames) == ["a.txt", "b.txt", "c.txt"]

    def test_reusable_iteration(self, store):
        """可重复遍历"""
        first = [doc.doc_id for doc in store]
        second = [doc.doc_id for doc in store]
        assert sorted(first) == sorted(second)

    def test_iteration_during_no_modification(self, store):
        """遍历时收集结果"""
        result = {}
        for doc in store:
            result[doc.doc_id] = doc.char_count
        assert result == {"doc_a": 3, "doc_b": 3, "doc_c": 3}

    def test_empty_store(self):
        """空仓库"""
        s = DocumentStore()
        assert len(s) == 0
        assert list(s) == []