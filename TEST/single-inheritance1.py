class parent:
   def func1(self):
    print('Hi Ravi.. glad to meet you')


class child(parent):
    def func2(self):
        print('Hi.. glad to meet you ')

test=child()
test.func1()
test.func2()

