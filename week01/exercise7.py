text = """
Python is a great programming language.
Python is easy to learn.
Python is widely used in web development, data science, and AI.
Learning Python is fun and rewarding.
"""

text = text.lower() ##lower() 方法将字符串中的所有大写字母转换为小写字母，但是不会在原字符串上进行修改，而是返回一个新的字符串
word_list = text.split()    ## split() 方法将字符串根据空格（默认）或指定的分隔符（如逗号、冒号等）分割成多个子字符串
for word in word_list:
    word.strip(".,!?:;")    ## strip() 方法用于移除字符串首尾的指定字符（默认是空格），但是不会在原字符串上进行修改，而是返回一个新的字符串,类似Java的trim()方法

word_dict = {}
for word in word_list:
    word_dict[word] = word_dict.get(word, 0) + 1

word_sort = sorted(word_dict.items(), key=lambda x: x[1], reverse=True) ## sorted() 函数返回一个新的列表，而不是原来的dict，因为这个导致了很多错误……
sorted_list = []
for element in word_sort:
    sorted_list.append(element[0])
print(f"出现次数前五的单词：{sorted_list[:5]}")

word_no_repeat_count = 0
for element in word_sort:
    if element[1] == 1:
        word_no_repeat_count += 1
print(f"不重复的单词数量：{word_no_repeat_count}")

## 用split方法指定一些句子结束的标点符号实现按句子的分块，
# 然后用列表存储每个块（后续可以对每个块进行单词统计，比如用之前的方法分割单词，去除标点符号等），
# 用一个大列表存储所有块。