import math

def file_ops(lines):
    f = open("output.txt", "a")
    for line in lines:
        print(line)
        f.write(line + '\n')
    f.write('\n')
    f.close()
    return

def euclidean_gcd(a,b):
    if (b == 0):
         return a
    return euclidean_gcd(b, a % b)

def is_quadratic_residue(N,prime):
    x = N**((prime-1)//2)%prime
    if (x==1):
        return True
    return False

def sieve_eras(n):
    prime = [True for i in range(n+1)]
    factors = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            factors.append(p)
    
    return factors

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

    return factors

def check_if_square(n):
    n_root = int(math.sqrt(n))
    return n_root*n_root == n

def quadratic_sieve(N,B):
    prime_factors = sieve_eras(B+1)
    lines = []
    factor_base = []
    for x in prime_factors:
        if is_quadratic_residue(N,x):
            factor_base.append(x)
    factor_base.insert(0,-1)
    f_b_n = len(factor_base)


    lines.append("\nB-smooth factor base: " + ','.join([str(f) for f in factor_base]))

    lines.append("Q(x) is defined as (a*a - N)\n")

    all_bits = []
    
    power_of_each = []
            
    a = int(math.sqrt(N)) + 1

    for iterations in range(40):
        bits = [0 for i in range(f_b_n)]
        power_of_each_bit = [0 for i in range(f_b_n)]
        flag = 0
        q = int(a*a) - N

        if(q<0):
            q = abs(q)
            bits[0] = 1
            power_of_each_bit[0] = 1
            flag = 1

        q_factors = prime_factorize(q)

        if (((set(q_factors) & set(factor_base)) == set(q_factors)) == False):
            a += 1
            continue
        
        for i in range(1,f_b_n):
            q_temp = q

            if(q_temp%factor_base[i]==0):
                flag = 1

            while(q_temp%factor_base[i]==0) and (q_temp>1):
                bits[i] += 1
                q_temp = int(q_temp/factor_base[i])
            
            power_of_each_bit[i] = bits[::][i]

            bits[i] = bits[i]%2
        if(flag==1):
            all_bits.append([a,bits])
            power_of_each.append([a,power_of_each_bit])
            lines.append("a such that Q(a) is B-smooth: " + str(a))
            lines.append("Exponent vectors of Q(a) modulo 2: " + ','.join([str(f) for f in bits]) + "\n")

        a += 1
    
    a_b_n = len(all_bits)

    for i in range(a_b_n):
        for j in range(i+1,a_b_n):
            for k in range(j+1,a_b_n):
                flag = 0
                for l in range(f_b_n):
                    if (all_bits[i][1][l] + all_bits[j][1][l] + all_bits[k][1][l]) % 2 == 1:
                        flag = 1
                        break
                if(flag==0):
                    # calculate x
                    X = (all_bits[i][0]*all_bits[j][0]*all_bits[k][0])%N
                    # calculate y
                    Y = 1
                    for l in range(1,f_b_n):
                        power = (power_of_each[i][1][l] + power_of_each[j][1][l] + power_of_each[k][1][l])/2
                        Y *= factor_base[l]**power
                    Y = int(Y%N)
                    
                    f = euclidean_gcd(X+Y,N)
                    g = euclidean_gcd(X-Y,N)

                    if(f not in range(2,N) or g not in range(2,N)):
                        lines.append(
                            "x and y such that x^2 is congruent to y^2(mod N): " + str(X) + " " + str(Y))
                        lines.append(
                            "Either of f and g such that f = gcd(x+y,N) and g = gcd(x-y,N) is 1.\n")
                        continue

                    lines.append(
                        "x and y such that x^2 is congruent to y^2(mod N): " + str(X) + " " + str(Y))
                    lines.append(
                        "f and g such that f = gcd(x+y,N), g = gcd(x-y,N), N = f*g and 1 < (f,g) < N: " + str(f) + " " + str(g) + "\n")

    file_ops(lines)


def main():
    N = int(input("Enter the positive integer N: "))
    B = int(input("Enter the positive integer B: "))
    lines = []
    
    if (N < 1):
        lines.append((str(N) + " is not positive! Terminating"))
        file_ops(lines)
        return 0
    if (B < 1):
        lines.append((str(B) + " is not positive! Terminating"))
        file_ops(lines)
        return 0
    if (N == 1):
        lines.append((str(N) + " does not have any prime factors."))
        file_ops(lines)
        return 0
    if (N == 2):
        lines.append((str(N) + " is the only prime factor of itself."))
        file_ops(lines)
        return 0
    
    
    quadratic_sieve(N,B)

if __name__ == '__main__':
    main()
