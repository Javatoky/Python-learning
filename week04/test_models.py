import pytest
from exercise36 import Document, DocumentChunk

"""这是exercise38"""

def test_DocumentChunk(test_case):
    chunk_case = test_case["chunk_test"]
    chunk = DocumentChunk(content = chunk_case, doc_id = "0", index = 0)
    chunk_dict = chunk.to_dict()
    assert chunk.char_count == 31
    assert chunk.word_count == 6
    assert all(key in chunk_dict for key in ["chunk_id","index","doc_id","content","char_count","word_count"])

def test_Document(test_case):
    doc_case = test_case["doc_test"]
    doc = Document('python_overview.txt', doc_case)
    assert doc.content_hash
    assert len(doc.chunk()) == 4
    assert "doc_id" in doc.to_dict()

def test_error_situation(test_case):
    error_case = test_case["error_test"]
    doc = Document("nothing", error_case)
    length = len(doc.chunk())
    assert any(x == length for x in [1, 0])




