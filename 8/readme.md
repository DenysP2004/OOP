### Львівський Національний Університет Природокористування 

### Кафедра Інформаційних Технологій 

# Звіт

#### про виконання практичної роботи №8

## Тема: Наслідування в об’єктно-орієнтованому програмуванні.

## Мета: оволодіння концепцією наслідування класів.

## Хід роботи
1. Створив два дочірніх класи. Використав функцію super() яка дозволяє перенести параметри конструктора базового класу.
```Py
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
class Player:
    def __init__(self,name, year, game=None):
        super().__init__(name,year)

```
2. Використав метод об'єкта наслідуваного класу в іншому наслідуваному класі.
```Py
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
```
Цей код використовує об'єкт класу videogame і вносить інформацію про гру гравця.
## Висновки
Я навчився використовувати наслідування, освоів використання методу super, навчився працювати з дочірніми класами.