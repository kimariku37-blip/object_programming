class Drink:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def sell_one(self):
        if self.__stock == 0:
            return False

        self.__stock -= 1
        return True


class VendingMachine:
    def __init__(self, drink):
        self.drink = drink

    def buy(self, money):
        if money < self.drink.get_price():
            print("お金が足りません。")
            return

        if self.drink.sell_one():
            print(f"{self.drink.name}を購入しました！")
        else:
            print("売り切れです。")


tea = Drink("お茶", 120, 2)

machine = VendingMachine(tea)

machine.buy(100)
machine.buy(120)
machine.buy(150)
machine.buy(120)

print(f"{tea.name}の在庫：{tea.get_stock()}本")