class student:
    clg_name= 'BHU'
    counter=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        student.counter=student.counter+1
    def msg(self):
        print(self.name+''+self.age)

    @classmethod
    def obj_count(cls):
        return cls.counter

print(student.clg_name)
s1=student('Praveen', '33')
s2=student('ravikanth','34')
student.obj_count()
print(student.obj_count())
