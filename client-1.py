import socket
#Creates a new socket
my_socket = socket.socket()
#Gets the address of the server
address = input('Enter IPv4 address of server: ')
#Gets the port of the server
port = int(input('Enter port number of server: '))
#all the names of the host
host = socket.gethostname()
#Connects to the server
my_socket.connect((address,port))
#prints out the data recieved from server
print(my_socket.recv(1024))
my_socket.close()

