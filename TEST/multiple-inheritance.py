class parent1:
    def func1(self):
        print('Hi parent 1')

class parent2:
    def func2(self):
        print('hi parent 2')

class parent3:
    def func2(self):
        print('Hi parent3')

class child(parent1, parent2, parent3):
    def func3(self):
        print('Hello child')

test=child()
test.func1()
test.func2()
test.func3()     
print(child.__mro__)                       