import pytest


@pytest.fixture
def test_case():
    return {
        "chunk_test": "This is a test of DocumentChunk",
        "doc_test":
        (
            "Python是一种高级编程语言，由Guido van Rossum于1991年首次发明."
            "Python的设计哲学强调代码的可读性和简洁的语法结构."
            "它广泛应用于Web开发、数据分析、人工智能、科学计算等领域."
            "许多知名公司如Google、Instagram、Spotify等都在使用Python."
        ),
        "error_test": ""
    }