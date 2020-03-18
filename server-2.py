import socket
import time
#Creates a new socket
my_socket = socket.socket()
#Creates a server at address local host and port number 12345
my_socket.bind(("127.0.0.1", 12345))
#listens for active connections from the client
my_socket.listen()
while True:
    #accepts connections from the client and returns the socket to send data to client
    new_socket, addr = my_socket.accept()
    #sending bytes to the client
    new_socket.sendall(b'Hello fr')
    time.sleep(0.1)
    new_socket.sendall(b'om server\n')
    new_socket.close()
    #my_socket.close()
