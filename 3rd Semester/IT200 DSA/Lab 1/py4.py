x = int(input("Enter two numbers"))
y = int(input())
i = 1
gcd = 1

while i<x or i<y:
	if (x%i)==0 and (y%i)==0 :
		gcd = i
	i = i+1

print("GCD of ",x," and ",y," is ",gcd)


