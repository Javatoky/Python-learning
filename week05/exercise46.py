def read_lines(filepath):
    with open(filepath, "r", encoding = "utf-8") as f:
        for line in f:
            if line:=line.strip():
                yield line

def count_lines(filepath):
    return len(list(read_lines(filepath)))


