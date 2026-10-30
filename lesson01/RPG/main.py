# 攻撃処理を行う関数
# attacker : 攻撃するキャラクター
# target : 攻撃されるキャラクター
def attack(attacker, target):

    # 攻撃メッセージ表示
    input(attacker["name"] + "の攻撃！▼")

    # 相手のHPを攻撃力分減らす
    target["hp"] -= attacker["attack"]

    # ダメージメッセージ表示
    input(
        target["name"]
        + "に"
        + str(attacker["attack"])
        + "のダメージ！▼"
    )


# ステータス表示用関数
def show_status(player, enemy):
    print()
    print(player["name"], "HP:", player["hp"])
    print(enemy["name"], "HP:", enemy["hp"])


# プレイヤーデータ
player = {
    "name": "勇者",
    "hp": 100,
    "attack": 20
}

# 敵データ
enemy = {
    "name": "スライム",
    "hp": 50,
    "attack": 10
}

# 隠しキャラクター（チート用）
destory_player = {
    "name": "最強勇者",
    "hp": 1000,
    "attack": 10000000
}

# 敵出現
input(enemy["name"] + "があらわれた！▼")

# プレイヤーまたは敵が倒れるまで繰り返す
while player["hp"] > 0 and enemy["hp"] > 0:

    # 現在のHP表示
    print()
    print(player["name"], "HP:", player["hp"])
    print(enemy["name"], "HP:", enemy["hp"])

    # コマンド選択
    print()
    print("どうする？")
    print("1.こうげき")

    command = input("> ")

    # 通常攻撃
    if command == "1":

        # プレイヤーの攻撃
        attack(player, enemy)

        # 敵が生きていれば反撃
        if enemy["hp"] > 0:
            attack(enemy, player)

    # 隠しコマンド（チート）
    elif command == "8635":

        # 最強勇者による即死攻撃
        attack(destory_player, enemy)

    # 行動後のHP表示
    print()
    print(player["name"], "HP:", player["hp"])
    print(enemy["name"], "HP:", enemy["hp"])

# バトル終了
print()

# 勝敗判定
if enemy["hp"] <= 0:
    input(enemy["name"] + "をたおした！▼")
else:
    input(player["name"] + "はしんでしまった…▼")