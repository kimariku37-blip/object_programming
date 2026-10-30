class Character:
    def __init__(self, name, hp, level):            #Character()からインスタンスが作られるたびに実行される。
        self.name = name
        self.hp = hp
        self.level = level


    def show_status(self):  #メソッドの第１引数はselfにすること   ->  selfは勝手にインスタンスを変更できる（なんでもなれる）例）self == hero , self == wizard 
        print(f"名前:{self.name}")
        print(f"HP:{self.hp}")
        print(f"レベル:{self.level}")

    def show_hp(self):
        print(f"HP{self.hp}")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name}はHPが{amount}回復した！")
        self.show_hp()    

hero = Character()
hero.show_status()

warrior = Character("戦士", 150, 6)
warrior.show_status()



#def show_status(character):     #インデントされていないもの：トップレベル関数
#    print("--------------------")
#    print(f"名前：{character.name}")
#    print(f"HP：{character.hp}")
#    print(f"レベル：{character.level}")

#def heal(character, amount):
#    character.hp += amount

#hero.show_status()
#hero.heal(40)
#hero.show_status()


#class Item:
#    def get_price_with_tax(self):
#        return self.price * 1.1
#
#item = Item()
#item.price = 1000
#
#price_with_tax = item.get_price_with_tax()
#
#print(price_with_tax)

    