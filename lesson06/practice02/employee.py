# 社員を表すクラス
class Employee:

    # コンストラクタ
    # name : 社員名
    # salary : 月給
    def __init__(self, name, salary):

        # 社員名を保存
        self.name = name

        # 給与は外部から直接変更されないように
        # プライベート属性として管理する
        self.__salary = salary

    # 社員情報を表示する
    def show_info(self):

        # 社員名と月給を表示
        print(f"{self.name}：月給{self.__salary}円")