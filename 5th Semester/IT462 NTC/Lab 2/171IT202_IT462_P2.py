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

def file_ops(lines):
    f = open("output.txt","a")
    for line in lines:
        print(line)
        f.write(line + '\n')
    f.write('\n');
    f.close()
    return
  
def lucas(n):
    factors = [] 
    lines = []
    primeFactors(n - 1, factors)
    a = random.randint(2,n-1)
    lines.append(("a: " + str(a)))
    lines.append(("Prime factors of " + str(n-1) + " are: " + str(factors)[1:-1]))

    if (square_and_multiply(a, n - 1, n) != 1): 
        lines.append((str(n) + " is not prime."))
        file_ops(lines)
        return

    for i in range(len(factors)): 
        if (square_and_multiply(a, int((n - 1) / factors[i]), n) == 1): 
            lines.append((str(n) + " may not be prime."))
            file_ops(lines)
            return

    lines.append((str(n) + " is prime."))
    file_ops(lines)

def main():
    n = int(input("Enter any positive integer: "))
    lines = []
    
    if (n < 1):
        lines.append((str(n) + " is not positive! Terminating"))
        file_ops(lines)
        return 0
    if (n == 1):
        lines.append((str(n) + " is not prime."))
        file_ops(lines)
        return 0
        
    if (n == 2) or (n == 3):
        lines.append((str(n) + " is prime."))
        file_ops(lines)
        return 0
    
    if (n > 2) and (n%2 == 0):
        lines.append((str(n) + " is even and greater than 2, and thus not prime."))
        file_ops(lines)
        return 0
        
    lucas(n)

if __name__=='__main__':
	main()
