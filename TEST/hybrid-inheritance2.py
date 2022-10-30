class parent1:
    def func1(self):
        print('parent 1')
        

class parent2:
    def func2(self):
        print('Parent 2')        


class child1(parent1,parent2):
    def func3(self):
        print('hello child1')

class child2(child1,parent2):
    def func4(self):
        print('hello child2')

test1 = child1()                          # object created
test2 = child2()
 
test1.func1()                       # child1 calling parent1 method
test1.func2()                       # child1 calling its own method
 
test2.func1()                       # child2 calling parent1 method
test2.func2()                       # child2 calling parent2 method
test2.func3()                       # child2 calling child1 method
test2.func4()                       # child2 calling its own method
 
 

 