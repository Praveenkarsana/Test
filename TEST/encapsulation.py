#public member
class pub_mod:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def Age(self):
        print('age :', self.age) 

obj=pub_mod('ravi', 33)
print('Name :',obj.name())
obj.Age()      