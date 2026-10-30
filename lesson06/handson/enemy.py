class Enemy:
    # Enemyクラスの初期化
    # name：敵の名前
    # hp：敵の体力
    # attack_power：敵の攻撃力
    def __init__(self, name, hp, attack_power):
        # 外部から参照できる名前
        self.name = name

        # HPと攻撃力はカプセル化するためプライベート属性にする
        self.__hp = hp
        self.__attack_power = attack_power

    # 指定された相手を攻撃する
    def attack(self, target):
        print(f"{self.name}が{target.name}を攻撃！")

        # 相手に自分の攻撃力分のダメージを与える
        target.take_damage(self.__attack_power)

    # ダメージを受ける処理
    def take_damage(self, amount):

        # ダメージが0以下なら何もしない
        if amount <= 0:
            return

        # HPを減少させる
        self.__hp -= amount

        # HPが0未満にならないよう補正する
        if self.__hp < 0:
            self.__hp = 0

        # ダメージ内容を表示
        print(f"{self.name}は{amount}ダメージを受けた！")

        # ダメージ後のHPを表示
        self.show_hp()

    # 現在のHPを表示する
    def show_hp(self):
        print(f"{self.name}のHP：{self.__hp}")

    # 生存判定を行う
    # HPが1以上ならTrue、0ならFalseを返す
    def is_alive(self):
        return self.__hp > 0