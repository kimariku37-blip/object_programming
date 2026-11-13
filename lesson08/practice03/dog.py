from animal import Animal

class Dog(Animal):
    def __init__(self, name, energy, favorite_toy):
        super().__init__(name, energy)
        self.favorite_toy = favorite_toy

    def walk(self):
        self.use_energy(20)
        print(f"{self.name}は散歩した！")

    def show_toy(self):
        print(f"{self.name}のお気に入り：{self.favorite_toy}")