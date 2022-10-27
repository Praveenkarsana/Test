def login(func1):
    def exec():
        print('Enter your name here')
        func1()
        print('Your payment is done here')
    return exec

@login
def payment():
    print('Payment 1000 paid to ravi')

payment()

@login
def checkbal():
    print('Your Bal')

checkbal()    
