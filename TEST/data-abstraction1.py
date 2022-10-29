from abc import ABC, abstractmethod
class car(ABC):
    def mileage(self):
        pass

class tata(car):
    def mileage(self):
        print('88mp/h')

class mahindra(car):
    def mileage(self):
        print('99mp/h')            

t=tata()
t.mileage()

m=mahindra()
m.mileage()