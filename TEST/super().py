class parent:
    def display(self):
        # super().display()
        print('hello parent')

class child(parent):
    def display(self):
        super().display()
        print("hello child")

test=child()
test.display() 