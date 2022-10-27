class parent:
    def func1(self):
        print('Hello Ravi')

class child(parent):
    def func2(self):
        print('printed bro!')        


test=child()
test.func1()
test.func2()