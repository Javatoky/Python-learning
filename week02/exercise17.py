def calculate_stats(numbers: list[int | float]) -> dict:
    """
    接收一个数字列表，返回字典包含：
    {"count": 数量, "sum": 总和, "avg": 平均, "max": 最大, "min": 最小}
    """
    if not numbers:
        return {"count": 0, "sum": 0, "avg": 0, "max": None, "min": None}
    
    count = len(numbers)
    total_sum = sum(numbers)
    avg = total_sum / count
    max_val = max(numbers)
    min_val = min(numbers)
    
    return {
        "count": count,
        "sum": total_sum,
        "avg": avg,
        "max": max_val,
        "min": min_val
    }


def is_valid_email(email: str) -> bool:
    """
    简单检查：包含恰好一个 @，@ 后面包含至少一个 .，@ 前面长度 >= 1
    """
    # 检查是否包含 @
    if "@" not in email:
        return False
    
    # 检查是否包含恰好一个 @
    if email.count("@") != 1:
        return False
    
    # 分割 @ 前后部分
    parts = email.split("@")
    if len(parts) != 2:
        return False
    
    local_part, domain_part = parts
    
    # 检查 @ 前面长度 >= 1
    if len(local_part) == 0:
        return False
    
    # 检查 @ 后面包含至少一个 .
    if "." not in domain_part:
        return False
    
    return True


def fizzbuzz(n: int) -> list[str]:
    """
    返回 1 到 n 的 FizzBuzz 结果列表：
    - 能被 3 整除："Fizz"
    - 能被 5 整除："Buzz"
    - 能被 3 和 5 整除："FizzBuzz"
    - 其他：数字本身（字符串）
    """
    result = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    
    return result


# 测试代码
if __name__ == "__main__":
    # 测试 calculate_stats
    print("Testing calculate_stats:")
    stats_result = calculate_stats([4, 8, 15, 16, 23, 42])
    print(stats_result)
    
    # 测试 is_valid_email
    print("\nTesting is_valid_email:")
    print(is_valid_email("alice@gmail.com"))  # True
    print(is_valid_email("bob@com"))          # False
    print(is_valid_email("@x.com"))           # False
    print(is_valid_email("a@@b.com"))         # False
    
    # 测试 fizzbuzz
    print("\nTesting fizzbuzz:")
    fb_result = fizzbuzz(15)
    print(fb_result)