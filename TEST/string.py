s1=input("Enter first string")
s2=input("Enter second string")
if(len(s1)==len(s2)):
   print("strings are with same length")
   result=" "
   for i in range(len(s1)):
      result=result+(s1[i]+s2[i])
   print(result)
else:
    print("strings are with diffrent length")   
