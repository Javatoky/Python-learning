import asyncio


class AsyncDatabase:
    def __init__(self, name: str):
        self.name = name
        self.queries = []
        self.connected = False

    async def __aenter__(self):
        await asyncio.sleep(0.1)
        self.connected = True
        print(f"连接到 {self.name}")
        return self
    
    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await asyncio.sleep(0.05)
        self.connected = False
        print(f"断开 {self.name}")
        return False
    
    async def execute(self, sql: str):
        await asyncio.sleep(0.05)
        self.queries.append(sql)
        return f"{sql} → ok"
    
class AsyncCounter:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    # __aiter__必须是普通函数，返回一个异步协程迭代器对象
    def __aiter__(self):
        return AsyncCounterIterator(self.start, self.stop)
    
class AsyncCounterIterator:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    # 迭代器类也要实现__iter__方法，因为这样可以直接iter()调用，只不过是一次性的，相当于一体式迭代器
    def __aiter__(self):
        return self

    # __anext__必须是异步函数
    async def __anext__(self):
        if self.start >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.05)
        value = self.start
        self.start += 1
        return value
    
    
            