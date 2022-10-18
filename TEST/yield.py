def getFibonacci():
    a, b = 0, 1

    while True:
        yield b
        b = a + b
        a = b - a

for num in getFibonacci():

    if num > 100:
        break
    print(num)