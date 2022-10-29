class classic:
    _name='Ravikanth'
    _age=27
    _occupation='Student'

class cult(classic):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._occupation)    

test=cult()
print('name is', test.name)
print('age is', test.age)        