import socket
import random
import math

def main():

    print('Starting Server Program')

    c_arr = [1,1,0]

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           
    port = 8181                                           
    serversocket.bind((host, port))                                  
    serversocket.listen(len(c_arr))                                           

    clientsocket, addr = serversocket.accept()      

    for i, c in enumerate(c_arr):

        print('Evaluating Round',i+1)

        x = float(clientsocket.recv(1024).decode('utf-8'))
        
        clientsocket.send(str(c).encode('utf-8'))

        y_n_v = clientsocket.recv(1024).decode('utf-8').split(',')
        y = float(y_n_v[0])
        n = float(y_n_v[1])
        v = float(y_n_v[2])

        y2 = (math.pow(y,2) % n)
        xvc = (x*math.pow(v,c) % n)

        verified = False
        if (y2==xvc):
            verified = True
        
        clientsocket.send(str(verified).encode('utf-8'))

        if verified == False:
            print('Identity not verified!')
            break

    clientsocket.close()

    print('Ending Server Program')

if __name__ == '__main__':
    main()
