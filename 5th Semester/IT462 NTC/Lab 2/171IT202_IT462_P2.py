import random
import math

def primeFactors(n,factors):  
    if (n % 2 == 0):
        factors.append(2) 
    while (n % 2 == 0): 
        n = n / 2 
          
    for i in range(3,int(math.sqrt(n)+1),2):
        if (n % i == 0):
            factors.append(int(i)) 
        while (n % i == 0): 
            n = n / i
    if (n > 2): 
      factors.append(int(n))
  
def square_and_multiply(a,r,n):
    y = 1
    b = format(r,"b")
    nb = len(b)
    for i in range(nb-1,-1,-1):
        if int(b[i])==1:
            y = (a*y)%n
        a = (a*a)%n
    return y

def file_write(strings):
    return
  
def lucas(n):
    factors = [] 
    primeFactors(n - 1, factors)
    a = random.randint(2,n-1)
    print("a:",a)
    print("Prime factors of",n-1,"are:",str(factors)[1:-1])

    if (square_and_multiply(a, n - 1, n) != 1): 
        print(n,"is not prime.")
        return

    for i in range(len(factors)): 
        if (square_and_multiply(a, int((n - 1) / factors[i]), n) == 1): 
            print(n,"may not be prime.")
            return

    print(n,"is prime.")

def main():
	n = int(input("Enter any positive integer: "))

	# Base cases:

	if (n < 1):
		print(n,"is not positive! Terminating")
		return 0

	if (n == 1):
		print(n,"is not prime.")
		return 0

	if (n == 2) or (n == 3):
		print(n,"is prime.")
		return 0

	if (n > 2) and (n%2 == 0):
		print(n,"is even and greater than 2, and thus not prime.")
		return 0

	lucas(n)

if __name__=='__main__':
	main()
