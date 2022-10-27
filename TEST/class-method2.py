class student:
    clg_name= 'Gulbarga University'
    counter=0
    def __init__(self, name, age):
        self.name=name
        self.age=age
        student.counter=student.counter+1
    def msg(self):
        print(self.name+''+self.age)

    @classmethod
    def obj_count(clg):
        return clg.counter

print(student.clg_name) 
s1=student('ravikanth', '66')
s2=student('praveen', '33')
student.obj_count()
print(student.obj_count())               