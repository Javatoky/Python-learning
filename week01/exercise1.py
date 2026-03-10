import os
import platform
import sys

print(f"操作系统名称：{platform.system()}")
print(f"操作系统版本：{platform.version()}")
print(f"机器架构：{platform.machine}")
print(f"Python实现：{platform.python_implementation()}")
print(f"当前用户的HOME目录：{os.path.expanduser('~')}")
for i, path in enumerate(sys.path): ##Python用冒号开始代码块
    print(f"{i}.{path}")
## Python的for循环语法遵循“for variable in iterable的格式
## 其中variable是循环变量，iterable是可迭代对象（如列表、元组、字符串等）
## enumerate() 将可遍历对象（如列表、元组等）转换成一个枚举对象
## 这个枚举对象生成 (index, value) 形式的元组序列
## index 是元素的索引号（从0开始），value 是对应的元素值 （索引-值对为一个元组（离散数学））
## 所以 for i, path in enumerate(sys.path): 实际上是：同时解包每个元组到两个变量：i（索引）和 path（实际路径）