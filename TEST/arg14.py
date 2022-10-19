def myfun(*args,**kwargs):
    print("*args",args)
    print("kwargs",kwargs)

myfun('hello','python','world',First='hello', mid='python', last='world')    