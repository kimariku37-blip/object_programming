class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def work(self):
        print(f"{self.name}は通常作業を行った！")
        self.battery -= 10

    def show_battery(self):
        print(f"{self.name}のバッテリー残量：{self.battery}")