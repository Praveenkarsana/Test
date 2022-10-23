def login(func1):
    def exec():
        print('Enter Your Amount')
        func1()
        print('Your Payment is Done')
    return exec()


@login
def  payment():
    print('Paying 1000 Rupees to Ravikanth')



payment()
