text = """
Python 3.12 was released on October 2, 2023.
Python 3.11 was released on October 24, 2022.
Python 3.10 was released on October 4, 2021.
Contact: support@python.org or admin@python.org
Visit: `https://www.python.org`  or `https://docs.python.org`  
"""
import re

version = re.findall(r'\d+\.\d+',text)
print(version)

emails = re.findall(r'[\w.-]+@[\w.-]+\.[\w]+', text)
print(emails)

urls = re.findall(r'https?://[\w.-]+', text)
print(urls)

year = re.findall(r'\b\d{4}\b', text)     # \b 匹配一个位置，而不是实际的字符,位置的左侧是单词字符，右侧是非单词字符（空格、标点、换行符），或反之，即一边是单词字符，一边是非单词字符，作用是标志分隔
print(year)

words = "the quick brown fox jumps over the lazy dog the fox the".split()

from collections import Counter, defaultdict, namedtuple

word_count = Counter(words)
print("词频统计:", word_count)

most_common = word_count.most_common(3)
print("出现次数最多的3个词:", most_common)

grouped_by_first_letter = defaultdict(list)     # 声明返回默认值为空列表的字典
for word in words:
    grouped_by_first_letter[word[0].upper()].append(word)

print("按首字母分组:")
for letter, word_list in sorted(grouped_by_first_letter.items()):
    print(f"  {letter}: {word_list}")

Student = namedtuple('Student', {'name', 'age', 'score'})   # namedtuple———被命名的元组(名字：字符串， [元组中的元素])

students = [
    Student('Alice', 20, 85),
    Student('Bob', 21, 92),
    Student('Charlie', 19, 78)
]

sorted_students = sorted(students, key=lambda s: s.score, reverse=True)

print("\n按分数降序排列的学生:")
for student in sorted_students:
    print(f"  姓名: {student.name}, 年龄: {student.age}, 分数: {student.score}")