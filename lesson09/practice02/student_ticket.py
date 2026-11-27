from object_programming.lesson09.practice02.ticket import Ticket

class StudentTicket(Ticket):
    def __init__(self, price, discount):
        super().__init__("学生チケット", price)
        self.discount = discount

    def calculate_price(self):
        base_price = super().calculate_price()
        total = base_price - self.discount
        return total