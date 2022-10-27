def login(func1):
    def exec():
        print("Enter the amount")
        func1()
        print('Your payment is done')
    return exec

@login
def payment():
    print('1000 is paid to praveen')

payment()

@login
def checkbal():
    print('Your balance is nill')

checkbal()    
