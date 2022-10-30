class orbit:
    _name='Heer'
    _age=23
    _job='Employee'
    
class elipse(orbit):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)


obj=elipse()
print('Name is:', obj.name)
print('Age is:', obj.age)