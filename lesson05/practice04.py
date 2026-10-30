class Robot:
    def __init__(self, name, energy, power, armor):
        self.name = name
        self.__energy = energy
        self.__power = power
        self.__armor = armor

    def get_armor(self):
        return self.__armor

    def receive_damage(self, amount):
        if amount <= 0:
            return

        self.__energy -= amount

        if self.__energy < 0:
            self.__energy = 0

        print(f"{self.name}は{amount}ダメージを受けた！")
        self.show_energy()

    def show_energy(self):
        print(f"{self.name}のエネルギー：{self.__energy}")

    def fire(self, target):
        print(f"{self.name}が{target.name}にビーム攻撃！")

        damage = self.__power * 4 - target.get_armor() * 2

        if damage < 1:
            damage = 1

        target.receive_damage(damage)


robot1 = Robot("ロボA", 100, 10, 4)
robot2 = Robot("ロボB", 80, 8, 6)

robot1.fire(robot2)
robot2.fire(robot1)