class DatabaseConnection:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connected = False
        self.queries = []
    
    def __enter__(self):
        self.connected = True
        print(f"连接到 {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f"断开 {self.db_name} 连接")
        self.connected = False
        if exc_value is not None:
            print(f"事务回滚：{exc_value}")
            return False
        print("事务提交")
        return False

    def execute(self, sql: str):
        self.queries.append(sql)
        