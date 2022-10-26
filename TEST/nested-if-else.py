rank=int(input('Enter Your Marks:'))
if rank>=90:
    print('A++')
else:
    if rank>=80:
        print('A') 
    else:
        if rank>=70:
            print('B')
        else:
            if rank>=60:
                print('C')
            else:
                print('Fail')
                        
