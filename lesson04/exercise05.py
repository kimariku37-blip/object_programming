class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def set_hand(self, hand):
        self.hand = hand

    def play(self, opponent):
        print(f"{self.name}：{self.hand}")
        print(f"{opponent.name}：{opponent.hand}")

        if self.hand == opponent.hand:
            print("あいこ！")
        elif (
            (self.hand == "グー" and opponent.hand == "チョキ") or
            (self.hand == "チョキ" and opponent.hand == "パー") or
            (self.hand == "パー" and opponent.hand == "グー")
        ):
            print(f"{self.name}の勝ち！")
        else:
            print(f"{opponent.name}の勝ち！")


player1 = Player("田中", "グー")
player2 = Player("佐藤", "チョキ")
player1.play(player2)
print()

player1.set_hand("チョキ")
player2.set_hand("グー")
player1.play(player2)
print()

player1.set_hand("パー")
player2.set_hand("パー")
player1.play(player2)
