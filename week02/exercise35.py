from dataclasses import FrozenInstanceError, dataclass, field
from datetime import datetime


@dataclass
class Config:
    app_name: str
    version: str
    debug: bool = False
    port: int = 8000
    allowed_origins: list[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: dict) -> "Config":
        """从字典创建（忽略未知字段）"""
        return cls(app_name = data.get("app_name"), version = data.get("version"), debug = data.get("debug"), port = data.get("port", 8000), allowed_origins = data.get("allowed_origins", []))
        

@dataclass
class APIResponse:
    success: bool
    data: dict | list | None = None
    error: str | None = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    @classmethod
    def ok(cls, data) -> "APIResponse":
        """快捷创建成功响应"""
        return cls(success=True, data=data)
    
    @classmethod
    def fail(cls, error: str) -> "APIResponse":
        """快捷创建失败响应"""
        return cls(success=False, error=error)

@dataclass(frozen = True)
class Point:
    x: float = field(default = 0.0)     # default是默认值（一般处理不可变变量的初始化），default_factory是默认函数（一般用来处理可变变量）
    y: float = field(default = 0.0)


def test():
    print(Config.from_dict({"app_name": "DocMind", "version": "0.1", "debug": True, "unknown_field": "xxx"}))
    print(APIResponse.ok({"users": ["Alice", "Bob"]}))
    print(APIResponse.fail("Not Found"))
    point1 = Point(5, 25)
    try:
        point1.x = 3
    except FrozenInstanceError:
        print("坐标不可更改！")
    point2 = Point(5, 25)
    print(point1 == point2)     # 自动实现__eq__，判定两个实例能否相等
    test_dict = {
        point1 : "my_birth"
    }
    print(test_dict)    # frozen自动实现了__hash__，使Point实例可以做键

if __name__ == "__main__":
    test()


