import pygame
import random
from block_myname import Block
from gameboard_myname import gameboardWidth
from gameboard_myname import gameboardHeight
from gameboard_myname import activeBoardcolor
from gameboard_myname import activeBoardspot
from Shadowblock import shadowblock
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


class Shadowshape():
    def __init__(self,shapenum):
        self.numblocks = 4
        self.bottomblocklist = []
        self.shape = allShapes[shapenum]
        self.color = allColors[shapenum]
        self.atbottom = False

        for i in range(self.numblocks):
            self.bottomblocklist.append(shadowblock(self.color,  self.shape[i][0], self.shape[i][1]))


    def draw(self, screen):
        for i in range(self.numblocks):
            self.bottomblocklist[i].draw(screen)
    def update(self,shape):
        for i in range(self.numblocks):
            self.bottomblocklist[i].gridxPosition = shape.blocklist[i].gridxPosition
            self.bottomblocklist[i].gridyPosition = shape.blocklist[i].gridyPosition
        while not self.atbottom:
            for i in range(4):
                if self.bottomblocklist[i].gridyPosition == gameboardHeight - 1 or \
                        activeBoardspot[self.bottomblocklist[i].gridxPosition][self.bottomblocklist[i].gridyPosition + 1]:
                    self.atbottom=True
            for i in range(self.numblocks):
                if self.atbottom == False:
                    self.bottomblocklist[i].gridyPosition += 1
        self.atbottom = False


