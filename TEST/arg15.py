def display(name,*args,**kwargs):
    print(name)
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(f"{k} is a {v}") 

name='class'
item=['phone','cool','magnet','sneeker']
d={'praveen':'instruct','ravi':'student','shagun':'student3'}
display(name,*item,**d)           