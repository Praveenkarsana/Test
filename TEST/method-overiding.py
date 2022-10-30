class parent:
    def __init__(self):
            attr1=55
            attr2=99

class child(parent):
    def __init__(self):
        parent.__init__(self)
        attr3=66

test=child()
print(test.attr1)
