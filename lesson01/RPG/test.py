class Character:
    def __init__(self, name, age):       #初期化メソッド
        self.name = name
        self.age = age
        self.hobby = "筋トレ"
        
    def introduce(self):
        print("名前は" + self.name + "です")
        print("年齢は" + str(self.age) + "です")
        print("趣味は" + self.hobby + "です")


player = Character("kimata", 18)
enemy = Character("テネプレ", 19)

player.introduce()    #console.log()  window.alert()
enemy.introduce()



