def func(*heee):
    for arg in heee:
        print(arg)
        yield arg

var=func('hello','priye')
print(var)        
