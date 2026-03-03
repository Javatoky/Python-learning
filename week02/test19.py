def analyze_text(text: str) -> tuple[int, int, int]:
    """
    返回：(字符数, 单词数, 行数)
    """
    char_count = len(text)
    word_count = len(text.split())
    line_count = len(text.splitlines())
    
    return (char_count, word_count, line_count)


# 测试用文本
text = """Hello World
Python is great
Let us code"""
char_count, word_count, line_count = analyze_text(text)
print(f"字符数: {char_count}, 单词数: {word_count}, 行数: {line_count}")

def merge_dicts(*dicts: dict) -> dict:
    new_dict = {}
    for single_dict in dicts:
        new_dict.update(single_dict)
    return new_dict
print(merge_dicts({"a": 1}, {"b": 2}, {"a": 3, "c": 4}))

args = [1, 2, 3]
kwargs = {"sep": " + ", "end": " = ?\n"}
print(*args, **kwargs)  # 预测输出是1,2,3,"sep":" + ","end":"= ?\n"
# 预测错了，原因是"sep"关键字在print()函数中是分隔符，"end"是结束符
# 所以结果是"1 + 2 + 3 = ? 
# "