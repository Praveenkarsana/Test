class parent1:
    def func1(self):
        print('Parent1')

class parent2:
    def func2(self):
        print('Parent2')

class child1(parent1, parent2):
    def func3(self):
        print('Child1')

class child2(child1, parent2):
    def func4(self):
        print('Child2')

test1=child1()
test2=child2()

test1.func1()

test1.func3()

test2.func2()

test2.func4()