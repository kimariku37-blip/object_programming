# Contestantクラスを読み込む
from contestant import Contestant

# Tournamentクラスを読み込む
from tournament import Tournament


# 参加者を作成
player1 = Contestant("勇者")
player2 = Contestant("魔法使い")

# 大会オブジェクトを作成
# 勇者と魔法使いを大会に参加させる
tournament = Tournament(player1, player2)

# 大会開始
tournament.start()