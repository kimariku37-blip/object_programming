# 部署を表すクラス
class Department:

    # コンストラクタ
    # name : 部署名
    def __init__(self, name):

        # 部署名を保存
        self.name = name

        # 社員オブジェクトを格納するリスト
        self.employees = []

    # 社員を部署へ追加する
    def add_employee(self, employee):

        # 引数で受け取った社員オブジェクトをリストに追加
        self.employees.append(employee)

    # 所属社員一覧を表示する
    def show_employees(self):

        # 部署名を表示
        print(f"{self.name}の社員一覧")

        # 社員リストを順番に取り出す
        for employee in self.employees:

            # Employeeクラスのshow_info()を呼び出す
            employee.show_info()