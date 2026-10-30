from contestant import Contestant
from tournament import Tournament

player1 = Contestant("勇者")
player2 = Contestant("魔法使い")

tournament = Tournament(player1, player2)

tournament.start()