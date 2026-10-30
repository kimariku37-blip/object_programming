class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            return

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            return

        if amount > self.__balance:
            return

        self.__balance -= amount

account = BankAccount("田中", 5000)

print(f"{account.owner}の残高：{account.get_balance()}円")

account.deposit(2000)

print(f"{account.owner}の残高：{account.get_balance()}円")

account.withdraw(3000)

print(f"{account.owner}の残高：{account.get_balance()}円")

account.withdraw(5000)

print(f"{account.owner}の残高：{account.get_balance()}円")

account.deposit(-100)

print(f"{account.owner}の残高：{account.get_balance()}円")

account.withdraw(0)

print(f"{account.owner}の残高：{account.get_balance()}円")