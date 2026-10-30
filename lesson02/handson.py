# Playerクラス
# 今回は属性だけを持つシンプルなクラス
class Player:
    pass


# 勇者を作成
player1 = Player()

player1.name = "勇者"
player1.hp = 100
player1.level = 1


# 魔法使いを作成
player2 = Player()

player2.name = "魔法使い"
player2.hp = 80
player2.level = 1


# 戦士を作成
player3 = Player()

player3.name = "戦士"
player3.hp = 150
player3.level = 1


# プレイヤーをリストで管理
players = [player1, player2, player3]


# プレイヤー情報を表示する関数
# playerにはPlayerオブジェクトが渡される
def show_player(player):

    print("--------------------")
    print(f"名前：{player.name}")
    print(f"HP：{player.hp}")
    print(f"レベル：{player.level}")


# ダメージ処理を行う関数
# player : ダメージを受けるプレイヤー
# damage_amount : ダメージ量
def damage_player(player, damage_amount):

    # ダメージメッセージ表示
    input(f"{player.name}は{damage_amount}のダメージを受けた！▼")

    # HPを減少させる
    player.hp -= damage_amount

    # ダメージ後のHPを表示
    print(f"{player.name}のHP：{player.hp}")


# 全プレイヤーの情報を表示
for player in players:
    show_player(player)

print("--------------------")

# 勇者に30ダメージを与える
damage_player(player1, 30)