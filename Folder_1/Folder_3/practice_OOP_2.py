
#ss;dfs;kldfksf

#121212

#Task1
class Peopl:

    count=0

    def __init__(self, fullName, birthDay, phoneNum, city, country, address):
        Peopl.count+=1
        self.fullName = fullName
        self.birhDay = birthDay
        self.phoneNum = phoneNum
        self.city = city
        self.country = country
        self.address = address

    def __str__(self):
        return f'{self.fullName} is people\n'  \
                f'was born {self.birhDay}\n'   \
                f'Phone - {self.phoneNum}\n'  \
                f'Live in {self.city}\n'  \
                f'From {self.country}\n'  \
                f'My address  {self.address}\n'

    def __lt__(self, other):
        if self.birhDay<other.birhDay:
            return f'{self.fullName} is older'
        else:
            return f'{self.fullName} is younger'

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
    @staticmethod
    def quntityHuman():
        return Peopl.count

people1=Peopl('Dima',1984,380971234567,'KR', "Ukraine",'Street 12/23')
people2=Peopl('Dima',1984,380971234567,'KR', "Ukraine",'Street 12/23')
# people1.setkeyWord('python')
# people1.setID(1234)
# print(people1.getInfo())
people2=Peopl('Max', 1979,30983434124, 'Kyiv', 'Ukraine', 'Pobedy 1/1')
# print(people2)
# print(people1>people2)
print(Peopl.quntityHuman())

#Task2
# #
# class City:
#     def __init__(self,nameCity,region, country, citizen, index, phoneCod):
#         self.nameCity=nameCity
#         self.region=region
#         self.country=country
#         self.citizen=citizen
#         self.index=index
#         self.phoneCod=phoneCod
#
#     def __str__(self):
#         return f'{self.nameCity} is great city. its situated in {self.country}, {self.region} region. Quantity of citizen  -{self.citizen} \n'  \
#                f'If you want sand mail to one of {self.citizen} citizen use index - {self.index} or phone code {self.phoneCod} when you call someone'
#     def __le__(self, other):
#         if self.citizen<= other.citizen:
#             return f'In {self.nameCity} more people then in {other.nameCity}'
#
#     def infoCity(self):
#         return f"{self.nameCity} is great city. its situated in {self.country}, {self.region} region. Quantity of citizen  -{self.citizen}"
#     def mailCity(self):
#         return f'If you want sand mail to one of {self.citizen} citizen use index - {self.index} or phone code {self.phoneCod} when you call someone'
#     def mayorCity(self,mayor):
#         return f"Our mayor {mayor} is best of the best!!"
#
#
# myCity=City('KR','Dnipto','Ukraine',500000,500,'0564')
# city2=City('NY', 'Columbia d-t', 'USA', 4000000,400, '908' )
# print(city2)
# print(myCity.infoCity())
# print(myCity.mailCity())
# print(myCity.mayorCity('Vilkul'))
# print(myCity<=city2)
# #
# #
# # # #Task3
#
# class Country:
#     def __init__(self, nameCountry, continent, population, phoneCode, phoneNum, capital, city1,city2):
#         self.nameCountry=nameCountry
#         self.continent=continent
#         self.population=population
#         self.phoneCode=phoneCode
#         self.capital=capital
#         self.city1=city1
#         self.city2 = city2
#         self.phoneNum=phoneNum
#
#     def __str__(self):
#         return f'My native country is {self.nameCountry}. It is situated on continent {self.continent}. Capital of country - {self.capital}\n '    \
#                 f'To call someone in {self.nameCountry} please enter code - {self.phoneCode}. for example - ({self.phoneCode})({self.phoneNum})'
#
#     def infoCountry(self):
#         return f'My native country is {self.nameCountry}. It is situated on continent {self.continent}. Capital of country - {self.capital}'
#
#     def conectionWithCountry(self,phoneNum):
#         return f'to call someone in {self.nameCountry} please enter code - {self.phoneCode}. for example - ({self.phoneCode})({phoneNum})'
#     def populationInfo(self):
#         return f'Population of {self.nameCountry} is {self.population} people'
#     def visitInfo(self):
#         print(f'most popular cities in {self.nameCountry} are {self.city1}, {self.city2}.')
#         city3=input('Input city which you recommend to visit - ')
#         return f'Also, we can recommend {city3}'
#
# myCountry=Country('Ukraine', "EurAsia", 40000000, '+38', '0671234567','Kyiv', 'Lviv', 'Odessa')
# print(myCountry)
# print(myCountry.infoCountry())
# print(myCountry.conectionWithCountry('0671234567'))
# print(myCountry.populationInfo())
# print(myCountry.visitInfo())
#
# #
# #
# # # #Task4
# #
# class Fraction:
#     x=0
#     y=0
#     # def __init__(self,x,y):
#     #     self.x=x
#     #     self.y=y
#
#     def __str__(self):
#         return f'we have Point({self.x},{self.y})'
#
#     def __gt__(self, other):
#         if self.x>other.y:
#             return f"X more"
#         else:
#             return f"Y more then X"
#     def inputNum(self):
#         self.x=int(input('input number "X" - '))
#         self.y=int(input('input number "Y" - '))
#     def showFraction(self):
#         return f'Your fraction - {self.x}/{self.y}'
#
#     def calculationNum(self):
#         g=input("Chose action with your numbers - '+,-,*,/' - ")
#         if g=='+':
#             return self.x+self.y
#         elif g=='-':
#             return self.x-self.y
#         elif g=='*':
#             return self.x*self.y
#         elif g=='/':
#             return self.x/self.y
#         else:
#            'Wrong choise !'
# num1=Fraction()
# num2=Fraction()
# num1.inputNum()
# num2.inputNum()
# print(num1)
# print(num2)
# print(num1>num1)
# #
# # #Task 5
# #
# class Watch:
#
#     def __init__(self, name,produce, year, price, type):
#         self.name=name
#         self.producer=produce
#         self.year=year
#         self.price=price
#         self.type=type
#
#     def __str__(self):
#         return f'I use {self.name} watch\n'   \
#                 f'it was produced by {self.producer} in {self.year}\n'    \
#                 f'Price - {self.price} $\n'   \
#                 f'Type of this watch  - {self.type}'
#     def __gt__(self, other):
#         if self.price>other.price:
#             return f'{self.name} cost more then {other.name}'
#     def __le__(self, other):
#         if self.year<=other.year:
#             return f'{self.name} older then {other.name}'
#
# clock1=Watch('orion', 'ttt', 2000, 2000, 'hand')
# clock2=Watch('apple', 'fgf', 2020, 2010, 'hand')
# print(clock1)
# print('-'*20)
# print(clock2)
# print('-'*20)
# print(clock2>clock1)
# print(clock1<=clock2)
# #
# #
# # # #Task6
# # #
# class Website:
#
#     def __init__(self, name, eAddress, siteDiscription):
#         self.name=name
#         self.eAddress=eAddress
#         self.siteDiscription=siteDiscription
#
#     def __str__(self):
#         return f'When you come on your site {self.name} using address {self.eAddress}\nYou will be able to know {self.siteDiscription}'
#     def __len__(self):
#         return len(self.siteDiscription)
#     def isSiteAbout(self):
#         a=input('Is on site information about - ')
#         for i in range(len(self.siteDiscription)-len(a)+1):
#             if a.lower()==self.siteDiscription[i:(i+len(a))].lower():
#                 return f'Yes, you can find some information about "{a}"'
#
# site=Website('Python', "www.python.com", 'Python is a programming language that lets you work quickly and integrate systems more effectively')
# print(site)
# print(site.isSiteAbout())
