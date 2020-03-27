import socket
##MISSING CODE
#Code to create client socket
#Code to connected client socket to server socket

print("Welcome to Battleship! Try to guess where the ship is!\n")

while True:
    ##MISSING CODE
    #Code to store data received into a variable named 'datareceived' 
    datareceived = 
    print(datareceived, end='')
    if "Enter" in datareceived:
        userinput = input()
        client_socket.sendall(userinput.encode()) #Code to send encoded userinput
    if "YOU WON" in datareceived or "YOU LOST" in datareceived:
        break

client_socket.close() 

####BATTLESHIP
