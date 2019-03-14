import huffman_encode
import math 

def nextPowerOf2(n): 
    count = 0; 
    if (n and not(n & (n - 1))): 
        return n 
      
    while( n != 0): 
        n >>= 1
        count += 1
      
    return 1 << count; 

def main():

    lines = [line.rstrip('\n') for line in open('code.txt','r')]
    binary = input('Enter binary representation: ')
    
    codes = [(i[:-1:],i[-1]) for i in lines]

    code = ''
    n_b = len(binary)
    n_c = len(codes)
    n_chars = 0

    for j in range(n_b):
        if binary[j] not in ['0','1']:
            print("Error! Invalid binary code entered!")
            exit(0)

        code += binary[j]
        for i in range(n_c):
            if code == codes[i][0]:
                print(codes[i][1],end='')
                code = ''
                n_chars += 1
                break
    print()

    compr = n_chars*int(math.log(nextPowerOf2(n_chars)+1,2))
    compr = (n_b/compr)*100
    print('The percentage of compression is: ' + format(compr, '.3f') + '%')

if __name__ == '__main__':
    main()