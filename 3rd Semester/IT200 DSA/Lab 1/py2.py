x = int(input("Enter number to check if it is prime:"))
i = 1
count = 0
while i < x:
	if (x%i)==0:
		count = count+1
	i = i+1
if count==1:
	print("The number is prime")
else:
	print("The number is not prime. The number of factors = ",count)
			
