class mate:
    pass
a=mate
print(a)
a.name='Praveen'
print(a.name)
a.position= 'Tutor'
print(a.position)

b=mate
b.name= 'Ravikanth chavan'
print(b.name)
b.position= 'Student'
print(b.position)

mate.no_cls=19
print(mate.no_cls)
print(a.no_cls)
print(b.no_cls)


a.no_cls=18
print(a.no_cls)
print(b.no_cls)