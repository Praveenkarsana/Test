def room(func):
    print('your value is low')
    func()

def come():
    print('but there is a chance')    

def go():
    print('read above comment')

room(come)
room(go)        