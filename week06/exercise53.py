from typing import Protocol


class SearchBackend(Protocol):
    def search(self, query: str, top_k: int) -> list[dict]: ...
    
    def index(self, doc_id: str, chunks: list[str]) -> int: ...

class SimpleSearchBackend:
    def __init__(self):
        self._index: dict[str, list[str]] = {}
    
    def index(self, doc_id: str, chunks: list[str]) -> int:
        self._index[doc_id] = chunks
        return len(chunks)
    
    def search(self, query: str, top_k: int) -> list[dict]:
        results: list[dict] = []
        count = 0
        for doc_id, chunks in self._index.items():
            for chunk in chunks:
                if count >= top_k:
                    break
                if query in chunk:
                    results.append(
                        {
                            "doc_id": doc_id, "chunk": chunk, "score": 1.0
                        }
                    )
                    count += 1
        return results
    
def search_documents(backend: SearchBackend, query: str, top_k: int) -> list[dict]:
    return backend.search(query, top_k)

