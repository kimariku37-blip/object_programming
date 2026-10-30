class Pet:
    def show_info(self):
        print(f"名前：{self.name}")
        print(f"年齢：{self.age}歳")

pet = Pet()

pet.name = "ポチ"
pet.age = 3
pet.show_info()