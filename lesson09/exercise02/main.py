from object_programming.lesson09.exercise02.car import Car
from object_programming.lesson09.exercise02.bicycle import Bicycle

car = Car(800, 500)
bicycle = Bicycle(300)

print(f"{car.name}（2時間）：{car.calculate_fee(2)}円")
print(f"{car.name}（4時間）：{car.calculate_fee(4)}円")

print(f"{bicycle.name}（2時間）：{bicycle.calculate_fee(2)}円")
print(f"{bicycle.name}（4時間）：{bicycle.calculate_fee(4)}円")