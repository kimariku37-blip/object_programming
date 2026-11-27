from object_programming.lesson09.practice03.robot import Robot

class SecurityRobot(Robot):
    def __init__(self, battery):
        super().__init__("警備ロボット", battery)

    def work(self):
        print("警備ロボットは巡回作業を行った！")
        self.battery -= 20