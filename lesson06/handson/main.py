# Playerクラスを読み込む
from player import Player

# Enemyクラスを読み込む
from enemy import Enemy

# Battleクラスを読み込む
from battle import Battle


# プレイヤー（勇者）を作成
# 引数：名前, HP, 攻撃力
hero = Player("勇者", 100, 25)

# 敵（スライム）を作成
# 引数：名前, HP, 攻撃力
slime = Enemy("スライム", 60, 15)

# Battleクラスのインスタンスを作成
# 勇者とスライムの戦闘を管理する
battle = Battle(hero, slime)

# バトル開始
battle.start()