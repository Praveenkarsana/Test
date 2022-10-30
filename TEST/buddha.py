s1=input("Enter First String")
s2=input("Enter Second String")
if(len(s1)==len(s2)):
    print("Strings are with same length")
    result=""
    for i in range(len(s1)):
        result=result+(s2[i]+s1[i])
    print(result) 
else:
    print("Strings are with different length ")       