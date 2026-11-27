from object_programming.lesson09.practice02.ticket import Ticket

class PremiumTicket(Ticket):
    def __init__(self, price, extra_fee):
        super().__init__("プレミアムチケット", price)
        self.extra_fee = extra_fee

    def calculate_price(self):
        base_price = super().calculate_price()
        total = base_price + self.extra_fee
        return total
