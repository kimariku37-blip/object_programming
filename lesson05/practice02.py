class Pet:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def show_status(self):
        print(f"{self.name}の体力：{self.energy}")

    def play(self, amount):
        if amount <= 0:
            return

        self.energy -= amount

        if self.energy < 0:
            self.energy = 0

    def rest(self, amount):
        if amount <= 0:
            return

        self.energy += amount

        if self.energy > 100:
            self.energy = 100


pet = Pet("ポチ", 80)


pet.show_status()

pet.play(30)

pet.show_status()

pet.rest(80)

pet.show_status()

pet.play(-10)

pet.show_status()

pet.rest(0)

pet.show_status()

pet.play(150)

pet.show_status()