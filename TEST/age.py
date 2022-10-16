name=input("Enter your name")
age=int(input("Hi  %s,Enter your age:"%name))
if(age<24):
    print("Congratulations %s"%name)
    print("You are eligible for military service")

else:
    print("Sorry %s"%name) 
    print("You are not eligible for military Service")   