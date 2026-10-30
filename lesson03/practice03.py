class Student:
    def show_result(self):
        print(f"名前：{self.name}")
        print(f"点数：{self.score}")

student = Student()

student.name = "木全"
student.score = 80

student.show_result()