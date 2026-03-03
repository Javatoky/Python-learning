from typing import Callable


def make_multiplier(factor: int) -> Callable[[int], int]:   # 返回一个参数列表为[int]，返回类型为int的函数
    def new_function(number: int) -> int:
        return factor * number
    return new_function
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))    # 10
print(triple(5))    # 15

def make_accumulator(initial: int = 0):
    total_sum = initial
    def number_plus(number: int):
        nonlocal total_sum
        total_sum += number
        return total_sum
    return number_plus
acc2 = make_accumulator(100)
print(acc2(1))   # 101

def make_logger(prefix: str):
    number = 0
    def request_back(message: str):
        nonlocal number
        number += 1
        return f"{prefix} #{number} {message}"
    return request_back
info = make_logger("INFO")
error = make_logger("ERROR")
print(info("服务器启动"))
print(info("收到请求"))
print(error("连接失败"))
print(info("处理完成"))