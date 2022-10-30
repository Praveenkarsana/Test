class parent:
    def func1(self):
        print('hello ravi')

class child(parent):
    def func2(self):
        print('glad ! to meet you')

test=child()
test.func1()
test.func2()        
