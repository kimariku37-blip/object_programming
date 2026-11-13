class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def show_status(self):
        print(f"{self.name}のHP：{self.hp}")

    def take_damage(self, amount):
        if amount <= 0:
            return

        self.hp -= amount

        if self.hp < 0:
            self.hp = 0

        print(f"{self.name}は{amount}ダメージを受けた！")

    def heal(self, amount):
        if amount <= 0:
            return

        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

class Player(Character):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp

    def use_potion(self):
        self.heal(20)
        print(f"{self.name}はポーションを使った！")

    def show_mp(self):
        print(f"{self.name}のMP：{self.mp}")

class Enemy(Character):
    def __init__(self, name, hp, reward_exp):
        super().__init__(name, hp)
        self.reward_exp = reward_exp

    def growl(self):
        print(f"{self.name}は威嚇している！")

    def show_reward_exp(self):
        print(f"{self.name}の獲得経験値：{self.reward_exp}")

hero = Player("勇者", 100, 30)
slime = Enemy("スライム", 50, 15)

hero.show_status()
slime.show_status()

hero.take_damage(30)
slime.take_damage(20)

hero.show_status()
slime.show_status()

hero.use_potion()
hero.show_status()

slime.growl()

slime.show_reward_exp()

