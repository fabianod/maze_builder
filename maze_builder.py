#320 seconds for 80000 squares

import pygame
import math
import random
import time

width = 1600
height = 800
scale = 20

displayMoves = False

start = time.time()
startPoint = [random.randint(3,(width/scale)-3),random.randint(3,(height/scale)-3)]
print(startPoint)
endPoint = [random.randint(3,(width/scale)-3),random.randint(3,(height/scale)-3)]

print(endPoint)

squares = ((width / scale) * (height / scale))
print(squares)

WHITE = (255,255,255)
PURPLE = (150,0,150)
RED = (255,0,0)
DARK_RED= (155,0,0)
BLACK = (0,0,0)
GREY = (50,50,50)
GREEN = (0,255,0)

class Builder:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.LastList = []

    def Show(self, window, scale, colour):

        pygame.draw.rect(window, colour, (self.x * scale, self.y * scale, scale, scale), 0) 

    def Move(self):

        direction = random.randint(0,3)

        tiles[self.y][self.x].visited = True

        #print(self.x, self.y)
        
        if direction == 0 and self.y != 0 and not tiles[self.y - 1][self.x].visited:

            #print(direction)

            self.LastList.append([self.y,self.x])
            tiles[self.y][self.x].N = False

            self.y -= 1
            tiles[self.y][self.x].S = False

        elif direction == 1 and self.x != math.floor(width / scale) - 1 and not tiles[self.y][self.x + 1].visited:

            #print(direction)

            self.LastList.append([self.y,self.x])
            tiles[self.y][self.x].E = False

            self.x += 1
            tiles[self.y][self.x].W = False

        elif direction == 2 and self.y != math.floor(height / scale) - 1 and not tiles[self.y + 1][self.x].visited:

            #print(direction)

            self.LastList.append([self.y,self.x])
            tiles[self.y][self.x].S = False

            self.y += 1
            tiles[self.y][self.x].N = False

        elif direction == 3 and self.x != 0 and not tiles[self.y][self.x - 1].visited:

            #print(direction)

            self.LastList.append([self.y,self.x])
            tiles[self.y][self.x].W = False

            self.x -= 1
            tiles[self.y][self.x].E = False
            
        elif self.isStuck():

            self.StepBack()

        else:

            pass

       

    def StepBack (self):

        listPos = len(self.LastList) - 1

        while self.isStuck():

            try:

                self.y = self.LastList[listPos][0]
                self.x = self.LastList[listPos][1]

            except:

                running = False
                break

            listPos -= 1

            if listPos <= 1 and cycles >= squares / 2:

                running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        #print("Unstuck")
            

    def isStuck(self):

        stuck = True

        for direction in range(4):

            if direction == 0 and self.y != 0 and not tiles[self.y - 1][self.x].visited:

                stuck = False

            elif direction == 1 and self.x != math.floor(width / scale) and not tiles[self.y][self.x + 1].visited:

                stuck = False

            elif direction == 2 and self.y != math.floor(height / scale) and not tiles[self.y + 1][self.x].visited:

                stuck = False

            elif direction == 3 and self.x != 0 and not tiles[self.y][self.x - 1].visited:

                stuck = False

        return stuck
        

class Tile:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.N = True
        self.E = True
        self.S = True
        self.W = True

        self.visited = False
        if [self.x, self.y] != endPoint:
            self.endPoint = False
        else:
            self.endPoint = True

        self.path = False

    def Show(self, window, scale, colour):

        x = self.x
        y = self.y

        colour = GREY if self.visited else colour
        colour = DARK_RED if self.path else colour
        colour = RED if self.endPoint else colour

        pygame.draw.rect(window, colour, (self.x * scale, self.y * scale, scale, scale), 0) 

        if self.N == True and self.visited:
            #print(1)
            pygame.draw.line(window, WHITE, (x * scale, y * scale), ((x + 1) * scale, y * scale), 1)
        if self.E == True and self.visited:
            #print(1)
            pygame.draw.line(window, WHITE, ((x + 1) * scale, y * scale), ((x + 1) * scale, (y + 1) * scale), 1)
        if self.S == True and self.visited:
            #print(1)
            pygame.draw.line(window, WHITE, ((x + 1) * scale, (y + 1) * scale), (x * scale, (y + 1) * scale), 1)
        if self.W == True and self.visited:
            #print(1)
            pygame.draw.line(window, WHITE, (x * scale, (y + 1) * scale), (x * scale, y * scale))

def display(tiles, surface, colour):

    for y in range(len(tiles) - 1):

        for x in range(len(tiles[y]) - 1):

            tiles[y][x].Show(surface, scale, colour) 

tiles = []

for y in range(math.floor(height / scale) + 1):

    tiles.append([])
    
    for x in range(math.floor(width / scale) + 1):

        tiles[y].append(Tile(x,y))

        if x == math.floor(width / scale) or y == math.floor(height / scale):

            tiles[y][x].visited = True
        

screen = pygame.display.set_mode((width,height))

billy = Builder(startPoint[0],startPoint[1])
pygame.display.update()

cycles = 0

running = True
while running:

    if displayMoves:

        display(tiles, screen, BLACK)
        billy.Show(screen, scale, WHITE)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    billy.Move()

    cycles += 1

    if (billy.x, billy.y) == (startPoint[0],startPoint[1]) and cycles >= 4:

        running = False


if not displayMoves:

    display(tiles, screen, BLACK)
    billy.Show(screen, scale, WHITE)
    pygame.display.update()

end = time.time()

time = end - start

print('Time is: ' +str(time)+ ' for ' + str(squares) + ' squares')



      
                
