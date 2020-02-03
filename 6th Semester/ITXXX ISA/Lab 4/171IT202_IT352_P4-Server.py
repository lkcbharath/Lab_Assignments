#!/usr/bin/python3
# This is server.py file
import socket     
                                    
def main():

    # create a socket object
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           

    port = 9999                                           

    # bind to the port
    serversocket.bind((host, port))                                  

    # queue up to 5 requests
    serversocket.listen(5)                                           

    while True:
        # establish a connection
        clientsocket,addr = serversocket.accept()      

        print("Got a connection from %s" % str(addr))

        msg1 = clientsocket.recv(1024).decode('utf-8')
        print(msg1)

        msg = 'Thank you for connecting'+ "\r\n"
        clientsocket.send(msg.encode('utf-8'))
        clientsocket.close()


if __name__ == '__main__':
    main()
