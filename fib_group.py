# A function to return a range Fibonacci numbers

def fibonacci(n):
    i=0;
    j=1;
    ls=[]
    ls.append(i)
    ls.append(j)
    while i+j<n:
        fib=i+j;
        ls.append(fib)
        i=j;
        j=fib
    return ls
print(fibonacci(20))

def fib(n):
	 n = 0
	 p = []
	 for i in range(0,n):
	 	n +=i
	 	p.append(i)
	 return p
print fib(10)