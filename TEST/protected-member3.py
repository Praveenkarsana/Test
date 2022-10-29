class protected:
    _name= 'Ancient'
    _age= 25
    _job= 'King'

class guard(protected):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)

test=guard()
print('name is', test.name)            
print('Age is', test.age)