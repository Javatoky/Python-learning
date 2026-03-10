text = """
Python is a great programming language.
Python is easy to learn.
Python is widely used in web development, data science, and AI.
Learning Python is fun and rewarding.
"""

print("=== 词频统计 ===")
word_list = [word.strip(".,!?:;") for word in text.lower().split()]
word_count = {word : word_list.count(word) for word in set(word_list)}
## word_count = {}
## for word in word_list:
##      word_count[word] = word_count.get(word, 0) + 1
word_sort = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
for i, (word, count) in enumerate(word_sort):
    print(f"{i+1}. {word}:{count}次")

print("\n=== 句子分析 ===")
sentence_list = text.lower().replace("\n", "").split(".")
sentence_word_list = [[word.strip(".,!?:;") for word in sentence.split()] for sentence in sentence_list if sentence]
sentence_word_count = [len(sentence) for sentence in sentence_word_list]
for i, (sentence, count) in enumerate(zip(sentence_list, sentence_word_count)):
    print(f"句子{i+1}（{count}个词）：{sentence}")

print("\n=== 词汇分析 ===")
word_length = {word:len(word) for word in set(word_list) if len(word) > 2}
max = max(word_length.values())
min = min(word_length.values())
word_analysis = {
    "最长单词" : "Unknown",
    "最短单词" : "Unknown",
    "词汇量" : len(set(word_list))
}
for word, length in word_length.items():
    if length == max:
        word_analysis["最长单词"] = word
    if length == min:
        word_analysis["最短单词"] = word
for key, value in word_analysis.items():
    print(f"{key}：{value}")

# 思考题：
# 1. 
# 答：差别大，两个数据类型的底层逻辑不同，list 是顺序存储，查询需要遍历，set 是哈希存储，查询只需要 O(1) 时间。

# 2. 
# 答：可能会像Java那样现将数据序列化，然后写入文件，但是要注意对数据的保护，对于数据损坏等情况要求应对措施吧
