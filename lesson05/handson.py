class Character:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.__hp = hp
        self.__max_hp = hp
        self.__attack_power = attack_power
        self.__defense = defense

    def show_hp(self):
        print(f"{self.name}のHP：{self.__hp}")

    def attack(self, target):
        print(f"{self.name}が{target.name}を攻撃！")
        

        defense = target.get_defense()
        power = 4

        damage = (
            (self.__attack_power ** 3 / 32 + 30)
            * (730 - (defense * 51 - defense ** 2 / 11) / 10)
            / 730
            * power / 16
        )
        target.take_damage(int(damage))

    def take_damage(self, amount):
        if amount <= 0:
            print("ダメージ量は1以上で指定してください。")
            return

        self.__hp -= amount

        if self.__hp < 0:
            self.__hp = 0

        print(f"{self.name}は{amount}ダメージを受けた！")
        self.show_hp()

    def heal(self, amount):
        if amount <= 0:
            print("回復量は1以上で指定してください。")
            return

        before_hp = self.__hp

        self.__hp += amount

        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp

        healed = self.__hp - before_hp

        print(f"{self.name}は{healed}HP回復した！")
        self.show_hp()
    
    def is_alive(self):
        return self.__hp > 0

    def get_defense(self):
        return self.__defense

hero = Character("勇者", 100, 12, 6)
slime = Character("スライム", 60, 15, 8)

print("===== バトル開始！ =====")

hero.show_hp()
slime.show_hp()

while hero.is_alive() > 0 and slime.is_alive() > 0:
    print()
    hero.attack(slime)

    if not slime.is_alive():
        break

    print()
    slime.attack(hero)

print()

if not slime.is_alive():
    print("スライムを倒した！")
else:
    print("勇者は倒れてしまった...。")

print("===== バトル終了 =====")

