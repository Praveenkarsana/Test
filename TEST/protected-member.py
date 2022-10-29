class outlook:
    _name='Jain'
    _age=55
    _job='priest'

class inlook(outlook):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)

obj=inlook()
print('Name:', obj.name)
print('Name:', obj.age)            