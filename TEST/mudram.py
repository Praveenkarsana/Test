def sorted(l):
    x=l[:]
    x.sort()
    if l==x:
        return True
    else:
        return False
l=list(input("enter list items").split())
print(sorted(l))            