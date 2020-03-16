import socket
chat_socket = socket.socket()
chat_socket.connect(('127.0.0.1',6789))

quit = False
while not quit:
    print("WAITING FROM SERVER")
    data = ''
    while '\n' not in data:
        data += chat_socket.recv(1024).decode()
    print("SERVER WROTE: {}".format(data))
    if data == 'quit\n':
        quit = True
    else:
        data = input("INPUT CLIENT: ")
        if data == 'quit':
            quit = True
        chat_socket.sendall(data.encode() + b'\n')
chat_socket.close()
