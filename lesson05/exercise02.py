class Product:
    def __init__(self, name, stock, capacity):
        self.name = name
        self.__stock = stock
        self.__capacity = capacity

    def get_stock(self):
        return self.__stock

    def sell(self, quantity):
        if quantity <= 0:
            return

        if quantity > self.__stock:
            return

        self.__stock -= quantity

    def restock(self, quantity):
        if quantity <= 0:
            return

        if self.__stock + quantity > self.__capacity:
            return

        self.__stock += quantity

    def is_low_stock(self):
        return self.__stock <= 5


product = Product("ノート", 8, 20)

print(f"{product.name}の在庫：{product.get_stock()}個")

product.sell(4)

print(f"{product.name}の在庫：{product.get_stock()}個")

if product.is_low_stock():
    print("在庫が少なくなっています。")

product.restock(10)

print(f"{product.name}の在庫：{product.get_stock()}個")

product.restock(10)

print(f"{product.name}の在庫：{product.get_stock()}個")

product.sell(20)

print(f"{product.name}の在庫：{product.get_stock()}個")
