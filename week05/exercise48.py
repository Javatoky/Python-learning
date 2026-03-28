def deep_flatten(data: list | tuple):
    for item in data:
        if isinstance(item, list | tuple):
            yield from deep_flatten(item)
        else:
            yield item
def chunk_generator(text: str, chunk_size: int):
    chunk_content = ""
    while True:
        if text:
            sentence, separator, text = text.partition(".")
            if len(chunk_content) + len(sentence:=(sentence + separator)) > chunk_size:
                yield chunk_content
                chunk_content = sentence
            else:
                chunk_content += sentence
        else:
            if chunk_content:
                yield chunk_content
            break
    
