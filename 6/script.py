#створення класу відеогра
class Videogame:
    lichylnyk=0
    def __init__(self, name, year, genre):
        self.name=name
        self.year=year
        self.genre=genre
        Videogame.lichylnyk+=1
    def show(self):
        print("Назва гри: "+self.name)
        print("Рік випуску: %s" %self.year)
        print("Жанр гри: "+self.genre)
    def count(self):
        print("Rількість об'єктів: %s"%Videogame.lichylnyk)
#створення об'єктів з характеристиками, вивід інформації про них і кількість об'єктів
obj1=Videogame("Counter-strike 2", 2023, "Shooter")
obj1.show()
obj1.count()
obj2=Videogame("Stellaris", 2016, "Strategy game")
obj2.show()
obj1.count()
obj3=Videogame("Ultrakill", 2020, "Shooter")
obj3.show()
obj1.count()
