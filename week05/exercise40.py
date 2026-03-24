class MyRange:
    """模仿Python内置range()"""
    def __init__(self, *args: int):
        if (args_length:=len(args)) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif args_length == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif args_length == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("参数数量应为1-3个")
        
        if self.step == 0:
            raise ValueError("步长不能为0！")

        self.length = 0
        start = self.start
        stop = self.stop
        step = self.step
        while True:
            if start >= stop:
                break
            self.length += 1
            start += step

    def __iter__(self):
        return MyRangeIterator(self.start, self.stop, self.step, self.length)
    
    def __len__(self):
        return self.length
            
    
    def __repr__(self):
        return f"MyRange({self.start}, {self.stop}, {self.step})"
    
class MyRangeIterator:
    """MyRange的分离式迭代器类"""
    def __init__(self, start: int, stop: int, step: int, length: int):
        self.start = start
        self.stop = stop
        self.step = step
        self.length = length

    def __next__(self) -> int:
        if self.length <= 0:
            raise StopIteration
        val = self.start
        self.start += self.step
        self.length -= 1
        return val

for i in MyRange(0, 10 ,3):
    print(MyRange(0, 10, 3).length)