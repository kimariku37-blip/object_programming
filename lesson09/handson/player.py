from object_programming.lesson09.handson.character import Character


class Player(Character):
    def __init__(self, name, hp, attack_power, mp):
        super().__init__(name, hp, attack_power)
        self.mp = mp
        self.exp = 0

    def heal(self, amount):
        self._recover_hp(amount)

    def use_potion(self):
        print(f"{self.name}はポーションを使った！")
        self.heal(20)

    def show_mp(self):
        print(f"{self.name}のMP：{self.mp}")

    def gain_exp(self, amount):
        if amount <= 0:
            return

        self.exp += amount
        print(f"{self.name}は{amount}の経験値を獲得した！")

    def show_exp(self):
        print(f"{self.name}の経験値：{self.exp}")