import socket
import random
import math

class TestCase:
    
    def __init__(self,p,q,r,s):
        self.n = p * q
        self.s = s
        self.v = int(math.pow(s,2) % self.n)
        self.r = r
        self.x = int(math.pow(r,2) % self.n)
    
    def prove_identity(self, c):
        y = int(self.r * math.pow(self.s, c))

        return [y, self.n, self.v]

def printer(str_):
    filename = '171IT202_IT352_P4_Output_TC5-Clientside.txt'
    print(str_)
    print(str_, file=open(filename, "a+"))


def main():

    printer('Starting Client Program')

    results = []

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8181
    sock.connect((host, port))

    for i in range(3):
        printer('Evaluating Round ' + str(i+1))
        
        p = int(input('Enter first prime number p: '))
        q = int(input('Enter second prime number q: '))
        r = int(input('Enter commitment/random number r: '))
        s = int(input('Enter private key s: '))

        tc = TestCase(p, q, r, s)

        printer('Witness generated and sent, x: ' + str(tc.x))
        printer('Commitment/Random number generated, r: ' + str(tc.r))
        printer('Private key generated, s: ' + str(tc.s))
        printer('Public key generated and made public, v: ' + str(tc.v))
        printer('Public value generated and made public, n: ' + str(tc.n))

        if tc.r not in range(0,tc.n):
            printer('The value of r is not in between 0 and n-1. Terminating execution of Client Program.')
            sock.send('-1'.encode('utf-8'))
            break
        
        if tc.s not in range(1,tc.n-1):
            printer('The value of s is not in between 1 and n-1 (exclusive). Terminating execution of Client Program.')
            sock.send('-1'.encode('utf-8'))
            break
        
        sock.send(str(tc.x).encode('utf-8'))

        c = int(sock.recv(1024).decode('utf-8'))

        printer('Challenge received, c: ' + str(c))

        y, n, v = tc.prove_identity(c)

        printer('Response generated and sent, y: ' + str(y))
        
        sock.send(','.join([str(y), str(n), str(v)]).encode('utf-8'))

        verified = sock.recv(1024).decode('utf-8')
        verified = (verified == 'True')

        if verified == True:
            printer('For Round ' + str(i+1) + ' Identity verified!')
        else:
            printer('For Round ' + str(i+1) + ' Identity not verified, and connection was closed.')

        printer('')
        
        if verified == False:
            break

    sock.close()

    printer('Ending Client Program')       

if __name__ == '__main__':
    main()
