def format_name(*parts: str, sep: str = " ") -> str:
    """
    接收任意数量的名字部分，用分隔符拼接
    """
    return sep.join(parts)


def create_config(**kwargs) -> dict:
    """
    接收任意关键字参数，返回字典。
    - 所有键转为小写
    - 所有字符串值去除首尾空格
    - 添加一个 "_created" 键，值为 True
    """
    result = {}
    
    for key, value in kwargs.items():
        lower_key = key.lower()
        
        # 如果值是字符串，则去除首尾空格
        if isinstance(value, str):
            result[lower_key] = value.strip()
        else:
            result[lower_key] = value
    
    # 添加 _created 键
    result["_created"] = True
    
    return result


def safe_divide(a, b, *, default=None):
    """
    a 除以 b，如果 b 为 0 返回 default
    注意：default 是仅关键字参数（在 * 后面）
    """
    if b == 0:
        return default
    return a / b


# 测试代码
if __name__ == "__main__":
    # 测试 format_name
    print("Testing format_name:")
    print(repr(format_name("张", "三")))  # "张 三"
    print(repr(format_name("Alice", "Bob", "Charlie", sep=", ")))  # "Alice, Bob, Charlie"
    print(repr(format_name()))  # ""
    
    # 测试 create_config
    print("\nTesting create_config:")
    config_result = create_config(Name="  Alice  ", AGE=25, City=" Beijing ")
    print(config_result)  # {'name': 'Alice', 'age': 25, 'city': 'Beijing', '_created': True}
    
    # 测试 safe_divide
    print("\nTesting safe_divide:")
    print(safe_divide(10, 3))  # 3.333...
    print(safe_divide(10, 0))  # None
    print(safe_divide(10, 0, default=0))  # 0