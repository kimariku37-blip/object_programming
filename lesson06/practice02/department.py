class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"{self.name}の社員一覧")

        for employee in self.employees:
            employee.show_info()
