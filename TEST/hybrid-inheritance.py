class parent1:
    def func1(self):
        print('Hi parent1')

class parent2:
    def func2(self):
        print('Hi Parent 2')

class child1(parent1,parent2):
    def func3(self):
        print('Hi child1')

class child2(child1,parent2):                        
    def func4(self):
        print('Hi child2')

test1=child1()
test2=child2()

test1.func1()
test1.func2()
test1.func3()

test2.func1()
test2.func2()
test2.func4()