## 思考题在注释中
a = 25
b = 520.1314
c = "python "
d = True

print(f"a = {a}，类型为{type(a)}")
print(f"b = {b}，类型为{type(b)}")
print(f"c = {c}，类型为{type(c)}")
print(f"d = {d}，类型为{type(d)}")
print(f"None = {None}，类型为{type(None)}")

print(f"2 ** 100 = {2 ** 100}")
## 在Java和C中会发生精度损失
# （除非Java中使用BigDecimal等类,C语言中使用大整数库），
# Python中会自动调整，将整数调整为长整数，这是它相比于C、Java的优势

print(f"7 / 2 = {7 / 2}")
print(f"7 // 2 = {7 // 2}") # // 是整数除法，向下取整
print(f"7 % 2 = {7 % 2}")

e = "is a great language"
print(f"c + e = {c + e}")
f = "ha" * 3
print(f"{f}")

## True + True 的结果为 2，因为 True 被解释为 1，False 被解释为 0，是int的子类