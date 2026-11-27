from object_programming.lesson09.handson.enemy import Enemy


class Slime(Enemy):
    def __init__(self):
        super().__init__("スライム", 60, 15, 15)