from object_programming.lesson09.practice02.ticket import Ticket
from object_programming.lesson09.practice02.student_ticket import StudentTicket
from object_programming.lesson09.practice02.premium_ticket import PremiumTicket

normal = Ticket("通常チケット", 2000)
student = StudentTicket(2000, 500)
premium = PremiumTicket(2000, 1000)

print(f"{normal.name}：{normal.calculate_price()}円")
print(f"{student.name}：{student.calculate_price()}円")
print(f"{premium.name}：{premium.calculate_price()}円")