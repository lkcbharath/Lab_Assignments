import socket
import random
import math

class TestCase:
    
    def __init__(self,p,q,s,r):
        self.n = p * q
        self.s = s
        self.v = math.pow(s,2) % self.n
        self.r = r
        self.x = math.pow(r,2) % self.n
    
    def prove_identity(self, c):
        y = self.r * math.pow(self.s, c)

        return [y, self.n, self.v]

def main():

    print('Starting Client Program')

    t1 = TestCase(467,479,111,1111)
    t2 = TestCase(929,937,200,760)
    t3 = TestCase(727,733,1000,540)

    test_cases = [t1,t2,t3]
    results = []

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8181
    sock.connect((host, port))

    for i, tc in enumerate(test_cases):

        print('Evaluating Round', i+1)

        sock.send(str(tc.x).encode('utf-8'))

        c = int(sock.recv(1024).decode('utf-8'))

        y, n, v = tc.prove_identity(c)
        
        sock.send(','.join([str(y), str(n), str(v)]).encode('utf-8'))

        # Verify whether user is really Alice
        verified = sock.recv(1024).decode('utf-8')
        verified = (verified == 'True')

        results.append([verified,i+1])
        
        if verified == False:
            break

    sock.close()

    for result, round_ in results:
        if result == True:
            print('For Round',round_,'Identity verified')
        else:
            print('For Round',round_,'Identity not verified')

    print('Ending Client Program')

if __name__ == '__main__':
    main()
