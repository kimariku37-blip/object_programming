class GameCharacter:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name}はHPが{amount}回復した！")

    def show_status(self):
        print(f"名前：{self.name}")
        print(f"HP：{self.hp}")

character1 = GameCharacter("剣士", 100)

character1.heal(30)

character1.show_status()