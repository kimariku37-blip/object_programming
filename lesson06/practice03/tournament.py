# 大会を管理するクラス
class Tournament:

    # コンストラクタ
    # player1 : 参加者1
    # player2 : 参加者2
    def __init__(self, player1, player2):

        # 参加者を保持
        self.player1 = player1
        self.player2 = player2

        # 現在のラウンド数
        self.round_number = 0

    # 1ラウンド実施する
    # points1 : player1が獲得した得点
    # points2 : player2が獲得した得点
    def play_round(self, points1, points2):

        # ラウンド数を1増やす
        self.round_number += 1

        print(f"--- 第{self.round_number}ラウンド ---")

        # 各プレイヤーに得点を加算
        self.player1.add_score(points1)
        self.player2.add_score(points2)

        # 現在の得点を表示
        self.player1.show_score()
        self.player2.show_score()

    # 最終結果を表示する
    def show_result(self):

        print(" ===== 大会結果 =====")

        # 両者の得点を表示
        self.player1.show_score()
        self.player2.show_score()

        # 得点を取得
        score1 = self.player1.get_score()
        score2 = self.player2.get_score()

        # player1の方が高得点の場合
        if score1 > score2:
            print(f"優勝：{self.player1.name}")

        # player2の方が高得点の場合
        elif score2 > score1:
            print(f"優勝：{self.player2.name}")

        # 同点の場合
        else:
            print("引き分け！")

    # 大会開始
    def start(self):

        print("===== ゲーム大会開始！ =====")

        # 第1ラウンド
        self.play_round(20, 15)

        # 第2ラウンド
        self.play_round(5, 25)

        # 第3ラウンド
        self.play_round(35, 10)

        # 最終結果を表示
        self.show_result()

        print("===== ゲーム大会終了 =====")