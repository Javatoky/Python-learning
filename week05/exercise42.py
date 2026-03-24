from models_for_exercise import Document, DocumentNotFoundError


class DocumentStore:
    

    def __init__(self):
        self.doc_dict: dict = {}

    def add(self, doc: Document):
        if self.doc_dict.get(doc_id:=doc.doc_id) is None:
            self.doc_dict[doc_id] = doc
            print(f"存入成功！")
        else:
            print(f"文档id已存在：{doc_id}")

    def remove(self, doc_id: str):
        try:
            self.doc_dict.pop(doc_id)
        except KeyError:
            raise DocumentNotFoundError(doc_id)
        
    def get(self, doc_id: str):
        if doc:=self.doc_dict.get(doc_id):
            return doc
        else:
            raise DocumentNotFoundError(doc_id)
        
    def __len__(self):
        return len(self.doc_dict)
    
    def __iter__(self):
        return iter(self.doc_dict.values())
    
    def __contains__(self, item: object):
        if isinstance(item, str):
            return item in self.doc_dict.keys()
        else:
            return False