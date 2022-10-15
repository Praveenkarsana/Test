def sum(num):
    sum=0
    while(num>0):
      sum=sum+num%10
      num=num//10
    print("sum of digits:",sum)
    return sum    


sum(21)