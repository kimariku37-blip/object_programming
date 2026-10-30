from employee import Employee
from department import Department

employee1 = Employee("田中", 250000)
employee2 = Employee("佐藤", 300000)
employee3 = Employee("鈴木", 280000)

department = Department("営業部")

department.add_employee(employee1)
department.add_employee(employee2)
department.add_employee(employee3)

department.show_employees()