def common(a,b):
    count=0
    for i in a:
        for j in b:
            if i==j:
                count+=1
    if(count>=3):
        print("True")
    else:
        print("False")

a=[12,54,78,36,74] 
b=[12,54,78,37,73]                       