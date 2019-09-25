import random, math

def euclidean_gcd(a,b):
    r1 = a 
    r2 = b 
    while r2 > 0:
        q = int(r1/r2)
        r = r1 - (q*r2)
        r1 = r2
        r2 = r
    
    return r1

def pollardRho(N, x, c):
        if N%2==0:
                return 2
        y = x
        g = 1
        while g==1:             
                x = ((x*x)%N+c)%N
                y = ((y*y)%N+c)%N
                y = ((y*y)%N+c)%N
                g = euclidean_gcd(abs(x-y),N)
        return g

def main():
    n = input("Enter n: ")
    x = input("Enter x: ")
    y = input("Enter y: ")
    while (int(n) < 0):
        print("N must be positive. Please retry")
        n = input("Enter n:\t")
    while (int(x) < 0):
        print("x must be positive. Please retry")
        n = input("Enter x:\t")
    while (int(y) < 0):
        print("y must be positive. Please retry")
        n = input("Enter y:\t")
    result = pollardRho(int(n), int(x), int(y))
    print("Running, Pollard-Rho algorithm with given parameters on (n = " + str(int(n)) + ")...\n...")
    print("Result => Prime Factors of " + str(n) + " are: " + str(result) + ", " + str(int(int(n)/result))  )

if __name__ == '__main__':
    main()