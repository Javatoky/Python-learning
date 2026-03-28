def lines_from_string(text: str):
    while True:
        if text:
            line, separator, text = text.partition("\n")
            yield line.strip()
        else:
            return 

def skip_empty(lines):
    for line in lines:
        if line:
            yield line

def skip_comments(lines, prefix: str = "#"):
    for line in lines:
        if not line.startswith(prefix):
            yield line

def numbered(lines, start = 1):
    for line in lines:
        yield (start, line)
        start += 1

def pipeline(text: str, comment_prefix: str = "#"):
    return list(numbered(skip_comments(skip_empty(lines_from_string(text)), comment_prefix)))