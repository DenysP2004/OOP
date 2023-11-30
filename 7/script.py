class Videogame:
    def __init__(self, name, year, genre):
        self.name=name
        self.year=year
        self.genre=genre
    def show(self):
        print("Назва гри: "+self.name)
        print("Рік випуску: %s" %self.year)
        print("Жанр гри: "+self.genre)
    @classmethod
    def add(cls, data):
        name, year, genre = data.split(" ")
        return cls(name, year, genre)
    @staticmethod
    def showgenre(genre):
        print(genre)
obj1=Videogame("Counter-strike 2", 2023, "Shooter")
obj1.show()
obj2=Videogame("Stellaris", 2016, "Strategy game")
obj2.show()
obj3=Videogame("Ultrakill", 2020, "Shooter")
obj3.show()
print("дані з альтернативного конструктора методу класу: ")
obj4=Videogame.add("Doom 2016 Shooter")
obj4.show()
obj4.showgenre(obj4.genre)
