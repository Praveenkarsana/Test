def myfun(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)

args=('hello','python','world')
myfun(*args)
kwargs={'arg1':'hello','arg2':'python','arg3':'world'}
myfun(**kwargs)    