class rectangle:
    __length=0
    __breadth=0
    def __init__(self):
        self.__length=9
        self.__breadth=8
        print(self.__length)
        print(self.__breadth)

rect=rectangle()     
print(rect.length)
print(rect.breadth)