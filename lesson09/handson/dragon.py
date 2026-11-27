from object_programming.lesson09.handson.enemy import Enemy


class Dragon(Enemy):
    def __init__(self):
        super().__init__("ドラゴン", 100, 12, 50)

    def attack(self, target):
        print(f"{self.name}は炎を吐いた！")

        damage = self.get_attack_power() * 2
        target.take_damage(damage)
