E = 2.71828

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n
    
def fibonacci(n: int) -> list[int]:
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        result = fibonacci(n-1)
        result.append(result[-1] + result[-2])
        return result
    
if __name__ == "__main__":
    print(f"my_math直接运行")

