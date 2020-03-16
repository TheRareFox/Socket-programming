import socket
#Creates a new socket
my_socket = socket.socket()
#Gets the address of the server
address = input('Enter IPv4 address of server: ')
#Gets the port of the server
port = int(input('Enter port number of server: '))
#Connects to the server
my_socket.connect((address, port))
data = b''
#collects data from server until server ends the line
while b'\n' not in data:
    data += my_socket.recv(1024)
print(data)
my_socket.close()
