from object_programming.lesson09.practice03.robot import Robot
from object_programming.lesson09.practice03.cleaning_robot import CleaningRobot
from object_programming.lesson09.practice03.security_robot import SecurityRobot

normal = Robot("汎用ロボット", 50)
cleaner = CleaningRobot(50)
security = SecurityRobot(50)

normal.work()
normal.show_battery()

print()

cleaner.work()
cleaner.show_battery()

print()

security.work()
security.show_battery()