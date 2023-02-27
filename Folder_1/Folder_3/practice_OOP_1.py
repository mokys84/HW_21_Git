

#Task1
class Peopl:
    def __init__(self, fullName, birthDay, phoneNum, city, country, address):
        self.fullName = fullName
        self.birhDay = birthDay
        self.phoneNum = phoneNum
        self.city = city
        self.country = country
        self.address = address

    def getInfo(self):                                  #Загальна інформація
        return  f'{self.fullName} is people\n'  \
                f'was born {self.birhDay}\n'   \
                f'Phone - {self.phoneNum}\n'  \
                f'Live in {self.city}\n'  \
                f'From {self.country}\n'  \
                f'My address  {self.address}\n'
    def setkeyWord(self,keyWord):                       # встановити кодове слово
        self.__keyWord=keyWord

    def setID(self,personID):                           # внести персональні даннні
        self.__personID=personID

    def getID(self):                                    # показати персональні данні за умови правильного вводу кодового слова
        b=input("Input your keyword - ")
        if b==self.__keyWord:
            return f'Your personal ID - {self.__personID}'
        else:
            return "Wrong Key Word"

a=input('Input name - ')
people1=Peopl(a,1984,380971234567,'KR', "Ukraine",'Street 12/23')
people1.setkeyWord('python')
people1.setID(1234)
print(people1.getID())
print(people1.getInfo())


#Task2

class City:
    def __init__(self,nameCity,region, country, citizen, index, phoneCod):
        self.nameCity=nameCity
        self.region=region
        self.country=country
        self.citizen=citizen
        self.index=index
        self.phoneCod=phoneCod

    def infoCity(self):
        return f"{self.nameCity} is great city. its situated in {self.country}, {self.region} region. Quantity of citizen  -{self.citizen} people"
    def mailCity(self):
        return f'If you want sand mail to one of {self.citizen} citizen use index - {self.index} or phone code {self.phoneCod} when you call someone'
    def mayorCity(self,mayor):
        return f"Our mayor {mayor} is best of the best!!"


myCity=City('KR','Dnipto','Ukraine',500000,500,'0564')
print (myCity.infoCity())
print(myCity.mailCity())
print(myCity.mayorCity('Vilkul'))

#
# #Task3

class Country:
    def __init__(self, nameCountry, continent, population, phoneCode, capital, city1,city2):
        self.nameCountry=nameCountry
        self.continent=continent
        self.population=population
        self.phoneCode=phoneCode
        self.capital=capital
        self.city1=city1
        self.city2 = city2

    def infoCountry(self):
        return f'My native country is {self.nameCountry}. It is situated on continent {self.continent}. Capital of country - {self.capital}'

    def conectionWithCountry(self,phoneNum):
        return f'to call someone in {self.nameCountry} please enter code - {self.phoneCode}. for example - ({self.phoneCode})({phoneNum})'
    def populationInfo(self):
        return f'Population of {self.nameCountry} is {self.population} people'
    def visitInfo(self):
        print(f'most popular cities in {self.nameCountry} are {self.city1}, {self.city2}.')
        city3=input('Input city which you recommend to visit - ')
        return f'Also, we can recommend {city3}'

myCountry=Country('Ukraine', "EurAsia", 40000000, '+38', 'Kyiv', 'Lviv', 'Odessa')
print(myCountry.infoCountry())
print(myCountry.conectionWithCountry('0671234567'))
print(myCountry.populationInfo())
print(myCountry.visitInfo())

# #Task4

class Fraction:
    x=0
    y=0
    def inputNum(self):
        self.x=int(input('input number "X" - '))
        self.y=int(input('input number "Y" - '))
    def showFraction(self):
        return f'Your fraction - {self.x}/{self.y}'

    def calculationNum(self):
        g=input("Chose action with your numbers - '+,-,*,/' - ")
        if g=='+':
            return self.x+self.y
        elif g=='-':
            return self.x-self.y
        elif g=='*':
            return self.x*self.y
        elif g=='/':
            return self.x/self.y
        else:
           return 'Wrong choise !'
num1=Fraction()
num1.inputNum()
print(num1.showFraction())
print(num1.calculationNum())


