from object_programming.lesson09.exercise02.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,  hourly_rate, insurance_fee):
        super().__init__("自動車", hourly_rate)
        self.insurance_fee = insurance_fee

    def calculate_fee(self, hours):
        base_fee = super().calculate_fee(hours)
        total = base_fee + self.insurance_fee
        return total

    