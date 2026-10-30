class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_info(self):
        print(f"{self.name}：月給{self.__salary}円")