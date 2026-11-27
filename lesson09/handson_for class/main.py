class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name}の通常攻撃！")


class Slime(Enemy):
    def __init__(self):
        super().__init__("スライム")

class Goblin(Enemy):
    def __init__(self):
        super().__init__("ゴブリン")

    def attack(self):
        super().attack()
        print(f"{self.name}は素早く追撃した！")

class Dragon(Enemy):
    def __init__(self):
        super().__init__("ドラゴン")
    
    def attack(self):
        super().attack()
        print(f"{self.name}はさらに炎を吐いた！")

class Golem(Enemy):
    def __init__(self):
        super().__init__("ゴーレム")
    
    def attack(self):
        print(f"{self.name}は強力な一撃を繰り出した！")

slime = Slime()
goblin = Goblin()
dragon = Dragon()
golem = Golem()

slime.attack()
goblin.attack()
dragon.attack()
golem.attack()