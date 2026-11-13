from player import Player
from enemy import Enemy
from battle import Battle

hero = Player("勇者", 100, 25, 30)
slime = Enemy("スライム", 60, 15, 15)

battle = Battle(hero, slime)

hero.show_mp()
slime.growl()

battle.start()

if hero.is_alive():
    hero.gain_exp(slime.get_reward_exp())
    hero.show_exp()
    hero.use_potion()