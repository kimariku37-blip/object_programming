class Tournament:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round_number = 0

    def play_round(self, points1, points2):
        self.round_number += 1

        print(f"--- 第{self.round_number}ラウンド ---")

        self.player1.add_score(points1)
        self.player2.add_score(points2)

        self.player1.show_score()
        self.player2.show_score()

    def show_result(self):
        print(" ===== 大会結果 =====")

        self.player1.show_score()
        self.player2.show_score()

        score1 = self.player1.get_score()
        score2 = self.player2.get_score()

        if score1 > score2:
            print(f"優勝：{self.player1.name}")

        elif score2 > score1:
            print(f"優勝：{self.player2.name}")

        else:
            print("引き分け！")

    def start(self):
        print("===== ゲーム大会開始！ =====")

        self.play_round(20, 15)
        self.play_round(5, 25)
        self.play_round(35, 10)

        self.show_result()

        print("===== ゲーム大会終了 =====")