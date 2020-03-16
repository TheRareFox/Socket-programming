import random
import time
import socket
class Map:
    def __init__(self):
        self.map = []
        ran = random.randint(1,18)
        for i in range(20):
            a = ['|']
            recent = True
            treasure = True
            for j in range(18):
                if j == ran and i == 13:
                    a.append('T')
                elif random.randint(0,10) == 10 and recent:
                    a.append('E')
                    recent = False
                else:
                    a.append('.')

            a.append('|')
            self.map.append(a)

    def get_map(self):
        return self.map

    def change_map(self,x,y):
        self.map[x][y] = "."
        
    def show(self,char_pos):
        #print(self.map)
        
        char_x = char_pos[0]
        lower_x = char_x - 3 if char_x - 4 > 0 else 0
        upper_x = char_x + 5 if char_x +4 < len(self.map)-1 else len(self.map)-1

        char_y = char_pos[1]
        lower_y = char_y - 3 if char_y - 4 > 0 else 0
        upper_y = char_y + 5 if char_y +4 < len(self.map[1])-1 else len(self.map[1])

        mp = ''
        for x in range(lower_x,upper_x):
            for y in range(lower_y,upper_y):
                if y == char_y and x == char_x:
                    print('C',end = "")
                    mp += 'C'
                else:
                    print(self.map[x][y],end = "")
                    mp += self.map[x][y]
            print()
            mp += '\n'
        client_socket.sendall(mp.encode())

    def show_map(self,char_pos,client_socket):
        mp = ''
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if x == char_pos[0] and y == char_pos[1]:
                    print('C',end = "")
                    mp += 'C'
                else:
                    print(self.map[x][y],end = "")
                    mp += self.map[x][y]                    
            print()
            mp += '\n'
        client_socket.sendall(mp.encode())

    def enemy_encounter(self,char_pos):
        if self.map[char_pos[0]][char_pos[1]] == "E":
            client_socket.sendall(b"Enemy encountered!")
            print("Enemy encountered!")
            return True
        else:
            return False
    def treasure_encounter(self,char_pos):
        if self.map[char_pos[0]][char_pos[1]] == "T":
            print("Treasure picked up!")
            client_socket.sendall(b"Treasure picked up!")
            return True
        else:
            return False

    def add_enemy(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                a = random.randint(1,10)
                if a == 1 and self.map[i][j] == ".":
                    self.map[i][j] = "E"
                
class Enemy:
    def __init__(self,difficulty):
        self.health = difficulty*5
        self.attack = difficulty/2*3

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def hit(self,dmg):
        self.health -= dmg
        
    def damage(self):
        return self.attack + random.randint(-3,3)

    def status(self):
        return "Enemy health left: {}".format(self.health)
        
    def get_sprite(self):
        return """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██  ▓▓░░░░░░░░▓▓  ▓▓░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██    ▓▓░░░░░░▓▓    ▓▓░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░██      ▓▓░░░░░░▓▓░░  ▓▓░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░██  ░░  ▓▓░░░░▓▓  ░░    ▓▓░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░██  ░░  ▓▓░░░░▓▓  ░░░░  ▓▓░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▓▓    ▓▓░░  ▓▓▓▓  ░░▓▓░░  ▓▓░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▓▓  ░░▓▓▒▒  ▓▓▓▓  ▓▓▓▓▒▒    ▒▒░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▓▓  ░░▓▓▓▓░░░░░░░░░░▓▓▓▓░░  ▓▓░░░░░░░░░░░░
░░░░░░░░░░░░░░▒▒░░    ░░▓▓▒▒      ░░░░▒▒▒▒  ▓▓░░░░░░░░░░░░
░░░░░░░░░░░░░░▓▓░░░░    ▓▓              ░░  ▓▓░░░░░░░░░░░░
░░░░░░░░░░░░░░▓▓░░░░  ░░    ████░░      ▒▒██░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▓▓░░░░░░    ██▓▓▓▓▓▓      ▓▓▓▓░░░░░░░░░░░░░░
░░░░░░░░██▓▓▓▓▒▒▒▒░░░░    ▓▓▓▓▓▓▓▓      ▓▓▓▓░░░░░░░░░░░░░░
░░░░░░██░░  ▓▓▒▒▒▒░░      ▓▓▓▓▓▓▓▓░░  ░░▓▓▓▓░░░░░░░░░░░░░░
░░░░░░▓▓░░░░  ▒▒▒▒░░      ░░▓▓▓▓▓▓▒▒░░  ▓▓  ▓▓░░░░░░░░░░░░
░░░░░░▓▓▓▓░░░░  ░░░░░░        ▓▓▓▓░░░░  ░░  ▓▓░░░░░░░░░░░░
░░░░░░░░▓▓▒▒░░░░  ░░        ░░▓▓░░░░░░░░  ░░▓▓░░░░░░░░░░░░
░░░░░░░░▓▓▓▓▓▓░░░░  ░░    ░░░░▓▓░░░░▓▓▓▓░░░░▓▓░░░░░░░░░░░░
░░░░░░░░▓▓▓▓▓▓▒▒░░  ░░░░  ░░░░░░▒▒░░░░░░▒▒▒▒░░░░░░░░░░░░░░
░░░░░░██▓▓▒▒▓▓▓▓▓▓░░  ░░░░  ░░░░░░░░░░▓▓██░░░░░░░░░░░░░░░░
░░░░██▓▓▒▒▒▒▒▒▓▓▓▓▓▓░░  ░░░░░░░░░░▒▒██░░░░░░░░░░░░░░░░░░░░
░░██▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░  ████▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░
░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░▓▓▓▓▓▓░░  ▓▓░░░░░░░░░░░░░░░░░░░░
░░▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▓░░  ▓▓▓▓▒▒░░▓▓░░░░░░░░░░░░░░░░░░░░
░░▓▓▓▓░░░░▒▒▒▒▓▓▓▓▓▓▒▒▓▓░░  ▓▓▓▓▓▓░░░░▒▒░░░░░░░░░░░░░░░░░░
░░▓▓░░░░  ▓▓▓▓▓▓░░▓▓▓▓▒▒░░▒▒▓▓▓▓▓▓░░  ▓▓░░░░░░░░░░░░░░░░░░
░░▓▓░░░░▒▒▓▓▓▓░░░░▒▒▓▓▒▒  ▓▓▓▓▓▓▓▓░░▒▒░░░░░░░░░░░░░░░░░░░░
░░░░██  ▓▓  ▓▓░░░░░░░░▓▓██░░░░▓▓░░  ██░░░░░░░░░░░░░░░░░░░░
░░░░██    ░░░░▓▓░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░
░░░░░░██  ██░░▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
    
class Character:
    def __init__(self):
        self.pos = [0,1]
        self.health = 20
        self.attack = 5

    def move(self,direction,mp,client_socket):
        if direction.lower() == "up":
            if self.pos[0] - 1 >= 0:
                self.pos[0] -= 1
            else:
                print("False move, try again")
                client_socket.sendall(b"False move, try again")
                
        elif direction.lower() == "down":
            if self.pos[0] + 1 <= 20:
                self.pos[0] += 1
            else:
                print("False move, try again")
                client_socket.sendall(b"False move, try again")

                
        elif direction.lower() == "left":
            if self.pos[1] - 1 > 1:
                self.pos[1] -= 1
            else:
                print("False move, try again")
                client_socket.sendall(b"False move, try again")
                
        elif direction.lower() == "right":
            if self.pos[1] + 1 < 19:
                self.pos[1] += 1
            else:
                print("False move, try again")
                client_socket.sendall(b"False move, try again")
                
        if mp.treasure_encounter(self.pos):
            print("YOU FOUND THE TREASURE! YOU WIN!")
            client_socket.sendall(b"YOU FOUND THE TREASURE! YOU WIN!")
            return False
        elif mp.enemy_encounter(self.pos):
            print("Fighting enemy...")
            client_socket.sendall(b"Fighting enemy...")
            enemy = Enemy(random.randint(1,4))
            while True:
                print(enemy.get_sprite())
                client_socket.sendall(b"sprite")
                print("1. Attack 2. Run(50% chance)")
                client_socket.sendall(b"1. Attack 2. Run(50% chance)")
                client_socket.sendall(b"INPUT: Enter action(1,2): ")
                a = client_socket.recv(1024).decode()
                while a != '1' and a != '2':
                    print("Invalid input")
                    client_socket.sendall(b"Invalid input")
                    client_socket.sendall(b"INPUT: Enter action(1,2): ")
                    a = client_socket.recv(1024).decode()
                    
                print(enemy.status())
                client_socket.sendall(enemy.status().encode())
                print("Your health: {}".format(self.health))
                client_socket.sendall(b"Your health: " + str(self.health).encode())
                if a == '1':
                    dmg = self.attack + random.randint(-3,3)
                    enemy.hit(dmg)
                    print("Attacked enemy for {} damage!".format(dmg))
                    client_socket.sendall(b"Attacked enemy for "+str(dmg).encode()+b" damage!")
                    print(enemy.status())
                    client_socket.sendall(enemy.status().encode())
                    if enemy.get_health()< 0:
                        print("Enemy defeated!")
                        client_socket.sendall(b"Enemy defeated!")
                        break
                elif a == '2':
                    if 1 == random.randint(1,2):
                        print("Ran away successfully!")
                        client_socket.sendall(b"Ran away successfully!")
                        break
                    else:
                        print("Failed to run away!")
                        client_socket.sendall(b"Failed to run away!")
                dmg = enemy.damage()
                print("Enemy hit you for {} damage! {} health remaining".format(dmg,self.health - dmg))
                client_socket.sendall(b"Enemy hit you for "+str(dmg).encode()+b" damage! "+str(self.health - dmg).encode() + b" health remaining")
                self.health -= dmg
                if self.health <0:
                    print("You have been killed!")
                    client_socket.sendall(b"You have been killed!")
                                      
                    return False
                time.sleep(2)
            
            mp.change_map(self.pos[0],self.pos[1])
            mp.show(self.pos)
                                            
                    
        else:
            mp.show(self.pos)
        return True

    def get_pos(self):
        return self.pos

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 6789))
listen_socket.listen()
client_socket, addr = listen_socket.accept()

mp = Map()
char = Character()
mp.show_map(char.get_pos(),client_socket)
print("Legend: C - character position E- enemy position T - Treasure position")
client_socket.sendall(b"Legend: C - character position E- enemy position T - Treasure position")
print("WELCOME TO NET, WHERE YOUR GOAL IS TO OBTAIN ALL THE TREASURES WHILE FIGHTING ENEMIES! GOOD LUCK!")
client_socket.sendall(b"WELCOME TO NET, WHERE YOUR GOAL IS TO OBTAIN ALL THE TREASURES WHILE FIGHTING ENEMIES! GOOD LUCK!")
charge = 0
index = 0
while True:
    print("Turns until you get to send reinforcements!: {}".format(7-index))
    if index >7:
        charge += 1
        index = 0
    if charge >0:
        print("You have {} reinforcements".format(charge))
        a = ''
        while a!= 'n' and charge >0:    
            if a == 'y':
                print("ENEMIES ADDED!")
                client_socket.sendall(b"ENEMIES ADDED!")
                mp.add_enemy()
                mp.show_map(char.get_pos(),client_socket)
                charge -= 1
                break
            a = input("Do you wish to send reinforcements(y/n)(you can send more than one at a time): ")
            
    client_socket.sendall(b"INPUT: WHERE DO YOU WANT TO GO?(up,down,left,right): ")
    movement = client_socket.recv(1024).decode()
    while movement != 'up' and movement != 'down' and movement != 'left' and movement != 'right':
        print("Please only input up,down,left or right")
        client_socket.sendall(b"Please only input up,down,left or right")
        client_socket.sendall(b"INPUT: WHERE DO YOU WANT TO GO?(up,down,left,right): ")
        movement = client_socket.recv(1024).decode()
    bo = char.move(movement,mp,client_socket)
    if not bo:
        print("Game over!")
        client_socket.sendall(b"Game over!")
        break
    index += 1
client_socket.close()
listen_socket.close()
