#!/usr/bin/python3
# This is client.py file

import socket

class TestCase:

    def __init__(self,p,q,r,s,c):
        self.n = (p * q)
        self.r = r
        self.s = s
        self.c = c

def main():

    

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))      

    msg1 = 'I am a menace'
    s.send(msg1.encode('utf-8'))


    # Receive no more than 1024 bytes
    msg = s.recv(1024)                                     

    s.close()
    print (msg.decode('utf-8'))

if __name__ == '__main__':
    main()
