class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def show_hp(self):
        print(f"{self.name}のHP：{self.hp}")


hero = Character("勇者", 100)

hero.show_hp()