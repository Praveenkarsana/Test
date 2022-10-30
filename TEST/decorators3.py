def login(func1):
    def exec():
        print("Enter your amount here")
        func1()
        print('Your amount has been initiated for payment')
    return exec()


@login
def payment():
    print('100 rupees is been paid to ravi')

payment()


@login
def checkbal():
    print('Your balance is')

checkbal()


