class Player:
    # Playerクラスの初期化
    # name：プレイヤー名
    # hp：初期HP
    # attack_power：攻撃力
    def __init__(self, name, hp, attack_power):
        # プレイヤー名を保持
        self.name = name

        # 現在のHP
        self.__hp = hp

        # 最大HP
        # 回復時に最大値を超えないようにするため保持しておく
        self.__max_hp = hp

        # 攻撃力
        self.__attack_power = attack_power

    # 敵を攻撃する
    def attack(self, target):
        print(f"{self.name}が{target.name}を攻撃！")

        # 相手に攻撃力分のダメージを与える
        target.take_damage(self.__attack_power)

    # ダメージを受ける処理
    def take_damage(self, amount):

        # ダメージが0以下なら処理しない
        if amount <= 0:
            return

        # HPを減らす
        self.__hp -= amount

        # HPが0未満にならないよう補正
        if self.__hp < 0:
            self.__hp = 0

        # ダメージ結果を表示
        print(f"{self.name}は{amount}ダメージを受けた！")

        # 現在HPを表示
        self.show_hp()

    # HPを回復する処理
    def heal(self, amount):

        # 回復量が0以下なら処理しない
        if amount <= 0:
            return

        # HPを回復
        self.__hp += amount

        # 最大HPを超えた場合は最大HPに戻す
        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp

        # 回復後のHPを表示
        self.show_hp()

    # 現在のHPを表示する
    def show_hp(self):
        print(f"{self.name}のHP：{self.__hp}")

    # 生存しているか判定する
    # HPが1以上ならTrue
    # HPが0