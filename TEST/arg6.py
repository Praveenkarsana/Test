def orders(name,*items):
    print('items purchased by customer',name)
    for i in item:
        print('\t\t',i)

name='paw'
item=['phone','cooling','magnet','sneekr']
orders(name,*item)        