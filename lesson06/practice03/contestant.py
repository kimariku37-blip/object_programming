class Contestant:
    def __init__(self, name):
        self.name = name
        self.__score = 0

    def add_score(self, points):
        if points <= 0:
            return

        self.__score += points

    def get_score(self):
        return self.__score

    def show_score(self):
        print(f"{self.name}:{self.__score}点")