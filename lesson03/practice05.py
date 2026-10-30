class Product:
    def get_half_price(self):
        return self.price / 2

product = Product()
product.price = 2000

product.get_half_price()

half_price = product.get_half_price()

print(half_price)