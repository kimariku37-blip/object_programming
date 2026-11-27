from object_programming.lesson09.exercise03.enemy import Enemy

class ArmoredEnemy(Enemy):
    def __init__(self):
        super().__init__("アーマーゴーレム", 50)