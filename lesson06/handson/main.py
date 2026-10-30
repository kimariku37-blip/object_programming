from player import Player
from enemy import Enemy
from battle import Battle



hero = Player("勇者", 100, 25)
slime = Enemy("スライム", 60, 15)

battle = Battle(hero, slime)

battle.start()

