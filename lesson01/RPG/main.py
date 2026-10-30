def attack(attacker, target):
    input(attacker["name"] + "の攻撃！▼")

    target["hp"] -= attacker["attack"]

    input(target["name"] 
          + "に" 
          + str(attacker["attack"]) 
          + "のダメージ！▼"
          )

def show_status(player, enemy):
    print()
    print(player["name"], "HP:", player["hp"])
    print(enemy["name"], "HP:", enemy["hp"])

player = {
    "name": "勇者",
    "hp": 100,
    "attack": 20
}

enemy = {
    "name": "スライム",
    "hp": 50,
    "attack": 10
}

destory_player = {
    "name": "最強勇者",
    "hp": 1000,
    "attack": 10000000
}

input(enemy["name"] + "があらわれた！▼")

while player["hp"] > 0 and enemy["hp"] > 0:

    print()
    print(player["name"], "HP:", player["hp"])
    print(enemy["name"], "HP:", enemy["hp"])

    print()
    print("どうする？")
    print("1.こうげき")

    command = input("> ")

    if command == "1":
        attack(player, enemy)

        if enemy["hp"] > 0:
            attack(enemy, player)


    elif command == "8635":
        attack(destory_player, enemy)
        

    print()
    print(player["name"], "HP:", player["hp"])
    print(enemy["name"], "HP:", enemy["hp"])

print()
if enemy["hp"] <= 0:
    input(enemy["name"] + "をたおした！▼")
else:
    input(player["name"] + "はしんでしまった…▼") 