class Game:
    def __init__(self, name):
        self.name=name
    def show(self):
        print("Назва гри: "+self.name)
    def __str__(self):
        return self.name

class Videogame(Game):
    def __init__(self,name,year,genre):
        super().__init__(name)
        self.year=year
        self.genre=genre
    def __len__(self):
        return len(self.name)
    def __str__(self):
        return Game.__str__(self)+"\n"+"Рік:%s Жанр:"%self.year + self.genre
ob=Videogame("Doom",2016, "fps")
print(ob)
print("Кількість букв у назві:%s" %len(ob))