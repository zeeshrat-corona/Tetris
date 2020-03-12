import pygame

gameboardWidth = 12
gameboardHeight = 20
activeBoardspot = []
activeBoardcolor = []
pygame.init()
Gray = (105,105,105)
linesound = pygame.mixer.Sound("sos-morse-code_daniel-simion.wav")
for i in range(gameboardWidth):
    rowspot= []
    rowcolor = []
    for j in range(gameboardHeight):
        rowspot.append(0)
        rowcolor.append(0)
    activeBoardcolor.append(rowcolor)
    activeBoardspot.append(rowspot)

class Gameboard:
    def __init__(self, color, blocksize):
        self.numslowtime = 654
        self.borderColor = color
        self.multiplier = blocksize
        self.score = 0
        self.numlines = 0
        self.templeveltracker = 0
        self.level = 1
        self.slowtimeon = False
        self.numswap = 1
        self.swapping = False
        for i in range(gameboardWidth):
            for j in range(gameboardHeight):
                activeBoardspot[i][j] = False
                activeBoardcolor[i][j] = (0, 0, 0)


    def draw(self, screen):
        pygame.draw.rect(screen, self.borderColor, [0, 0, self.multiplier*gameboardWidth, self.multiplier*gameboardHeight], 1)
        for i in range(gameboardWidth):
            for j in range(gameboardHeight):
                if activeBoardspot[i][j] == True:
                    pygame.draw.rect(screen, activeBoardcolor[i][j], [i*self.multiplier, j*self.multiplier, self.multiplier-1, self.multiplier-1], 0)

    def getlost(self):

        for i in range(gameboardWidth):
            if activeBoardspot[i][0]:
                return True
        return False
    def completeline(self,rownum):
        for i in range (gameboardWidth):
            if not activeBoardspot[i][rownum]:
                return False
        return True
    def clearfullrows(self):
        for i in range(gameboardHeight):
            if self.completeline(i):
                self.score += 40
                self.numlines += 1
                self.templeveltracker += 1
                if self.templeveltracker == 10:
                    self.level += 1
                    self.templeveltracker = 0
                for j in range (i,1,-1):
                    for r in range(gameboardWidth):
                        activeBoardspot[r][j]=activeBoardspot[r][j-1]
                        activeBoardcolor[r][j] = activeBoardcolor[r][j-1]
                for k in range(gameboardWidth):
                     activeBoardspot[k][0] = False
                     activeBoardcolor[k][0] = (0,0,0)
                linesound.play()
    def drawgridlines(self,screen):
        for i in range(gameboardWidth):
            for j in range(gameboardHeight):
                pygame.draw.rect(screen,Gray,[i*25,j*25,25,25],1)