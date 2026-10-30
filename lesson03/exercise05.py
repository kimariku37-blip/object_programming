class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print(f"タイトル：{self.title}")
        print(f"上映時間：{self.duration}分")    

movie1 = Movie("ベイマックス", 120)

movie1.show_info()