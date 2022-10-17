def gen_exmp():
	n=1
	yield n
	n+=1
	yield n
	n+=1
	yield n
x = gen_exmp()
print(next(x))
print(next(x))
print(next(x))
print(next(x))



