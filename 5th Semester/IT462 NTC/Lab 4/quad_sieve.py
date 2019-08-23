import math

def euclidean_gcd(a,b):
    r1 = a 
    r2 = b 
    while r2 > 0:
        q = int(r1/r2)
        r = r1 - (q*r2)
        r1 = r2
        r2 = r
    
    return r1

def is_quadratic_residue(a,p):
    x = int(math.pow(a,(p-1)/2))
    if (x==1):
        return True
    return False

def prime_factorize(n):
    factors = []
    if (n % 2 == 0):
        factors.append(2)
    while (n % 2 == 0):
        n = n / 2

    for i in range(3, int(math.sqrt(n)+1), 2):
        if (n % i == 0):
            factors.append(int(i))
        while (n % i == 0):
            n = n / i
    if (n > 2):
      factors.append(int(n))

def check_if_square(n):
    n_root = int(math.sqrt(n))
    return n_root*n_root == n

def quadratic_sieve(N,B):
    prime_factors = prime_factorize(B)
    factor_base = []
    for x in prime_factors:
        if is_quadratic_residue(x,p):
            factor_base.append(x)
    factor_base.insert(-1,0)
    f_b_n = len(factor_base)
    possibilities = []

    all_bits = []
            
    a = int(math.sqrt(N)) + 1
    for iterations in range(100):
        bits = [0 for i in range(f_b_n)]
        q = int((a*a)%N)
        for i in range(f_b_n):
            q_temp = q
            while(q_temp%factor_base[i]==0):
                bits[i] += 1
                q_temp = q_temp/factor_base[i]
            
            bits[i] = bits[i]%2

        all_bits.append(bits)
        a += 1

    

def main():
    N = int(input("Enter the positive integer N: "))
    B = int(input("Enter the positive integer B: "))
    lines = []
    
    if (N < 1):
        lines.append((str(n) + " is not positive! Terminating"))
        file_ops(lines)
        return 0
    if (B < 1):
        lines.append((str(k) + " is not positive! Terminating"))
        file_ops(lines)
        return 0
    if (N == 1):
        lines.append((str(n) + " does not have any prime factors."))
        file_ops(lines)
        return 0
    if (B == 2):
        lines.append((str(n) + " is the only prime factor of itself."))
        file_ops(lines)
        return 0
    
    
    quadratic_sieve(N,B)

if __name__ == '__main__':
    main()