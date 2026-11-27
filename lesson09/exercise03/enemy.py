class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp
        self.__max_hp = hp

    def take_damage(self, amount):
        if amount <= 0:
            return

        self.__hp -= amount

        if self.__hp < 0:
            self.__hp = 0

        print(f"{self.name}は{amount}ダメージを受けた！")
        self.show_hp()

    def heal(self, amount):
        if amount <= 0 or not self.is_alive():
            return

        self.__hp += amount

        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp

        print(f"{self.name}はHPを回復した！")
        self.show_hp()

    def show_hp(self):
        print(f"{self.name}のHP：{self.__hp}")

    def is_alive(self):
        return self.__hp > 0