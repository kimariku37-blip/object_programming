class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}の残高：{self.balance}円")

    def deposit(self, amount):
        self.balance += amount

    def transfer(self, target, amount):
            if self.balance < amount:
                 print("残金が不足しているため、送金できません")
                 return
            self.balance -= amount
            target.deposit(amount)
            print(f"{self.owner}から{target.owner}へ{amount}円送金しました。")

account1 = BankAccount("田中", 5000)
account2 = BankAccount("佐藤", 2000)

account1.show_balance()
account2.show_balance()

account1.transfer(account2, 1500)

account1.show_balance()
account2.show_balance()

account2.transfer(account1, 4000)

account1.show_balance()
account2.show_balance()