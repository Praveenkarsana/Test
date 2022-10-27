class student:
    def __init__(self,name,marks):
        self.name=name
        self.age=marks

    def msg(self):
        print(self.name+''+self.age)

    @staticmethod
    def cal(marks):
        print('marks is',str(marks/600)*100)

s1=student('Praveen','33')
marks=350
name='Rap'
mark1=(str(marks/600)*100)
print(s1.name)
print(s1.age)
s2=student('ravi','marks1')
s1.msg()
s1.cal(marks)
