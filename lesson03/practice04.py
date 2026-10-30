class BankAccount:
    def depojit(self, amount):
        self.balance += amount

account = BankAccount()

account.balance = 5000

account.depojit(3000)

print(account.balance)