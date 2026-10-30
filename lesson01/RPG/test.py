# キャラクターを表すクラス
class Character:

    # 初期化メソッド（コンストラクタ）
    # name : 名前
    # age : 年齢
    def __init__(self, name, age):

        # インスタンス変数に値を保存
        self.name = name
        self.age = age

        # 全キャラクター共通の趣味
        self.hobby = "筋トレ"

    # 自己紹介を行うメソッド
    def introduce(self):

        # 名前を表示
        print("名前は" + self.name + "です")

        # 年齢を表示
        # ageは整数なのでstr()で文字列に変換する
        print("年齢は" + str(self.age) + "です")

        # 趣味を表示
        print("趣味は" + self.hobby + "です")


# Characterクラスから勇者を生成
player = Character("kimata", 18)

# Characterクラスから敵を生成
enemy = Character("テネプレ", 19)

# playerオブジェクトのintroduce()を実行
# JavaScriptでいう console.log() や関数呼び出しに近い
player.introduce()

# enemyオブジェクトのintroduce()を実行
enemy.introduce()