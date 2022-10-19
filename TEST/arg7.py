def display(name,*args,**kwarge):
    print(name)
    for i in args:
        print(i)

name='paw'
item=['phone','cool','magnet','sneeker']
display(name,*item)        