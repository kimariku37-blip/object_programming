class Vehicle:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_fee(self, hours):
        return self.hourly_rate * hours