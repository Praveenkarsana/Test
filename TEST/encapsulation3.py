class depth:
    def __init__(self, name, age):
        self.name=name
        self.age=age



    def Age(self):
        print('Age:', self.age)

obj=depth('Ravi', 22)
print('Name:',obj.name)
obj.Age()            