#インスタンス同士のやり取り
#
#class Character:
#    def __init__(self, name, hp):
#        self.name = name
#        self.hp = hp
#
#    def greet(self, target):
#        print(f"{self.name}は{target.name}にあいさつした")
#
#    def show_hp(self):
#        print(f"{self.name}のHP：{self.hp}")
#
#    def heal(self, amount):
#        self.hp += amount
#
#    def support(self, target, amount):
#        target.heal(amount)
#        print(f"{self.name}は{target.name}のHPを{amount}回復させた")
#
#
#hero = Character("勇者", 100)
#wizard = Character("魔法使い", 70)
#
#hero.greet(wizard)
#wizard.greet(hero)
#
#hero.support(wizard, 20)
#wizard.show_hp()
#
#wizard.support(hero, 10)
#hero.show_hp()

#バトルプログラムを作成する

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def show_hp(self):
        print(f"{self.name}のHP：{self.hp}")
    
    def attack(self, target):
        print(f"{self.name}が{target.name}を攻撃！")
        target.take_damage(self.attack_power)   

    def take_damage(self, amount):
        self.hp -= amount
        
        if self.hp < 0:
            self.hp = 0
        
        print(f"{self.name}は{amount}ダメージを受けた！")
        self.show_hp()

hero = Character("勇者", 30, 25)
slime = Character("スライム", 60, 15)

print("===== バトル開始！ =====")

hero.show_hp()
slime.show_hp()

while hero.hp > 0 and slime.hp > 0:
    print()
    hero.attack(slime)

    if slime.hp <= 0:
        break

    print()
    slime.attack(hero)

print()

if slime.hp == 0:
    print("スライムを倒した！")
else:
    print("勇者は倒れてしまった...。")

print("===== バトル終了 =====")