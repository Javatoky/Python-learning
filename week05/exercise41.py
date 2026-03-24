from pathlib import Path


class LineReader:
    def __init__(self, filepath: Path):
        with open(filepath, "r", encoding = "utf-8") as f:
            self.text = f.read().strip()
        
    def __iter__(self):
        return LineReaderIterator(self.text)
    
class LineReaderIterator:
    def __init__(self, text: str):
        self.text = text
    def __next__(self):
        while True:
            if self.text:
                line, separator, self.text = self.text.partition("\n")
                if line:=line.strip():
                    return line
            else:
                raise StopIteration