class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name}：{self.price}円")

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def show_author(self):
        print(f"著者：{self.author}")


class Food(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def show_expiration(self):
        print(f"賞味期限：{self.expiration_date}")

book = Book("Python入門", 2400, "山田太郎")
food = Food("ヨーグルト", 180, "2026-12-01")

book.show_info()
book.show_author()
food.show_info()
food.show_expiration()