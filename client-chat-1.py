import socket
#Creates a new socket
my_socket = socket.socket()
#Gets the address of the server
address = input('Enter IPv4 address of server: ')
#Gets the port of the server
port = int(input('Enter port number of server: '))
#Connects to the server
my_socket.connect((address, port))
#continuously run the code
while True:
    print('WAITING FOR SERVER...')
    #collects data from server until server ends the line
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    print('SERVER WROTE: ' + data.decode()
    data = input('INPUT CLIENT: ').encode()
    #sends data to the server
    chat_socket.sendall(data + b'\n')
