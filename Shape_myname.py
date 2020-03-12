import pygame
import random
from block_myname import Block
from gameboard_myname import gameboardWidth
from gameboard_myname import gameboardHeight
from gameboard_myname import activeBoardcolor
from gameboard_myname import activeBoardspot
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)
Magenta = (255, 0, 255)
Turquoise = (0, 206, 209)
zShape = [[(gameboardWidth/2) - 1, 0], [(gameboardWidth/2) - 2, 0],[(gameboardWidth/2) - 1,1],[(gameboardWidth/2) - 0, 1]]
lineShape = [[(gameboardWidth/2) - 1,0], [(gameboardWidth/2) - 2, 0],[(gameboardWidth/2) + 1, 0],[(gameboardWidth/2) + 0,0]]
squareShape = [[(gameboardWidth/2) - 1,0],[(gameboardWidth/2) - 0,1], [(gameboardWidth/2) - 1,1], [(gameboardWidth/2) + 0,0]]
lShape = [[(gameboardWidth/2) - 1,1], [(gameboardWidth/2) - 1,0], [(gameboardWidth/2) - 1,2], [(gameboardWidth/2) - 2,2]]
sShape = [[(gameboardWidth/2) - 1,0], [(gameboardWidth/2) + 0, 0], [(gameboardWidth/2) - 1,1], [(gameboardWidth/2) - 2,1]]
mlShape = [[(gameboardWidth/2) - 1,1], [(gameboardWidth/2) - 1,0], [(gameboardWidth/2) - 1,2], [(gameboardWidth/2) - 2,0]]
tShape = [[(gameboardWidth/2) - 1,1], [(gameboardWidth/2) - 1,0], [(gameboardWidth/2) - 0,1], [(gameboardWidth/2) - 2,1]]
allShapes  = [zShape, lineShape, lShape, squareShape, sShape, mlShape, tShape]
allColors = [Red, Blue, White, Yellow, Magenta, Turquoise, Green]


class Shape():
    def __init__(self):
        self.numblocks = 4
        self.blocklist = []
        randomNumber = random.randrange(7)
        self.shapenum = randomNumber
        self.shape = allShapes[self.shapenum]
        self.color = allColors[self.shapenum]
        for i in range(self.numblocks):
            self.blocklist.append(Block(self.color,  self.shape[i][0], self.shape[i][1]))
        self.active = True



    def rotateclockwise(self):
        canrotate=True
        newblockx = [0, 0, 0, 0]
        newblocky = [0, 0, 0, 0]
        if self.shape != squareShape:
            for i in range(self.numblocks):
                newblockx[i] = -(self.blocklist[i].gridyPosition - self.blocklist[0].gridyPosition) + self.blocklist[0].gridxPosition
                newblocky[i] = (self.blocklist[i].gridxPosition - self.blocklist[0].gridxPosition) + self.blocklist[0].gridyPosition
                if newblockx[i] >= gameboardWidth-1 or newblockx[i] < 0:
                    canrotate=False
                elif newblocky[i] >= gameboardHeight:
                    canrotate=False
                elif activeBoardspot[newblockx[i]][newblocky[i]]:
                    canrotate= False
            if canrotate:
                for i in range(self.numblocks):
                    self.blocklist[i].gridxPosition = newblockx[i]
                    self.blocklist[i].gridyPosition = newblocky[i]

    def rotatecounterclockwise(self):
        canrotate = True
        newblockx = [0, 0, 0, 0]
        newblocky = [0, 0, 0, 0]
        if self.shape != squareShape:
            for i in range(self.numblocks):
                newblockx[i] = (self.blocklist[i].gridyPosition - self.blocklist[0].gridyPosition) + self.blocklist[0].gridxPosition
                newblocky[i] = -(self.blocklist[i].gridxPosition - self.blocklist[0].gridxPosition) + self.blocklist[0].gridyPosition

                if newblockx[i] >= gameboardWidth or newblocky[i] < 0:
                    canrotate = False
                elif newblocky[i] >= gameboardHeight:
                    canrotate = False
                elif activeBoardspot [newblockx[i]] [newblocky[i]]:
                    canrotate = False

            if canrotate:
                for i in range(self.numblocks):
                    self.blocklist[i].gridxPosition = newblockx[i]
                    self.blocklist[i].gridyPosition = newblocky[i]

    def moveleft(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridxPosition == 0 or activeBoardspot[self.blocklist[i].gridxPosition-1][self.blocklist[i].gridyPosition]:
                blocked = True
        if not blocked:
            for i in range(self.numblocks):
                self.blocklist[i].gridxPosition -= 1

    def moveright(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridxPosition == gameboardWidth - 1 or activeBoardspot[self.blocklist[i].gridxPosition+1][self.blocklist[i].gridyPosition]:
                blocked = True
        if not blocked:
            for i in range(self.numblocks):
                self.blocklist[i].gridxPosition += 1

    def movedown(self):
        blocked = False
        for i in range(self.numblocks):
            if self.blocklist[i].gridyPosition == gameboardHeight - 1 or activeBoardspot[self.blocklist[i].gridxPosition][self.blocklist[i].gridyPosition+1]:
                blocked = True
        if not blocked:
            for i in range(self.numblocks):
                self.blocklist[i].gridyPosition += 1

    def draw(self, screen):
        for i in range(self.numblocks):
            self.blocklist[i].draw(screen)
    def falling(self):
        for i in range(self.numblocks):
            if self.blocklist[i].gridyPosition == gameboardHeight -1 or activeBoardspot[self.blocklist[i].gridxPosition][self.blocklist[i].gridyPosition + 1]:
               self.hitbottom()
        for i in range(self.numblocks):
            if self.active == True:
                self.blocklist[i].gridyPosition+=1

    def hitbottom(self):
        for i in range (self.numblocks):
            activeBoardspot[self.blocklist[i].gridxPosition][self.blocklist[i].gridyPosition] = True
            activeBoardcolor[self.blocklist[i].gridxPosition][self.blocklist[i].gridyPosition] = self.blocklist[i].color
        self.active = False

    def drop(self):
        while self.active:
            for i in range (self.numblocks):
                if self.blocklist[i].gridyPosition == gameboardHeight - 1 or activeBoardspot[self.blocklist[i].gridxPosition][self.blocklist[i].gridyPosition +1]:
                    self.hitbottom()
            for i in range (self.numblocks):
                if self.active:
                    self.blocklist[i].gridyPosition += 1
    def drawnextshape(self,screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen,self.blocklist[i].color,[self.blocklist[i].gridxPosition*self.blocklist[i].size + 325, self.blocklist[i].gridyPosition * self.blocklist[i].size + 150, self.blocklist [i].size -1, self.blocklist[i] .size -1], 0)
