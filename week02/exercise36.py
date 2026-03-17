"""DocMind 数据模型 - 用 dataclass 设计"""
import hashlib
import json
import os
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


# 自定义异常
class DocumentNotFound(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(f"错误：{msg}")

@dataclass
class DocumentChunk:
    """文档块"""
    content: str
    index: int
    doc_id: str
    chunk_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    
    @property
    def char_count(self) -> int:
        return len(self.content)
    
    @property
    def word_count(self) -> int:
        return len(self.content.split())
    
    def to_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "index": self.index,
            "doc_id": self.doc_id,
            "content": self.content,
            "char_count": self.char_count,      # 重写to_dict时注意要把@property的值带上！！！否则__dict__时不会加上这些属性
            "word_count": self.word_count,
        }


@dataclass
class Document:
    """文档"""
    filename: str
    content: str
    doc_id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    chunks: list[DocumentChunk] = field(default_factory=list, repr=False)
    
    @property
    def content_hash(self) -> str:
        return hashlib.sha256(self.content.encode()).hexdigest()[:16]
    
    @property
    def char_count(self) -> int:
        return len(self.content)
    
    @property
    def extension(self) -> str:
        return Path(self.filename).suffix   # 用Path的suffix更一致（实例方法）

    def chunk(self, chunk_size: int = 20) -> list[DocumentChunk]:
        """将文档分块"""
        sentences = self.content.replace("\n", " ").split(".")
        sentences = [s.strip() + "." for s in sentences if s.strip()]
        
        self.chunks = []
        current = ""
        idx = 0
        
        for sentence in sentences:
            if len(current) + len(sentence) > chunk_size and current:
                self.chunks.append(DocumentChunk(
                    content=current.strip(),
                    index=idx,
                    doc_id=self.doc_id
                ))
                idx += 1
                current = sentence
            else:
                current += " " + sentence
        
        if current.strip():
            self.chunks.append(DocumentChunk(
                content=current.strip(),
                index=idx,
                doc_id=self.doc_id
            ))
        
        return self.chunks
    
    def to_dict(self) -> dict:
        return {
            "filename": self.filename,
            "content": self.content,
            "doc_id": self.doc_id,
            "create_at": self.created_at,
            "chunks": [chunk.__dict__ for chunk in self.chunks]
            
        }
    
    @classmethod
    def from_file(cls, filepath: Path):
        with open(filepath, "r", encoding = "utf-8", errors = None) as f:
            kwargs = json.load(f)
            try:
                return cls(**kwargs)
            except TypeError:
                print(f"创建失败！")

@dataclass
class QueryResult:
    query: str
    chunks: list[DocumentChunk]
    answer: str | None = None
    
    def to_dict(self) -> dict:
        return {
            "query": self.query,
            "chunks": [chunk.__dict__ for chunk in self.chunks],
            "answer": self.answer
        }

class DocumentStore:
    def __init__(self):
        self.store_dict: dict = {}

    def add(self, doc: Document) -> str:
        self.store_dict[doc.doc_id] = doc
        return doc.doc_id
    
    def get(self, doc_id: str) -> Document:
        doc = self.store_dict.get(doc_id, None)
        if doc:
            return doc
        else:
            raise DocumentNotFound(f"{doc_id}不存在")
        
    def delete(self, doc_id: str) -> None:
        self.store_dict.pop(doc_id, None)

    def list_all(self) -> list[Document]:
        return self.store_dict.values()
    
    def search_chunks(self, query: str) -> list[DocumentChunk]:
        result = []
        for doc in self.store_dict.values():
            for chunk in doc.chunks:
                if query in chunk.content:
                    result.append(chunk)
        return result
    
    def __len__(self):
        return len(self.store_dict)
    
    def __contains__(self, doc_id: str):
        return doc_id in self.store_dict.keys()

TEST_TEXT_1 = (
    "人工智能（Artificial Intelligence，AI）是计算机科学的一个分支."
    "它致力于创造能够模拟、延伸和扩展人类智能的理论、方法、技术及应用系统."
    "人工智能技术已经在图像识别、语音识别、自然语言处理等领域取得了显著成果."
    "未来，人工智能将在医疗、教育、交通等多个行业发挥重要作用."
)

TEST_TEXT_2 = (
    "Python是一种高级编程语言，由Guido van Rossum于1991年首次发明."
    "Python的设计哲学强调代码的可读性和简洁的语法结构."
    "它广泛应用于Web开发、数据分析、人工智能、科学计算等领域."
    "Python拥有丰富的标准库和第三方库，大大提高了开发效率."
    "许多知名公司如Google、Instagram、Spotify等都在使用Python."
)

TEST_TEXT_3 = (
    "机器学习是人工智能的一个重要分支，专注于算法和统计模型的研发."
    "它使计算机能够在没有明确编程指令的情况下学习和改进."
    "监督学习、无监督学习和强化学习是机器学习的三大主要类型."
    "深度学习作为机器学习的子集，使用神经网络来模仿人脑的学习方式."
    "机器学习在图像识别、语音识别、推荐系统等方面表现优异."
)

# === 测试 ===
if __name__ == "__main__":
    doc1 = Document("ai_introduction.txt", content = TEST_TEXT_1)
    doc2 = Document(
        filename="python_overview.txt", 
        content=TEST_TEXT_2
    )
    
    doc3 = Document(
        filename="ml_basics.txt",
        content=TEST_TEXT_3
    )
    store = DocumentStore()
    store.add(doc1)
    store.add(doc2)
    store.add(doc3)

    doc1.chunk()
    doc2.chunk()
    doc3.chunk()

    query_and_result = QueryResult("人工智能", [])
    query_and_result.chunks = store.search_chunks(query_and_result.query)
    for chunk in query_and_result.chunks:
        print(chunk.content)
