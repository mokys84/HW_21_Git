#Task1
class Car:
    def __init__(self,model,dataProd, vurob, motorVol, color, price):
        self.model=model
        self.dataProd=dataProd
        self.vurob=vurob
        self.motorVol=motorVol
        self.color=color
        self.price=price

    def infoCar(self):
        return f"Price for basic equipment {self.vurob} {self.model} with characteristic below - {self.price}$\n" \
               f'Production data - {self.dataProd}\n' \
               f'Volume of engine - {self.motorVol}\n' \
               f'Color - {self.color}'

    def __str__(self):
        return f"Price for basic equipment {self.vurob} {self.model} with characteristic below - {self.price}$\n" \
        f'Production data - {self.dataProd}\n' \
        f'Volume of engine - {self.motorVol}\n' \
        f'Color - {self.color}'
    def choseEquipment(self):
        print("If you want change basic equipment, please enter your mean!")
        v=float(input("Volume of engine - "))
        c=input('Color - ')
        p = int(input("Production data - "))
        if 2.0<v<=2.4 and 2015<p<=2018 and (c!="black" or c!= "white"):
            self.price=12000
            return f"Price for {self.vurob} {self.model} with characteristic below - {self.price}$\n" \
               f'Production data - {p}\n' \
               f'Volume of engine - {v}\n' \
               f'Color - {c}'
        elif v>2.4 and p > 2018 and (c != "black" or c != "white"):
            price = 15000
            return f"Price for {self.vurob} {self.model} with characteristic below - {price}$\n" \
                f'Production data - {p}\n' \
                f'Volume of engine - {v}\n' \
                f'Color - {c}'
    def __lt__(self, other):
        if self.price<other.price:
            dif=other.price-self.price
            return f'{self.vurob} {self.model} cost less then {other.vurob} {other.model} on {dif} $'
        else:
            dif = self.price-other.price
            return f'{other.vurob} {other.model} cost less then {self.vurob} {other.model} on {dif} $'

car1=Car('A5', 2015, 'Audi', 2.0, 'black', 10000)
car2=Car('Touareg', 2017, 'WV', 2.4, 'White', 15000)
print(car2)
print(car1<car2)



#Task2

class Book:
    def __init__(self, nameBook,year,publisher, genre,author,price ):
        self.nameBook=input("Input name of book - ")
        self.year=year
        self.publisher=publisher
        self.genre=genre
        self.author=author
        self.price=price
    def __str__(self):
        return f'Book info: Title - {self.nameBook}, author - {self.author}, publisher - {self.publisher}, was published in {self.year} year\n' \
               f'Writen in genre {self.genre}.\n' \
               f'If you want buy it you should pay {self.price}$'

    def infoBook(self):
        return f'Book info: Title - {self.nameBook}, author - {self.author}, publisher - {self.publisher}, was published in {self.year} year\n'    \
            f'Writen in genre {self.genre}.\n'  \
            f'If you want buy it you should pay {self.price}$'
    def __gt__(self, other):
        if self.price>other.price:
            return f'{self.nameBook} {self.author} cost more then {other.nameBook} {other.author}'
        else:
            return f'{other.nameBook} {other.author} cost more then {self.nameBook} {self.author}'
    def __add__(self, other):
        sum=self.price+other.price
        return f'To buy both book you should pay {sum} $'

book1=Book('', 2020, 'SinceHouse', "ITbook", 'Smith', 100)
book2=Book('', 2021, 'SinceHouse', "ITbook", 'Black', 120)
print(book2)
print(book1.infoBook())
print(book1>book2)
#
# #Task3
#
class Stadium:
    def __init__(self, nameStadium, openData, country, city, seats, team ):
        self.nameStedium=input('nameStadium - ')
        self.openData=openData
        self.country=country
        self.seats=seats
        self.team=team
        self.city=city

    def __str__(self):
        return f"Home stadium of {self.team} is {self.nameStedium}. it was build in {self.openData}\n"  \
                    f"It is situated in {self.city} {self.country}\n"   \
                    f"max seats - {self.seats} "
    def infoStedium(self):
        return f"Home stadium of {self.team} is {self.nameStedium}. it was build in {self.openData}\n"  \
            f"It is situated in {self.city} {self.country}\n"   \
            f"max seats - {self.seats} "

    def __gt__(self, other):
        if self.seats>other.seats:
            return f'{self.nameStedium} can accommodate more people then {other.nameStediun}'
        else:
            return f'{other.nameStedium} can accommodate more people then {self.nameStedium}'

team1=Stadium('', 1927, "Ukraine", "Kyiv", 40000,"Dinamo Kyiv")
team2=Stadium('', 1956, "Spane", "Barcelona", 40900,"Barca")

print(Stadium.infoStedium(team1))
print(team2)
print(team1>team2)
