def display(*folk):
    for i in folk:
        print(i)
    print(folk[2]) 

names=['paw','rain','ravi']
names=('paw','rain','ravi')
display(*names)       