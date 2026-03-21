import pytest


def fibonacci_gen(n: int):
    """斐波那契生成器"""
    def fibonacci(x: int): 
        if x == 1:
            return 1
        elif x == 2:
            return 1
        else:
            return fibonacci(x-1) + fibonacci(x-2)
    for i in range(1, n+1):
        yield fibonacci(i)

def chunk_iter(items: list, size: int):
    count = 0
    temp = []
    for item in items:
        temp.append(item)
        count += 1
        if count == size:
            yield temp
            count = 0
            temp = []
    if temp:
        yield temp

square_seven_multiple = (x**2 for x in range(1, 101) if x % 7 == 0)




            