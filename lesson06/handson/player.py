class Player:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.__hp = hp
        self.__max_hp = hp
        self.__attack_power = attack_power

    def attack(self, target):
        print(f"{self.name}が{target.name}を攻撃！")
        target.take_damage(self.__attack_power)

    def take_damage(self, amount):
        if amount <= 0:
            return

        self.__hp -= amount

        if self.__hp < 0:
            self.__hp = 0

        print(f"{self.name}は{amount}ダメージを受けた！")
        self.show_hp()

    def heal(self, amount):
        if amount <= 0:
            return

        self.__hp += amount

        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp

        self.show_hp()

    def show_hp(self):
        print(f"{self.name}のHP：{self.__hp}")

    def is_alive(self):
        return self.__hp > 0