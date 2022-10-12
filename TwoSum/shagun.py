n = [2, 7, 11, 15]
t = 26
c = 0
def sum():
    for x in n:
        for y in n:
            if x+y==t:
                # c = x+y
                print(n.index(x),n.index(y))
                return c
                
sum()