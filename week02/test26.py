import functools


def compose(*functions):
    def multifunction(*args, **kwargs):
        flag = -1
        def run_functions():
            nonlocal flag
            flag += 1
            if flag == (len(functions)-1):
                return functions[flag](*args, **kwargs)
            else:
                return functions[flag](run_functions())
        return run_functions()
    return multifunction
# 书写递归函数，递归本质上就是函数自己调用自己，所以判断什么时候自调用什么时候执行最终操作是关键，这里是用flag做指针判定
add_one = lambda x: x + 1
double = lambda x: x * 2
to_str = lambda x: f"结果是{x}"
pipeline = compose(to_str, double, add_one)
print(pipeline(5))   # "结果是12"  (5 → 6 → 12 → "结果是12")，这里要注意函数的调用顺序

def pipe(value, *functions):
    for function in functions:
        value = function(value)
    return value
result = pipe(
       "  Hello, World!  ",
       str.strip,
       str.lower,
       lambda s: s.replace(",", ""),
       str.split
   )
print(result)   # ['hello', 'world!']

def memoize(func):
    # 函数的属性
    memo = {}
    count = {
            'hits': 0,
            'missed': 0
        }
    @functools.wraps(func)
    def wrapper(*args):
          
        if args in memo:
            print(f"  ⚡ 命中缓存: {func.__name__}{args}")
            count["hits"] += 1
            return memo[args]
        result = func(*args)
        memo[args] = result
        print(f"  💾 计算: {func.__name__}{args} = {result}")
        count["missed"] += 1
        return result
        
    def cache_info():
        return count    # 闭包，可以访问count变量
    wrapper.cache_info = cache_info    # 函数是一等公民，也是对象可以有自己的属性，这里把cache_info函数外部绑定给wrapper函数，外部通过装饰器，将expensive指向wrapper，所以expensive就可以调用这个方法
    return wrapper

@memoize
def expensive(n):
   return n ** 2
   
expensive(5)   # 计算
expensive(5)   # 缓存命中
expensive(3)   # 计算
expensive(5)   # 缓存命中
print(expensive.cache_info())   # {"hits": 2, "misses": 2}

piped_result = pipe(
    '   I am Javatoky, a student who is learning Python.That is too interesting!   ',
    str.lower,
    # lambda x: x.strip(".,!?:;"),  strip()只处理收尾的标点，这只处理了收尾的标点
    lambda x: x.replace('!', '').replace('.', '').replace(',', ''),     #使用replace可以替换字符串中的所有标点
    str.split,
    lambda x: list(set(x)),
    lambda x: sorted(x, key = len)
)
print(piped_result)