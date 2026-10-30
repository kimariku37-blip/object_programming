class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):    
        print(f"商品名：{self.name}")
        print(f"価格：{self.price}円")
        print(f"在庫：{self.stock}個")

product = Product("ゲーミングPC", 200000, 10)

product.show_info()