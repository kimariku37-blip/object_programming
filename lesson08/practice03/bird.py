from animal import Animal

class Bird(Animal):
    def __init__(self, name, energy, wing_span):
        super().__init__(name, energy)
        self.wing_span = wing_span

    def fly(self):
        self.use_energy(15)
        print(f"{self.name}は空を飛んだ！")

    def show_wing_span(self):
        print(f"{self.name}の翼の長さ：{self.wing_span}cm")