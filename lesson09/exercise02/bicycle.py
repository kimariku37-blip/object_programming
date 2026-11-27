from object_programming.lesson09.exercise02.vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, hourly_rate):
        super().__init__("自転車", hourly_rate)

    def calculate_fee(self, hours):
        base_fee = super().calculate_fee(hours)
        total = base_fee

        if hours >= 3:
            total -= 200

        return total