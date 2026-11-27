from object_programming.lesson09.handson.enemy import Enemy


class Goblin(Enemy):
    def __init__(self):
        super().__init__("ゴブリン", 75, 10, 25)

    def attack(self, target):
        print(f"{self.name}は連続攻撃をした！")

        super().attack(target)

        if target.is_alive():
            super().attack(target)