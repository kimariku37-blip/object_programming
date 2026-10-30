class Battle:
    # Battleクラスの初期化
    # playerには勇者や主人公のオブジェクト
    # enemyには敵キャラクターのオブジェクトを渡す
    def __init__(self, player, enemy):
        # プレイヤーをメンバ変数に保存
        self.player = player

        # 敵をメンバ変数に保存
        self.enemy = enemy

    # 戦闘参加者の現在HPを表示する
    def show_status(self):
        print("===== 戦闘参加者 =====")

        # プレイヤーのHP表示
        self.player.show_hp()

        # 敵のHP表示
        self.enemy.show_hp()

    # 1ターン分の戦闘処理
    def one_turn(self):
        print()

        # プレイヤーが先に攻撃
        # attack()の中でダメージ計算やHP減少が行われる
        self.player.attack(self.enemy)

        # 敵がまだ生きている場合のみ反撃する
        if self.enemy.is_alive():
            print()

            # 敵の攻撃
            self.enemy.attack(self.player)

    # バトル開始処理
    def start(self):
        print("===== バトル開始！ =====")

        # 戦闘開始時点のHPを表示
        self.show_status()

        # プレイヤーと敵の両方が生存している間、
        # ターン処理を繰り返す
        while self.player.is_alive() and self.enemy.is_alive():
            self.one_turn()

        print()

        # 戦闘終了後の結果を表示
        self.show_result()

        print("===== バトル終了 =====")

    # 勝敗結果を表示する
    def show_result(self):

        # 敵が倒されていた場合はプレイヤーの勝利
        if not self.enemy.is_alive():
            print(f"{self.enemy.name}を倒した！")

        # 敵が生きているということは、
        # プレイヤーが先に倒されたことになる
        else:
            print(f"{self.player.name}は倒れてしまった...。")