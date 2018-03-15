# assign two variables
a,b = 0,1

# loop starts
while a < 10 :
	print a
	a,b = b, a+b
# loop ends 
# loop statements should be properly indended by tab or equal space




# define by funcation

def fib(n):
	a,b = 0,1
	while a < n :
		print a
		a,b = b, a+b


# call the defined function fib
fib(100)

print "\n next fibo series ************* \n"

# assign to variable
f = fib
f(10)

