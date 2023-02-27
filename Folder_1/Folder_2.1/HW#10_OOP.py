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
            return print(f"Price for {self.vurob} {self.model} with characteristic below - {price}$" \
                         f'Production data - {p}  ' \
                         f'Volume of engine - {v} ' \
                         f'Color - {c}')


car1=Car('A5', 2015, 'Audi', 2.0, 'black', 10000)
print(car1.infoCar())
print(car1.choseEquipment())



#Task2

class Book:
    def __init__(self, nameBook,year,publisher, genre,author,price ):
        self.nameBook=input("Input neme of book - ")
        self.year=year
        self.publisher=publisher
        self.genre=genre
        self.author=author
        self.price=price

    def infoBook(self):
        return f'Book info: Title - {self.nameBook}, author - {self.author}, publisher - {self.publisher}, was published in {self.year} year\n'    \
            f'Writen in genre {self.genre}.\n'  \
            f'If you want buy it you should pay {self.price}$'

book1=Book('Python', 2020, 'SinceHouse', "ITbook", 'Smith', 100)

print(book1.infoBook())

#Task3

class Stadium:
    def __init__(self, nameStadium, openData, country, city, seats, team ):
        self.naneStedium=input('nameStadium')
        self.openData=openData
        self.country=country
        self.seats=seats
        self.team=team
        self.city=city
    def infoStedium(self):
            return f"Home stadium of {self.team} is {self.naneStedium}. it was build in {self.openData}\n"  \
                    f"It is situated in {self.city} {self.country}\n"   \
                    f"max seats - {self.seats} "

team1=Stadium('', 1927, "Ukraine", "Kyiv", 40000,"Dinamo Kyiv")
team2=Stadium('', 1956, "Spane", "Barcelona", 40900,"Barca")

print(Stadium.infoStedium(team1))
print(Stadium.infoStedium(team2))