import socket
#Creates a new socket
my_socket = socket.socket()
#Gets the address of the server
address = input('Enter IPv4 address of server: ')
#Gets the port of the server
port = int(input('Enter port number of server: '))
#Connects to the server
my_socket.connect((address, port))
quit = False
#when users havent quitted yet
while not quit:
    print("WAITING FROM SERVER")
    data = ''
    while '\n' not in data:
        data += chat_socket.recv(1024).decode()
    #collects data from server until server ends the line
    print("SERVER WROTE: {}".format(data))
    #if server entered quit then stop running the code
    if data == 'quit\n':
        quit = True
    else:
        data = input("INPUT CLIENT: ")
        #if user entered data stop running the code
        if data == 'quit':
            quit = True
        #sends data over to the server
        chat_socket.sendall(data.encode() + b'\n')
chat_socket.close()
