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

class BankAccount:
    def __init__(self, account_id: str, balance: float = 0):
        self.account_id = account_id
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError()
        self.balance += amount
    
    def withdraw(self,amount: float):
        if amount <= 0:
            raise InvalidAmountError()
        elif self.balance < amount:
            raise InsufficientFundsError(amount, self.balance)
        else:
            self.balance -= amount
    
    def __str__(self):
        return f"Account(id: {self.account_id}, balance: {self.balance})"

class Bank:
    def __init__(self):
        self.account_collection = {}

    def create_account(self, account_id: str, initial_balance: float = 0) -> BankAccount:
        new_account = BankAccount(account_id, initial_balance)
        self.account_collection[account_id] = new_account
        return new_account

    def get_account(self, account_id: str) -> BankAccount:
        if account:=self.account_collection.get(account_id, None):
           return account 
        else:
           raise AccountNotFoundError(account_id)
    
    def transfer(self, from_id: str, to_id: str, amount: float):
        if amount <= 0:
            raise InvalidAmountError()
        try:
            from_account = self.get_account(from_id)
            to_account = self.get_account(to_id)
            from_account.withdraw(amount)
        except AccountNotFoundError:
            raise
        except InsufficientFundsError:
            raise
        else:
            to_account.deposit(amount)

def test():
    """存款"""
    def test_deposit(bank: Bank, id: str, amount: float):
        try:
            account = bank.get_account(id)
        except AccountNotFoundError as e:
            print(e)
        else:
            try:
                account.deposit(amount)
            except InvalidAmountError as e:
                print(e)
            else:
                print("存款成功！")

    """取款"""
    def test_withdraw(bank: Bank, account_id: str, amount: float):
        try:
            account = bank.get_account(account_id)
            account.withdraw(amount)
        except InvalidAmountError as e:
            print(e)
        except AccountNotFoundError as e:
            print(e)
        except InsufficientFundsError as e:
            print(e)
        else:
            print("取款成功！")
        
    """转账"""
    def test_transfer(bank: Bank, from_id: str, to_id: str, amount: float):
        try:
            bank.transfer(from_id, to_id, amount)
        except InvalidAmountError as e:
            print(e)
        except AccountNotFoundError as e:
            print(e)
        except InsufficientFundsError as e:
            print(e)
        else:
            print("转账成功! ")

    """测试开始"""         
    bank = Bank()
    test_accounts_data = [
        ("ACC001", 1000.0),
        ("ACC002", 500.0), 
        ("ACC003", 2000.0),
    ]

    test_ids = []
    for account_id, initial_balance in test_accounts_data:
        bank.create_account(account_id, initial_balance)
        test_ids.append(account_id)
    
    print("=== 测试开始 ===")
    
    print("\n--- 初始账户状态 ---")
    for account_id in test_ids:
        account = bank.get_account(account_id)
        print(account)
    
    print("\n--- 测试存款 ---")
    test_deposit(bank, test_ids[0], 500.0)
    test_deposit(bank, test_ids[1], 300.0)
    
    print("\n--- 测试无效存款 ---")
    test_deposit(bank, test_ids[0], -100.0)
    
    print("\n--- 测试取款 ---")
    test_withdraw(bank, test_ids[0], 200.0)
    
    print("\n--- 测试余额不足 ---")
    test_withdraw(bank, test_ids[1], 1000.0)
    
    print("\n--- 测试无效取款 ---")
    test_withdraw(bank, test_ids[0], -50.0)
    
    print("\n--- 测试转账 ---")
    print("转账前:")
    print(bank.get_account(test_ids[0]))
    print(bank.get_account(test_ids[1]))
    
    test_transfer(bank, test_ids[0], test_ids[1], 300.0)
    
    print("\n--- 测试无效转账 ---")
    test_transfer(bank, test_ids[0], "NONEXISTENT", 100.0)
    test_transfer(bank, test_ids[1], test_ids[0], 10000.0)
    test_transfer(bank, test_ids[0], test_ids[1], -50.0)
    
    print("\n--- 最终账户状态 ---")
    for account_id in test_ids:
        account = bank.get_account(account_id)
        print(account)

if __name__ == "__main__":
    test()
    