import functools


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(result)
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
        for position in args:
            if position <= 0 :
                print("存在非正数")
                return None
        else:
            result = func(*args, **kwargs)
        print(result)
    return wrapper
@validate_positive
def calculate_area(width, height):
   return width * height
calculate_area(3, 5)
calculate_area(-1, 3)
calculate_area(0, 7)
calculate_area(3.8, -1.7)
