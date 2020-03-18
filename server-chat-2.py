import socket
#Creates a new socket
listen_socket = socket.socket()
#Creates a server at address local host and port number 6789
listen_socket.bind(('127.0.0.1', 6789))
while True:
    #listens for active connections from the client
    my_socket.listen()
    #accepts connections from the client and returns the socket to send data to client
    chat_socket,addr = my_socket.accept()
    quit = False
    #while the user does not want to quit
    while not quit:
        data = input("Input server: ").encode()
        chat_socket.sendall(data + b'\n')
        if data == b'quit':
            #if data typed is quit then stops running the socket with the client
            quit = True
        else:
            print("WAITING FOR CLIENT")
            data = ''
            while '\n' not in data:
                data += chat_socket.recv(1024).decode()
            print("CLIENT WROTE: {}".format(data))
            #if data recieved is quit then stops running the socket with the client
            if data == 'quit\n':
                quit = True
    chat_socket.close()
    #while the client quit but the server is still listening for other connections
    print("Quitted, waiting for new connections")
