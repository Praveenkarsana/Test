class information:
    __local=0
    __global=0
    def __init__(self):
        self.__local=7
        self.__global=9
        print(self.__local)
        print(self.__global)


info=information()
print(info.__local)
print(info.__global)        