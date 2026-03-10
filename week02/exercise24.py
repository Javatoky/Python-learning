import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(result)
        return result   # 不能忘记在wrapper中返回值，必须加return func(……)
    return wrapper

@debug
def add(a, b):
    return a + b
@debug
def greet(name, greeting="Hello"):
   return f"{greeting}, {name}!"
add(500, 25)
greet('Javatoky')

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 有一个类型安全问题——如果参数中有字符串，position <= 0 会报 TypeError：
        # for position in args:
        for position in args:
            if isinstance(position, (int, float)) and position <= 0 :   # 用isinstance函数确保是数字
                print("存在非正数")
                return None
        else:
            result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper
@validate_positive
def calculate_area(width, height):
   return width * height
calculate_area(3, 5)
calculate_area(-1, 3)
calculate_area(0, 7)
calculate_area(3.8, -1.7)
