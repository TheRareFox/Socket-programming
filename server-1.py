import socket
#Creates a new socket
my_socket = socket.socket()
#Creates a server at address local host and port number 12345
my_socket.bind(("127.0.0.1", 12345))
#listens for active connections from the client
my_socket.listen()
#accepts connections from the client and returns the socket to send data to client
new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))
#sends bytes over to the client
new_socket.sendall(b'Hello from server\n')
#closes the connection
new_socket.close()
my_socket.close()
