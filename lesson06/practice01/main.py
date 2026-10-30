# 飲み物クラス
class Drink:

    # コンストラクタ
    # name : 商品名
    # price : 価格
    # stock : 在庫数
    def __init__(self, name, price, stock):
        self.name = name

        # 価格と在庫は直接変更されないようにプライベート属性にする
        self.__price = price
        self.__stock = stock

    # 商品の価格を取得する
    def get_price(self):
        return self.__price

    # 現在の在庫数を取得する
    def get_stock(self):
        return self.__stock

    # 商品を1本販売する
    def sell_one(self):

        # 在庫がない場合は販売できない
        if self.__stock == 0:
            return False

        # 在庫を1減らす
        self.__stock -= 1

        # 販売成功
        return True


# 自動販売機クラス
class VendingMachine:

    # 販売する飲み物を受け取る
    def __init__(self, drink):
        self.drink = drink

    # 購入処理
    # money : 投入金額
    def buy(self, money):

        # 商品の価格より投入金額が少ない場合
        if money < self.drink.get_price():
            print("お金が足りません。")
            return

        # 在庫がある場合は購入成功
        if self.drink.sell_one():
            print(f"{self.drink.name}を購入しました！")

        # 在庫がない場合
        else:
            print("売り切れです。")


# お茶を作成
# 商品名: お茶
# 価格: 120円
# 在庫: 2本
tea = Drink("お茶", 120, 2)

# お茶を販売する自動販売機を作成
machine = VendingMachine(tea)

# 100円で購入を試みる
# → お金不足
machine.buy(100)

# 120円で購入
# → 在庫 2 → 1
machine.buy(120)

# 150円で購入
# → 在庫 1 → 0
machine.buy(150)

# 120円で購入
# → 売り切れ
machine.buy(120)

# 最終的な在庫を表示
print(f"{tea.name}の在庫：{tea.get_stock()}本")