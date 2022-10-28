class parent:                       # parent class
 
    def __init__(self):             # __init__() of parent
        attr1 = 50
        attr2 = 66
 
class child(parent):                # child class
 
    def __init__(self):             # __init__() of child
        parent.__init__(self)       # calling parent’s __init__()
        attr3 = 45
 
test = child()                      # object initiated
 
print (test.attr1)                  # parent attribute called 