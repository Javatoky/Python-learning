raw_prices = ["  $19.99 ", "$5.50", " $123.45 ", "$0.99", "  $49.00"]
total_price = sum(filter(lambda x: x>10, map(lambda x: float(x.strip().strip('$')), raw_prices)))
# sum、filter都接受迭代器，不用list
print(total_price)

keys = ["name", "age", "city", "score"]
values = ["Alice", "25", "Beijing", "92.5"]
personal_info = {key: value for key, value in zip(keys, values)}
def try_convert(value: str):
    # if all(feature in ([str(number) for number in range(10)] + ['.']) for feature in value) :  # 不能在推导式中使用append方法，可以用 + 合并
    #    if '.' in value:
    #        convert = float(value)
    #    else:
    #        convert = int(value)
    #    return convert
    # else:
    #    return value
    # 思路正确，但是这每次判断都会重新创建列表，而且不处理负数，属于是想复杂了

    # 其实是没招了，毕竟还没有“EAFP 原则”的概念，先试着做，出错了再处理
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value
result = dict(map(lambda item: (item[0], try_convert(item[1])), personal_info.items()))     # 这里注意选择dict的items迭代，否则就会迭代键值
print(result)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(map(sum, matrix)))
print(list(map(max, matrix)))