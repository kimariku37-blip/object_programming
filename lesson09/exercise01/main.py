class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}は鳴いた！")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}はワンワンと鳴いた！")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}はニャー！と鳴いた！")

animal = Animal("動物")
dog = Dog("ポチ")
cat = Cat("タマ")

animal.speak()
dog.speak()
cat.speak()