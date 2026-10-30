class Wallet:
    def add_money(self, amount):
        self.money += amount

wallet = Wallet()

wallet.money = 1000

wallet.add_money(500)
wallet.add_money(200)

print(wallet.money)
