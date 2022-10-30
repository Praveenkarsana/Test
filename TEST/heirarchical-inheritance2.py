class parent:
    def func1(self):
        print('Hi Parent')

class child1(parent):
    def func2(self):
        print('Hi Child1')

class child2(parent):
    def func3(self):
        print('Hi Child2')

test1=child1()
test2=child2()

test1.func1()
test1.func2()

test2.func1()
test2.func3()