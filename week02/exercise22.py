words = ["Python", "is", "a", "great", "language", "for", "AI"]
length_sorted = sorted(words, key = lambda x: len(x))
length_reversed = sorted(words, key = lambda x : -len(x))
last_letter_sorted = sorted(words, key = lambda x: x[-1])
print(length_sorted)
print(length_reversed)
print(last_letter_sorted)

str_numbers = ["10", "3", "25", "7", "100", "1"]
numbers_sorted = sorted(str_numbers, key = int)
print(numbers_sorted)

records = [
       {"name": "Alice", "math": 90, "english": 88},
       {"name": "Bob", "math": 78, "english": 92},
       {"name": "Charlie", "math": 85, "english": 85},
   ]
math_sorted = sorted(records, key = lambda x: -x["math"])
total_sorted = sorted(records, key = lambda x: -(x['math'] + x['english']))
top_of_english = max(records, key = lambda x: x['english'])
print(math_sorted)
print(total_sorted)
print(top_of_english['name'])

result = filter(lambda x: x % 3 == 0 and x % 5 != 0, range(1, 51))
print(list(result))   # 和sorted不同，和map相同，返回迭代器，需要用list包装