from pathlib import Path


class FileProcessor:
    def __init__(self, filepath: str):
        self.file = Path(filepath)
        self.stats = {
            "line_count" : 0,
            "word_count" : 0,
            "char_count" : 0
        }
        self.closed = True


    def __enter__(self):
        self.closed = False
        self._reader = open(self.file, "r", encoding = "utf-8")
        self._lines = iter(self._reader)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self._reader.close()
        self.closed = True
        return False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        for line in self._lines:
            if line:=line.strip():
                self.stats["line_count"] += 1
                self.stats["word_count"] += len(line.split())            
                self.stats["char_count"] += len(line)
                return line
            else:
                continue
        raise StopIteration