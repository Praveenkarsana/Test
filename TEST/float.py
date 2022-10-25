p=float(input('Enter Your Principal Amount'))
t=float(input('Enter Your Time Period'))
r=float(input('Enter Your Rate of Interest'))
si=p*r*t/100
totalamount=p+si
print("*"*30)
print("Interest on amount", si)
print("*"*30)
print("Total amount=", totalamount)
print("*"*30)