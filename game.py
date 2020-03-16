import random
import time
class Map:
    def __init__(self):
        self.map = []
        ran = random.randint(1,19)
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

        
        for x in range(lower_x,upper_x):
            for y in range(lower_y,upper_y):
                if y == char_y and x == char_x:
                    print('C',end = "")
                else:
                    print(self.map[x][y],end = "")
            print()

    def show_map(self,char_pos):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if x == char_pos[0] and y == char_pos[1]:
                    print('C',end = "")
                else:
                    print(self.map[x][y],end = "")
            print()

    def enemy_encounter(self,char_pos):
        if self.map[char_pos[0]][char_pos[1]] == "E":
            print("Enemy encountered!")
            return True
        else:
            return False
    def treasure_encounter(self,char_pos):
        if self.map[char_pos[0]][char_pos[1]] == "T":
            print("Treasure picked up!")
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

    def move(self,direction,mp):
        if direction.lower() == "up":
            if self.pos[0] - 1 >= 0:
                self.pos[0] -= 1
            else:
                print("False move, try again")
                
        elif direction.lower() == "down":
            if self.pos[0] + 1 <= 20:
                self.pos[0] += 1
            else:
                print("False move, try again")
                
        elif direction.lower() == "left":
            if self.pos[1] - 1 > 1:
                self.pos[1] -= 1
            else:
                print("False move, try again")
                
        elif direction.lower() == "right":
            if self.pos[1] + 1 < 19:
                self.pos[1] += 1
            else:
                print("False move, try again")
        if mp.treasure_encounter(self.pos):
            print("YOU FOUND THE TREASURE! YOU WIN!")
            return False
        elif mp.enemy_encounter(self.pos):
            print("Fighting enemy...")
            enemy = Enemy(random.randint(1,4))
            while True:
                print(enemy.get_sprite())
                print("1. Attack 2. Run(50% chance)")
                a = input("Enter action(1,2): ")
                while a != '1' and a != '2':
                    print("Invalid input")
                    a = input("Enter action(1,2): ")
                print(enemy.status())
                print("Your health: {}".format(self.health))
                if a == '1':
                    dmg = self.attack + random.randint(-3,3)
                    enemy.hit(dmg)
                    print("Attacked enemy for {} damage!".format(dmg))
                    print(enemy.status())
                    if enemy.get_health()< 0:
                        print("Enemy defeated!")
                        break
                elif a == '2':
                    if 1 == random.randint(1,2):
                        print("Ran away successfully!")
                        break
                    else:
                        print("Failed to run away!")
                dmg = enemy.damage()
                print("Enemy hit you for {} damage! {} health remaining".format(dmg,self.health - dmg))
                self.health -= dmg
                if self.health <0:
                    print("You have been killed!")
                    return False
                time.sleep(2)
            
            mp.change_map(self.pos[0],self.pos[1])
            mp.show(self.pos)
                                            
                    
        else:
            mp.show(self.pos)
        return True

    def get_pos(self):
        return self.pos

    
mp = Map()
char = Character()
mp.show_map(char.get_pos())
print("Legend: C - character position E- enemy position T - Treasure position")
print("WELCOME TO NET, WHERE YOUR GOAL IS TO OBTAIN ALL THE TREASURES WHILE FIGHTING ENEMIES! GOOD LUCK!")
index = 0
while True:
    if index >7:
        index = 0
        print("ENEMIES ADDED!")
        mp.add_enemy()
        mp.show_map(char.get_pos())
        
    movement = input("WHERE DO YOU WANT TO GO?(up,down,left,right): ").lower()
    while movement != 'up' and movement != 'down' and movement != 'left' and movement != 'right':
        print("Please only input up,down,left or right")
        movement = input("WHERE DO YOU WANT TO GO?(up,down,left,right): ").lower()
    bo = char.move(movement,mp)
    if not bo:
        print("Game over!")
        break
    index += 1
    
