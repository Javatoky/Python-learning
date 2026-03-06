import functools
import time


def slow_down(seconds: float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            result  = func(*args,*kwargs)
            return result
        return wrapper
    return decorator

@slow_down(0.5)
def say(msg):
   print(msg)
say("hello")   # 等待 0.5 秒后打印

def require_fields(*fields: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key_not_exist = []
            for key in fields:
                if key not in args[0]:
                    key_not_exist.append(key)
            if len(key_not_exist) == 0:
                return func(*args, **kwargs)
            else:
                print(f"缺少{key_not_exist}字段")
                return None
        return wrapper
    return decorator

@require_fields("name", "age", "email")
def process_user(data: dict):
    print(f"处理用户: {data['name']}")
    return True
process_user({"name": "Alice", "age": 25, "email": "a@b.com"})  # 正常
process_user({"name": "Bob"})   # 打印缺少 age, email，返回 None

# Java的注解是解释代码的作用，它属于是提示JVM的一种方式，告诉编译器这段代码的作用或告诉JVM应该要做什么，并不会影响实际的代码
# python的装饰器实际上是影响代码的，它属于一种语法糖