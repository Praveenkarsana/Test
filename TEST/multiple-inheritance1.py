class parent1:
    def func1(self):
        print('Hi parent1')

class parent2:
    def func2(self):
       print('Hi parent2')


class parent3:
    def func2(self):
        print('Hi parent 3')

class child(parent1, parent2, parent3):
    def func3(self):
        print('Hello my child')

test=child()
test.func1()
test.func2()
test.func3()
print(child.__mro__)                              