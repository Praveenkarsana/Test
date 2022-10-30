from collections.abc import AsyncGenerator


class func:
    def __init__(self, name, age):
        self.name=name
        self.age=age


    def Age(self):
        print('Age:', self.age)

obj=func('Ravi', 27)
print('Name:', obj.name)
obj.Age()
