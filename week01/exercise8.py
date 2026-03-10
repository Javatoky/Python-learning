user_input = ""
if not user_input:
    print("输入为空")

data = []
if not data:
    print("没有数据")

temperatrue = 35
weather = "热" if temperatrue >=30 else "适中" if temperatrue >=20 else "冷"
print(weather)

bool(0)# False
bool("")# False
bool(" ")# True       # 注意：有一个空格
bool([])# False
bool([0])# True       # 注意：列表里有一个元素 0
bool(None)# False
bool("False")# True   # 注意：这是字符串