rev=0
num=int(input('Enter any number'))
n=num
while (num):
    rem=num%10
    rev=rev*10+rem
    num//=10
print('reverse of number is', rev)
if n==rev:
    print('Palindrome')
else:
    print('Not palindrome')        
