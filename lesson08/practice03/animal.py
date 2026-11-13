class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def show_status(self):
        print(f"{self.name}の体力：{self.energy}")

    def use_energy(self, amount):
        if amount <= 0:
            return

        self.energy -= amount

        if self.energy < 0:
            self.energy = 0