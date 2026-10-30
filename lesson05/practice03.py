class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock

    def get_stock(self):
        return self.__stock

    def restock(self, amount):
        if amount <= 0:
            return

        self.__stock += amount

    def sell(self, amount):
        if amount <= 0:
            return

        if amount > self.__stock:
            return

        self.__stock -= amount

product = Product("ノート", 5)

print(f"{product.name}の在庫：{product.get_stock()}個")

product.sell(3)

print(f"{product.name}の在庫：{product.get_stock()}個")

product.sell(5)

print(f"{product.name}の在庫：{product.get_stock()}個")

product.restock(10)

print(f"{product.name}の在庫：{product.get_stock()}個")

product.restock(-2)

print(f"{product.name}の在庫：{product.get_stock()}個")