def common(a,b):
    result=False
    for i in a:
        for j in b:
            if i==j:
                result=True
    print(result)
a=[12,54,78,36,74]
b=[53,77,61,77,54]
common(a,b)                