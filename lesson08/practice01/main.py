class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def show_status(self):
        print(f"{self.name}：{self.speed}km/h")

    def accelerate(self, amount):
        if amount <= 0:
            return

        self.speed += amount

class Car(Vehicle):
    def honk(self):
        print(f"{self.name}：プップー！")

class Bicycle(Vehicle):
    def ring_bell(self):
        print(f"{self.name}：チリンチリン！")

car = Car("自動車", 40)
bicycle = Bicycle("自転車", 15)

car.show_status()
bicycle.show_status()
car.accelerate(20)
bicycle.accelerate(5)
car.show_status()
bicycle.show_status()
car.honk()
bicycle.ring_bell()
