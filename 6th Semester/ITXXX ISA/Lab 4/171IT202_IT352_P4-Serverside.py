import socket
import random
import math

def printer(str_):
    filename = '171IT202_IT352_P4_Output_TC1-Serverside.txt'
    print(str_)
    print(str_, file=open(filename, "a+"))

def main():

    printer('Starting Server Program')

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8181
    serversocket.bind((host, port))                                  
    serversocket.listen(5)                                           

    clientsocket, addr = serversocket.accept()     

    printer('Recieved connection from ' + str(addr)) 

    for i in range(3):

        printer('Evaluating Round ' + str(i+1))

        x = int(clientsocket.recv(1024).decode('utf-8'))

        if x == -1:
            printer('Client Program was terminated due to failure of one or more conditions. Terminating Server Program.')
            break

        printer('Witness recieved, x: ' + str(x))

        c = int(input('Enter Challenge c: '))

        printer('Challenge generated, c: ' + str(c))
        
        clientsocket.send(str(c).encode('utf-8'))

        y_n_v = clientsocket.recv(1024).decode('utf-8').split(',')
        y = int(y_n_v[0])
        n = int(y_n_v[1])
        v = int(y_n_v[2])

        printer('Response recieved, y: ' + str(y))
        printer('Public key accessed, v: ' + str(v))
        printer('Public key accessed, n: ' + str(n))

        y2 = int(math.pow(y,2) % n)
        xvc = int(x*math.pow(v,c) % n)

        printer('Value of y^2: ' + str(y2))
        printer('Value of x*v^c ' + str(xvc))

        if (y2==xvc):
            verified = True
            printer('Verification y^2 = x*v^c succeeded, and identity verified!')
        else:
            verified = False
            printer('Verification y^2 = x*v^c failed, and identity is not verified. Closing connection.')

        
        clientsocket.send(str(verified).encode('utf-8'))

        printer('')

        if verified == False:
            break

    clientsocket.close()

    printer('Ending Server Program')

if __name__ == '__main__':
    main()
