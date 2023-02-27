# Task1
class Device:
    def __init__(self, name,power,size):
        self.name=name
        self.power=power
        self.size=size
class CoffeMachine(Device):
    def __init__(self,name,power,size,quantfunc):
        super().__init__(name,power,size)
        self.quantfunc=quantfunc

    def setPriceCof(self,coffeMacPrice):
        self.__coffeMacPrice=coffeMacPrice

    def __str__(self):
        return f"CoffeMachine {self.name} has {self.quantfunc} functions and its power {self.power}\n"    \
            f'Size of CoffeMachine {self.size}\n'   \
            f'Cost of CoffeMachine {self.__coffeMacPrice} $ '

a=CoffeMachine("Bosh", 5, '30x30x30',3)
a.setPriceCof(1000)
print(a)

# Task2

class Ship:
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        self.name = name


class Frigate(Ship):
    def __init__(self, name, length, width, quantGun):
        super().__init__(name, length, width)
        self.quantGun = quantGun

    def setSpeed(self, maxSpeed):
        self.__maxSpeed = maxSpeed

    def __str__(self):
        return f'Frigete {self.name} has length - {self.length} m & width - {self.width} m\n' \
               f'There are {self.quantGun} gun on a board\n' \
               f'Max speed - {self.__maxSpeed} km/h'


class Destroyer(Ship):
    def __init__(self, name, length, width, quantSailor):
        super().__init__(name, length, width)
        self.quantSailor = quantSailor

    def setShotPerMinute(self, spm):
        self.__spm = spm

    def __str__(self):
        return f'Destroyer {self.name} has length - {self.length} m & width - {self.width} m\n' \
               f'There are {self.quantSailor} sailor on a board\n' \
               f'Max shot per minute - {self.__spm} shots'

class Cruiser(Ship):
    def __init__(self, name, length, width, cruType):
        super().__init__(name, length, width)
        self.cruType = cruType

    def setsysPVO(self,pvo):
        self.__pvo=pvo
    def __str__(self):
        return f'Cruiser {self.name} has length - {self.length} m & width - {self.width} m\n' \
               f'There are {self.__pvo} pvo on a board\n' \
               f'Type of cruiser {self.name} - {self.cruType}'




frigate = Frigate('Beda', 100, 20, 15)
frigate.setSpeed(23)
destroyer = Destroyer('Victory', 50, 40,45)
destroyer.setShotPerMinute(67)
cruiser=Cruiser("Avrora",20,45,'light')
cruiser.setsysPVO('Good')
print(cruiser)
print(frigate)
print('*'*20)
print(destroyer)


class Money:
    def __init__(self,grn,kop):
        self._grn=grn
        self._kop=kop

    def _setGRN(self,grn,kop):
        self._grn=grn
        self._kop=kop
    def _getGrn(self):
        return self._grn

    def _getKop(self):
        return self._kop
    def total(self):
        return f'Total amount {self._grn+self._kop/100}'
class Product(Money):
    def __init__(self,grn,kop,name, price):
        super().__init__(grn,kop)
        self.name=name
        self.price=price
        self.unit=input("Input unit of measure of product 'kg' or 'psc' - ")
    def coast(self):
        self.n=int(input(f"enter quantity of {self.name} which you wont buy - "))
        return f"Total cost for {self.n} {self.name} - {self.price*self.n} "
    def quantCanBuy(self):
        if self.unit=='kg':
            return f'For money witch you have, You can bay {round((self._grn + self._kop/100)/self.price,3)} kg of {self.name}'
        elif self.unit == 'psc':
            if self.price>(self._grn+self._kop/100):
                return f'You dont have enough money to buy at list one psc of {self.name}.\n'   \
                    f'You need add {round(self.price-self._grn+self._kop/100,2)} and can buy 1 {self.name}'
            else:
                return f'For money witch you have You can bay {(self._grn+self._kop/100)//self.price} psc of {self.name}.\n'   \
                f'And you steel have {round(self._grn+self._kop/100-((self._grn+self._kop/100)//self.price)*self.price, 2)} grn'


money=Money(15,16)
money._setGRN(20,34)
# print(money.total())
product=Product(117,30,'banan', 50)
# print(product.total())
# #print(product.coast())
#
# print(product.quantCanBuy())
print(product._getGrn())
print(product._getKop())