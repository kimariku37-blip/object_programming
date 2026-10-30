class Pet:
    def __init__(self, name, fullness):
        self.name = name
        self.fullness = fullness

    def eat(self, amount):
        self.fullness += amount
        if self.fullness > 100:
            self.fullness = 100

    def show_status(self):
        print(f"{self.name}の満足度:{self.fullness}")

class Owner:
    def __init__(self, name):
        self.name = name

    def feed(self, pet, amount):
        pet.eat(amount)
        print(f"{self.name}は{pet.name}にエサを与えた！")

owner = Owner("田中")
dog = Pet("ポチ", 30)
cat = Pet("ミケ", 60)

dog.show_status()
cat.show_status()

owner.feed(dog, 25)
owner.feed(cat, 40)

dog.show_status()
cat.show_status()