#class Player():
#    pass
#
#player = Player()
#
#player.name = "勇者"
#player.hp = 100
#player.level = 1
#
#print(player.name)
#print(player.hp)
#print(player.level)
#
#input(f"{player.name}は攻撃を受けた！20のダメージ！ ▼")
#
#player.hp -= 20
#
#print(f"{player.name}の体力：{player.hp} ▼")
#
#input(f"{player.name}は何かに目覚めた...。レベルが１上がった！ ▼")
#
#player.level += 1
#
#print(f"{player.name}現在のレベル：{player.level} ▼")

#class Player:
#    pass
#
#player1 = Player()
#
#player1.name = "勇者"
#player1.hp = 100
#player1.level = 1
#
#print(f"名前：{player1.name}")
#print(f"体力：{player1.hp}")
#print(f"レベル：{player1.level}")
#
#player2 = Player()
#
#player2.name = "魔法使い"
#player2.hp = 80
#player2.level = 1
#
#print(f"名前：{player2.name}")
#print(f"体力：{player2.hp}")
#print(f"レベル：{player2.level}")
#
#input(f"{player1.name}は30のダメージを受けた！▼")
#
#player1.hp -= 30
#
#print(f"{player1.name}のHP：{player1.hp}")
#print(f"{player2.name}のHP：{player2.hp}")

#names = ["勇者", "魔法使い", "戦士"]
#
#class Player:
#    pass
#
#
#player1 = Player()
#
#player1.name = "勇者"
#player1.hp = 100
#player1.level = 1
#
#
#player2 = Player()
#
#player2.name = "魔法使い"
#player2.hp = 80
#player2.level = 1
#
#
#player3 = Player()
#
#player3.name = "戦士"
#player3.hp = 150
#player3.level = 1
#
#players = [player1, player2, player3]
#
#names = ["勇者", "魔法使い", "戦士"]
#
#for name in names:
#    print(name)
#
#for player in players:
#    print("-------------")
#    print(f"名前：{player.name}")
#    print(f"HP：{player.hp}")
#    print(f"レベル：{player.level}")
    
class Player:
    pass


player1 = Player()

player1.name = "勇者"
player1.hp = 100
player1.level = 1


player2 = Player()

player2.name = "魔法使い"
player2.hp = 80
player2.level = 1


player3 = Player()

player3.name = "戦士"
player3.hp = 150
player3.level = 1


players = [player1, player2, player3]


def show_player(player):
    print("--------------------")
    print(f"名前：{player.name}")
    print(f"HP：{player.hp}")
    print(f"レベル：{player.level}")


def damage_player(player, damage_amount):
    input(f"{player.name}は{damage_amount}のダメージを受けた！▼")

    player.hp -= damage_amount

    print(f"{player.name}のHP：{player.hp}")


for player in players:
    show_player(player)

print("--------------------")

damage_player(player1, 30)
