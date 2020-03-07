import socket
listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 6789))
listen_socket.listen()
chat_socket, addr = listen_socket.accept()
q = True
while q:
    
    data = input('INPUT SERVER: ').encode()
    #print(data)
    chat_socket.sendall(data + b'\n')
    if data == b'quit':
        chat_socket.close()
        print('QUITTING...')
        listen_socket.close()
        q = False
        break
    else:
        print('WAITING FOR CLIENT...')
        data = b''
        while b'\n' not in data:
            data += chat_socket.recv(1024)
            print('CLIENT WROTE: ' + data.decode())
            if data == b'quit\n':
                print('CLIENT QUITTED')
                listen_socket.close()
                q = False
