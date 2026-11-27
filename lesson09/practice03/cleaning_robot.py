from object_programming.lesson09.practice03.robot import Robot

class CleaningRobot(Robot):
    def __init__(self, battery):
        super().__init__("清掃ロボット", battery)

    def work(self):
        super().work()
        print("清掃ロボットは床を掃除した！")
        self.battery -= 5