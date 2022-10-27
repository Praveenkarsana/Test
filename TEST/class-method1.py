class student:
    clg_name= 'IIT bombay'
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
s1=student('Praveen', '55')
s2=student('Ravikanth','22')
student.obj_count()
print(student.obj_count())        
