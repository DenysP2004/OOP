class Game:
    def __init__(self, name):
        self.name=name
    def show(self):
        print("Назва гри: "+self.name)

class Videogame(Game):
    def __init__(self,name,year,genre):
        super().__init__(name)
        self.year=year
        self.genre=genre

    def show(self):
        Game.show(self)
        print("Рік:%s Жанр:"%self.year + self.genre)
class Player(Game):
    def __init__(self,name, year, game=None):
        super().__init__(name)
        self.year=year
        if game is None:
            game = []
        else:
             self.game=game
    def output(self):
        print(self.name)
        for g in self.game:
            g.show()
    
ob=Videogame("doom", 2016, "FPS")
ob.show()
obj=Player("Denis", "2004", [ob])
obj.output()