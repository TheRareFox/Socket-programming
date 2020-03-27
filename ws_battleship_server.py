import random, socket

##FUNCTIONS
def initGrid(): 
    return [["O" for _ in range(3)] for _ in range(3)]
       
def display(grid):
    for row in grid:
        connected_socket.sendall(("\t".join(row)+"\n").encode())
    connected_socket.sendall("\n".encode())

def getUserInput():
    ##MISSING CODE 
    #Code to send instructions for user to input row
    #Code to receive userinput for row
    #Code to send instructions for user to input column
    #Code to receive userinput for column
    connected_socket.sendall(b'\n')
    return (row, column)

##MAIN
##Create a server side socket

##MISSING CODE
#Code to create a server(listening) socket
#Code to bind that socket to localhost IP address and a port number 
#Code to allow socket to listen for incoming request
#Code to accept incoming request (Hint: .accept() returns a socket and address tuple) 
connected_socket, addr = 
##BATTLESHIP GAME CODE

grid = initGrid()

shiprow = random.randint(0,2) #generates a random number from 0-2
shipcolumn = random.randint(0,2)

won = False
times_guessed = 0

display(grid)
while times_guessed < 3 and won is False:
    row, col = getUserInput()
    if shiprow == row and shipcolumn == col:
        won = True
        ##MISSING CODE
        #Code to send message to client that client won
        times_guessed += 1
        grid[row][col] = "S" 
        display(grid)
    else:
        times_guessed += 1
        grid[row][col] = "X"
        display(grid)

if won is False: #times_guessed > 3 & won is False
    ##MISSING CODE 
    #Code to send message to client that client lost
    grid[shiprow][shipcolumn] = "S"
    display(grid)



