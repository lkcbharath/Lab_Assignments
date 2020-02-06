#!/usr/bin/python3
# This is server.py file
import socket
import random
import math

def main():

    print('Starting Server Program')

    c_arr = [1,1,0]

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           
    port = 9999                                           
    serversocket.bind((host, port))                                  
    serversocket.listen(len(c_arr))                                           

    clientsocket, addr = serversocket.accept()      

    for i, c in enumerate(c_arr):

        print('Evaluating Round',i+1)

        x = float(clientsocket.recv(1024).decode('utf-8'))
        
        clientsocket.send(str(c).encode('utf-8'))

        y = float(clientsocket.recv(1024).decode('utf-8'))
        v = float(clientsocket.recv(1024).decode('utf-8'))

        y2 = math.pow(y,2)
        xvc = x*math.pow(v,c)

        print(y2,xvc)

        verified = False
        if (y2==xvc):
            verified = True
        
        clientsocket.send(str(verified).encode('utf-8'))

    clientsocket.close()

    print('Ending Server Program')

if __name__ == '__main__':
    main()
