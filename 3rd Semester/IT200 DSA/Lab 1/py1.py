x = int(input("Enter no. of Fibonacci numbers to be printed"))
fib0 = 0
i = 1
fib1 = 1 
if x==1:
	print(fib0)
elif x==2:
	print(fib0," ",fib1," ")
else:
	while i<=x:
		if i==1:
			print(" 0")
			i = i+1
		elif i==2:
			print(" 1")
			i = i+1
		else:
			fib=fib0+fib1
			fib0=fib1
			fib1=fib
			print("",fib)
			i = i+1
		
