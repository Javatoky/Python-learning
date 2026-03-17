from dataclasses import dataclass, field


# 异常类
class BankError(Exception):
    """银行账户异常"""
    pass

class InsufficientFundsError(BankError):
    """余额不足"""
    def __init__(self, amount: float, balance: float):
        self.amount = amount
        self.balance = balance
        super().__init__(f'余额不足：{balance}/{amount}')

class InvalidAmountError(BankError):
    """无效金额"""
    def __init__(self):
        super().__init__(f"金额无效！")

class AccountNotFoundError(BankError):
    """账户不存在"""
    def __init__(self, account_id: str):
        self.account_id = account_id
        super().__init__(f'账户不存在：{account_id}')

# 银行账户类
class BankAccount:
    account_id: str
    owner: str
    _balance: float

    def __init__(self, account_id: str, owner: str, balance: float):
        self.account_id = account_id
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, amount) -> None:
        raise AttributeError


    # 这里注意内部方法使用内部保护属性时，不必调用他的getter方法，直接使用带"_"原保护变量
    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError()
        self._balance += amount
    
    def withdraw(self,amount: float):
        if amount <= 0:
            raise InvalidAmountError()
        elif self._balance < amount:
            raise InsufficientFundsError(amount, self._balance)
        else:
            self._balance -= amount
    
    def transfer_to(self, to_id: str, amount: float):
        if amount <= 0:
            raise InvalidAmountError()
        try:
            to_account = self.account_id
            self.withdraw(amount)
        except AccountNotFoundError:
            raise
        except InsufficientFundsError:
            raise
        else:
            to_account.deposit(amount)

    def __str__(self) -> str:       # 打印的依据（转换为字符串时的内容）
        return f"Account(owner={self.owner}, balance={self._balance})"
    
    def __repr__(self) -> str:
        return f"Account(account_id={self.account_id!r}, owner={self.owner!r}, balance={self._balance!r})"
    
    def __eq__(self, other: object) -> bool:        # 判定实例是否相同的依据
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.account_id == other.account_id
    
    def __lt__(self, other: "BankAccount") -> bool:     # BankAccount类名尚未被定义，需要用引号解决
        return self._balance < other._balance           # 将实例排序、比较的依据（前提是实力都是同一类)
    
    def __bool__(self) -> bool:     # Falsy判定依据
        return self.balance > 0

def test():

    acc1 = BankAccount("ACC001", "张三", 1000.0)
    acc2 = BankAccount("ACC002", "李四", 500.0)
    acc3 = BankAccount("ACC003", "王五", 2000.0)
    acc4 = BankAccount("ACC004", "钱六", 0.0)
    acc5 = BankAccount("ACC001", "宋七", 2000.0)

    acc_list = [acc1, acc2, acc3]
    acc_list = sorted(acc_list, reverse = True)
    print(acc_list)

    if not acc4:
        print(f"{acc4.owner}破产了")

    print(acc1 == acc5)

if __name__ == "__main__":
    test()
    



