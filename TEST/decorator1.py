# def dec1(func1):
#     def exec():
#         print('Executing now')
#         func1()
#         print('Execution is Done')
#     return exec    

# @dec1
# def display():
#     print('I am here to display')

# display()

def login(func1):
    def exec():
        print(" Enter your amount")
        func1()
        print('Your Payment is done')
    return exec


@login()
def payment():
    print('Paying 1000 Rupees to Ravikanth')

payment()    




