num=int(input('Enter Any Number:'))
count=1
s_even=s_odd=0
while (count<=num):
    if (count%2)==0:
        s_even+=count
    else:
        s_odd+=count
    count+=1
print('Sum of all even number',s_even)
print('Sum of odd number ',s_odd)            
