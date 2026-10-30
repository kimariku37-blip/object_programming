# Employeeクラスを読み込む
from employee import Employee

# Departmentクラスを読み込む
from department import Department


# 社員オブジェクトを作成
# 引数：名前, 月給
employee1 = Employee("田中", 250000)
employee2 = Employee("佐藤", 300000)
employee3 = Employee("鈴木", 280000)

# 部署オブジェクトを作成
department = Department("営業部")

# 社員を営業部へ追加
department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(employee3)

# 営業部に所属している社員一覧を表示
department.show_employees()