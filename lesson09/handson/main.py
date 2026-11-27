from object_programming.lesson09.handson.player import Player
from object_programming.lesson09.handson.slime import Slime
from object_programming.lesson09.handson.goblin import Goblin
from object_programming.lesson09.handson.dragon import Dragon
from object_programming.lesson09.handson.battle import Battle


print("===== スライム戦 =====")

hero = Player("勇者", 100, 25, 30)
enemy = Slime()

battle = Battle(hero, enemy)
battle.start()

if hero.is_alive():
    hero.gain_exp(enemy.get_reward_exp())
    hero.show_exp()


print("===== ゴブリン戦 =====")

hero = Player("勇者", 100, 25, 30)
enemy = Goblin()

battle = Battle(hero, enemy)
battle.start()

if hero.is_alive():
    hero.gain_exp(enemy.get_reward_exp())
    hero.show_exp()


print("===== ドラゴン戦 =====")

hero = Player("勇者", 100, 25, 30)
enemy = Dragon()

battle = Battle(hero, enemy)
battle.start()

if hero.is_alive():
    hero.gain_exp(enemy.get_reward_exp())
    hero.show_exp()