class Smartphone:
    def __init__(self, model, battery):
        self.model = model
        self.battery = battery

    def use(self, amount):
            self.battery -= amount
            print(f"{self.model}を使用しました。バッテリーを{self.battery}%消費しました。")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.model}を充電しました。バッテリーを{self.battery}%回復しました。")

    def show_status(self):
         print(f"{self.model}")
         print(f"{self.battery}%")

phone = Smartphone("iPhone15 pro", 80)

phone.use(30)

phone.charge(20)

phone.show_status()

          