class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def msg(self):
        print(self.name+'\t'+self.age)

print('Object 1')
s1=student('Praveen', '26')
print(s1.name)
print(s1.age)
s1.msg()

print('object 2')
s2=student('ravikanth', '27')
print(s2.name)
print(s2.age)
s2.msg()