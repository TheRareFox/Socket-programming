import socket
my_socket = socket.socket()
my_socket.bind(('127.0.0.1',6789))
while True:
    my_socket.listen()

    chat_socket,addr = my_socket.accept()

    quit = False
    while not quit:
        data = input("Input server: ").encode()
        chat_socket.sendall(data + b'\n')
        if data == b'quit':
            quit = True
        else:
            print("WAITING FOR CLIENT")
            data = ''
            while '\n' not in data:
                data += chat_socket.recv(1024).decode()
            print("CLIENT WROTE: {}".format(data))
            if data == 'quit\n':
                quit = True
    chat_socket.close()
    print("Quitted, waiting for new connections")
