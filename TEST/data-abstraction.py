from abc import ABC, abstractmethod
class car(ABC):
   def mileage(self):
    pass

class Tesla(car):
    def mileage(self):
        print('The Speed is 22mp/h')

class Maruti(car):
    def mileage(self):
        print('The speed is 44mp/h')

class tata(car):
    def mileage(self):
        print('The speed is 55mp/h')

t=Tesla()
t.mileage()

m=Maruti()
m.mileage()

t=tata()
t.mileage()

