class grandparent:
    def func1(self):
        print('Hi grandparents')


class parent(grandparent):
    def func2(self):
        print('Hi parents') 


class child(parent):
    def func3(self):
        print('Hi child')


test=child()
test.func1()
test.func2()
test.func3()
print(child.__mro__)