def myfun(**kwargs):
    for key, value in kwargs.items():
        print('%s==%s'%(key, value))

myfun(First='hello', mid='python', last='world') 
       