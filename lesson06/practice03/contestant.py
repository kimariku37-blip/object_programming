# 参加者を表すクラス
class Contestant:

    # コンストラクタ
    # name : 参加者名
    def __init__(self, name):

        # 参加者名を保存
        self.name = name

        # 得点を0点で初期化
        self.__score = 0

    # 得点を加算する
    # points : 加算する得点
    def add_score(self, points):

        # 0点以下は加算しない
        if points <= 0:
            return

        # 得点を加算
        self.__score += points

    # 現在の得点を取得する
    def get_score(self):
        return self.__score

    # 名前と得点を表示する
    def show_score(self):
        print(f"{self.name}:{self.__score}点")