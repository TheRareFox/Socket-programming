import socket
chat_socket = socket.socket()
#address = input('Enter IPv4 address of server: ')
#port = int(input('Enter port number of server: '))
chat_socket.connect(('127.0.0.1', 6789))
q = True
while q:
    print('WAITING FOR SERVER...')
    data = b'';
    while b'\n' not in data:
        data += chat_socket.recv(1024)
        
    print('SERVER WROTE: ' + data.decode())
    #print(data)
    if data == b'quit\n':
        chat_socket.close()
        print('QUITTING...')
        q = False
    else:
        data = input('INPUT CLIENT: ').encode()            
        chat_socket.sendall(data + b'\n')
        #print(data)
        if data == b'quit':
            chat_socket.close()
            print('QUITTING...')
            q = False
                

