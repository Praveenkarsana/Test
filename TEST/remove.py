l=list(map(int,input("enter the elements into the list with duplication")))
s=[]
for i in l:
    if i not in s:
        s.append(i)
print(s)        