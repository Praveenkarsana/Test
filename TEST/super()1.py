class parent:
    def display(self):
        print('Hi Parent')

class child(parent):
    def display(self):
        super().display()
        print('Hi child')

test=child()
test.display()                