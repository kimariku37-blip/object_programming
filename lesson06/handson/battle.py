class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def show_status(self):
        print("===== 戦闘参加者 =====")
        self.player.show_hp()
        self.enemy.show_hp()

    def one_turn(self):
        print()

        self.player.attack(self.enemy)

        if self.enemy.is_alive():
            print()
            self.enemy.attack(self.player)

    def start(self):
        print("===== バトル開始！ =====")
        self.show_status()

        while self.player.is_alive() and self.enemy.is_alive():
            self.one_turn()

        print()
        self.show_result()
        print("===== バトル終了 =====")

    def show_result(self):
        if not self.enemy.is_alive():
            print(f"{self.enemy.name}を倒した！")
        else:
            print(f"{self.player.name}は倒れてしまった...。")