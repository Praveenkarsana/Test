def login(func1):
    def exec():
        print('Enter your name here')
        func1()
        print('Your payment is done')
    return exec


@login
def payment():
    print('Payment of 1000 bucks has been paid to ravi')

payment()

@login
def checkbal():
    print('ypur amount is 10000 remaining')

checkbal()    
    