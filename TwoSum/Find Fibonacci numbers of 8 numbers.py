#Find Fibonacci numbers of 8 numbers
#Ex for finbonacci:
#[0,1,1,2,3,5]

#from tkinter import N


def gen_exmp():
    n=0
    yield n
    n+=1
    yield n
    yield n
    n+=1
    yield n
    n+=1
    yield n
    n+=2
    yield n
    n+=3
    yield n
    n+=5
    yield n
    n+=8
    yield n
    n+=13
    yield n
    n+=21
    yield n
    n+=34
    yield n
    n+=55
    yield n
    n+=89
    yield n
x = gen_exmp()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))