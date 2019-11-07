def fib(n):
	x=[0,1]
	for i in range(n):
		x.append(x[i]+x[i+1])
	return (x)
y=fib(100)

