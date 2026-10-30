class Car:
    def accelerate(self, speed_increase):
        self.speed += speed_increase

car1 = Car()
car2 = Car()

car1.speed = 20
car2.speed = 50

car1.accelerate(30)
car2.accelerate(10)

print(car1.speed)
print(car2.speed)