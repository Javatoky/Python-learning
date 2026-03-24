"""DocMind 数据模型"""
import hashlib
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


class DocMindError(Exception):
    """所有业务异常的基类"""
    pass


class DocumentNotFoundError(DocMindError):
    """文档未找到"""
    def __init__(self, doc_id: str):
        self.doc_id = doc_id
        super().__init__(f"文档 '{doc_id}' 不存在")


class UnsupportedFormatError(DocMindError):
    """不支持的文件格式"""
    def __init__(self, extension: str, supported: list[str]):
        self.extension = extension
        self.supported = supported
        super().__init__(
            f"不支持 '{extension}' 格式，支持: {', '.join(supported)}"
        )

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
            "doc_id": self.doc_id,
            "index": self.index,
            "content": self.content,
            "char_count": self.char_count,
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
        return Path(self.filename).suffix

    def chunk(self, chunk_size: int = 200) -> list[DocumentChunk]:
        """将文档按句号分块"""
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
                    doc_id=self.doc_id,
                ))
                idx += 1
                current = sentence
            else:
                current += " " + sentence

        if current.strip():
            self.chunks.append(DocumentChunk(
                content=current.strip(),
                index=idx,
                doc_id=self.doc_id,
            ))

        return self.chunks

    def to_dict(self) -> dict:
        return {
            "doc_id": self.doc_id,
            "filename": self.filename,
            "char_count": self.char_count,
            "content_hash": self.content_hash,
            "created_at": self.created_at,
            "chunk_count": len(self.chunks),
        }

    @classmethod
    def from_file(cls, filepath: str | Path) -> "Document":
        path = Path(filepath)
        content = path.read_text(encoding="utf-8")
        return cls(filename=path.name, content=content)