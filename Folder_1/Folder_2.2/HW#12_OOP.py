
#Task1
class Fraction:
    quant=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
        Fraction.quant+=1
    def __str__(self):
        return f'({self.x},{self.y})'
    def changNum(self):
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

    @staticmethod
    def quantFrac():
        return Fraction.quant
num1=Fraction(2,3)
num3=Fraction(2,3)
num2=Fraction(2,3)
num4=Fraction(2,3)
num1.changNum()
print(Fraction.quantFrac())

#Task2

class CelFar:
    quant=0
    @staticmethod
    def celToFar():
        x=float(input("Enter temperature in 'C - "))
        CelFar.quant+=1
        return f"Temperature in 'F - {x*9/5+32}"

    @staticmethod
    def farToCel():
        x = float(input("Enter temperature in 'F - "))
        CelFar.quant += 1
        return f"Temperature in 'C - {(x-32)*5/9}"

    @staticmethod
    def quantity():
        return CelFar.quant

print(CelFar.celToFar())
print(CelFar.farToCel())
print(CelFar.quantity())
print(CelFar.celToFar())
print(CelFar.farToCel())
print(CelFar.quantity())

#Task3

class BritishMetric:
    @staticmethod
    def kilomil():
        x = float(input("Enter distance in kilometer  - "))
        return f'Distance in mile - {round(x*0.6214,3)}'
    @staticmethod
    def milkilo():
        x = float(input("Enter distance in mile  - "))
        return f'Distance in kilometer - {round(x/0.6214,3)}'
    @staticmethod
    def metrfoot():
        x = float(input("Enter distance in meter  - "))
        return f'Distance in foot - {round(x * 3.281,3)}'

    @staticmethod
    def footmetr():
        x = float(input("Enter distance in foot  - "))
        return f'Distance in meter - {round(x / 3.281,3)}'

    @staticmethod
    def grampound():
        x = float(input("Enter weight in kilogram   - "))
        return f'Weight in pounds - {round(x * 2.205,3)}'

    @staticmethod
    def poundgram():
        x = float(input("Enter weight in pounds   - "))
        return f'Weight in kilogram - {round((x * 2.205),2)}'

print(BritishMetric.grampound())
print(BritishMetric.metrfoot())