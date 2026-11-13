from character import Character

class Enemy(Character):
    def __init__(self, name, hp, attack_power, reward_exp):
        super().__init__(name, hp, attack_power)
        self.reward_exp = reward_exp

    def get_reward_exp(self):
        return self.reward_exp

    def growl(self):
        print(f"{self.name}は威嚇している！")