python_students = [
    "Alice", "Bob", "Charlie", "Diana", "Eve"
]

java_students = [
    "Bob", "Diana", "Frank", "Grace"
]

a = set(python_students)
b = set(java_students)

print(f"同时学两门课的学生：{a & b}")   ## 交运算
print(f"所有学生：{a | b}")  ## 并运算
## print(f"所有学生：{list(set(python_students + java_students))}")     ## set特性：去重
print(f"只学Python不学Java的学生：{a - b}")  ## 差运算
print(f"只学一门课的学生：{a ^ b}")      ## 对称差运算