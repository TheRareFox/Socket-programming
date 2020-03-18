import socket
#Creates a new socket
listen_socket = socket.socket()
#Creates a server at address local host and port number 6789
listen_socket.bind(('127.0.0.1', 6789))
#listens for active connections from the client
listen_socket.listen()
#accepts connections from the client and returns the socket to send data to client
chat_socket, addr = listen_socket.accept()
while True:
    #Asks users to input what they want to send over to the client
    data = input('INPUT SERVER: ').encode()
    #Sends data over to client in form of bytes
    chat_socket.sendall(data + b'\n')
    print('WAITING FOR CLIENT...')
    #recieves the client's data and prints it
    data = b''
    while b&'\n' not in data:
        data += chat_socket.recv(1024)
    print('CLIENT WROTE: ' + data.decode())
