class Basic:
    pass
a=Basic()
a.name= 'Praveen'
print(a.name)
a.position= 'Tutor'
print(a.position)

b=Basic
b.name= 'Ravikanth'
print(b.name)
b.position= 'Student'
print(b.position)

Basic.no_cls=11
print(Basic.no_cls)
print(a.no_cls)
print(b.no_cls)

b.no_cls=22
print(b.no_cls)

print(a.__dict__)
print(Basic.__dict__)