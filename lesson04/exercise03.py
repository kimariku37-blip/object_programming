class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def decrease_stock(self, quantity):
        self.stock -= quantity 

    def show_info(self):
        print(f"商品名:{self.name}")
        print(f"価格:{self.price}円")
        print(f"在庫:{self.stock}個")

class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def show_money(self):
        print(f"{self.name}の所持金：{self.money}円")

    def buy(self, product, quantity):
        total_price = product.price * quantity
        
        if product.stock < quantity:
            print("在庫が不足しているため購入できません。")
            return

        if self.money < total_price:
            print("所持金が不足しているため購入できません。")
            return

        self.money -= total_price
        product.decrease_stock(quantity)

        print(f"{self.name}は{product.name}を{quantity}個購入しました。")
        print(f"合計金額：{total_price}円")

customer = Customer("田中", 10000)
keyboard = Product("キーボード", 3000, 2)
mouse = Product("マウス", 5000, 5)       

customer.show_money()
keyboard.show_info()
mouse.show_info()

print()

customer.buy(keyboard, 2)
print()

customer.buy(mouse, 1)
print()

customer.show_money()
keyboard.show_info()
mouse.show_info()