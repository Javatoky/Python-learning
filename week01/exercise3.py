numbers = [5, 2 ,8, 1, 9, 3, 7, 4, 6]

print(f"列表长度：{len(numbers)}")
print(f"第一个元素：{numbers[0]}")
print(f"最后一个元素：{numbers[-1]}")
print(f"前三个元素：{numbers[:3]}")
print(f"后三个元素：{numbers[-3:]}")
print(f"反转后的元素：{numbers[::-1]}")

numbers.sort()  ## 直接将原列表排序，而不会返回新的列表
print(f"排序后的元素：{numbers}")

print(f"最大元素：{max(numbers)}")
print(f"最小元素：{min(numbers)}")
print(f"总和：{sum(numbers)}")