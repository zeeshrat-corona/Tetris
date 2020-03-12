import pygame
from gameboard_myname import Gameboard
from Shape_myname import Shape
import time
from gameboard_myname import gameboardHeight

from Shadowshape import Shadowshape
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Yellow = (255, 255, 0)

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.music.load("Dr Dre- Still Dre instrumental.mp3")
    pygame.mixer.music.play(-1)
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(" Tetris by Zeeshan")
    shape = Shape()
    nextshape = Shape()
    shadowshape = Shadowshape(shape.shapenum)
    myfont=pygame.font.Font('freesansbold.ttf',30)
    HSfont = pygame.font.Font('freesansbold.ttf',20)
    gameboard = Gameboard(White, nextshape.blocklist[0].size)
    done = False
    gameover = False
    name = ""
    pygame.mixer.init()
    newhssound = pygame.mixer.Sound("funmusic.wav")
    slowtimedelay = 0
    started = False
    nameList = [0 for y in range(5)]
    scoreList = [0 for y in range(5)]
    HSfile = open("hsscore.txt", "r")
    for i in range(5):
        nameList[i] = HSfile.readline().rstrip('\n')
    for i in range(5):
        scoreList[i] = HSfile.readline().rstrip('\n')
    HSfile.close()
def keycheck():
    if event.key == pygame.K_RIGHT:
        shape.moveright()
    if event.key == pygame.K_LEFT:
        shape.moveleft()
    if event.key == pygame.K_d:
        shape.movedown()
    if event.key == pygame.K_UP:
        shape.rotateclockwise()
    if event.key == pygame.K_DOWN:
        shape.rotatecounterclockwise()
    if event.key == pygame.K_SPACE:
        shape.drop()
        gameboard.score += (gameboardHeight - shape.blocklist[0].gridyPosition)
    if event.key == pygame.K_CAPSLOCK and gameboard.numslowtime > 0:
        gameboard.slowtimeon = True
        gameboard.numslowtime -=1

def drawscreen():
    screen.fill(Black)
    shape.draw(screen)
    gameboard.draw(screen)
    scoretext = myfont.render("Score: "+ str(gameboard.score),1,White)
    linetext = myfont.render ("Lines: "+ str(gameboard.numlines),1,White)
    gameboard.drawgridlines(screen)
    screen.blit(scoretext,(400,400))
    screen.blit(linetext,(400,350))
    HighScore = myfont.render('High Score:', 1, White)
    screen.blit(HighScore, (570, 50))
    pygame.draw.rect(screen,White, [570,100,170,150], 1)
    leveltext = myfont.render("Level :" + str(gameboard.level), 1, White)
    screen.blit(leveltext, (400, 300))
    nexttext = myfont.render('Next:',1,White)
    screen.blit(nexttext,(400,50))
    pygame.draw.rect(screen,White, [400,100,150,150], 1)
    poweruptext = myfont.render('Power Ups:', 1, White)
    screen.blit(poweruptext,(400,500))
    nextshape.drawnextshape(screen)
    numslowtimetext=myfont.render("x"+str(gameboard.numslowtime),1,White)
    numswaptext = myfont.render("x" + str(gameboard.numswap), 1, White)
    screen.blit(numswaptext,(650,525))
    screen.blit(numslowtimetext,(310,525))
    slowtime_image = pygame.image.load("clock.png")
    screen.blit(slowtime_image,(250,515))
    swap_image = pygame.image.load("swap.png")
    screen.blit(swap_image,(575,515))
    playertext = myfont.render((name),1,White)
    screen.blit(playertext,(575,400))
    shadowshape.draw(screen)
    for i in range(5):
        hsnametext = HSfont.render(str(nameList[i]),1,White)
        screen.blit(hsnametext,(580, i*25+125))
        HSscoretext = HSfont.render(str(scoreList[i]),1,Blue)
        screen.blit(HSscoretext,(685,i*25+125))
    pygame.display.flip()


while not started:
    bg = pygame.image.load("Tetris Title Page.jpg")
    screen.blit(bg, (0, 0))
    PressAnyKeyToStart = myfont.render('Press any Key To Start', 1, Red)
    screen.blit(PressAnyKeyToStart, (210, 225))
    PleaseEnterYourName = myfont.render('Please Enter Your Name:', 1, Yellow)
    screen.blit(PleaseEnterYourName, (197, 400))
    nametext = myfont.render(name,1,White)
    screen.blit(nametext,(197,450))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key >= 33 and event.key<= 126 and len(name)<= 10:
                name = name + chr(event.key)
            if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
            if event.key == pygame.K_RETURN:
                if name == "":
                    name ="Peasant1"
                started=True


    def checkHS():
        newHighScore = False
        tempnamelist = [0 for y in range(5)]
        tempscorelist = [0 for y in range(5)]
        for i in range(5):
            if gameboard.score > int(scoreList[i]) and newHighScore == False:
                newHighScore = True
                tempscorelist[i] = gameboard.score
                tempnamelist[i] = name
                newhssound.play()
            elif newHighScore == True:
                tempscorelist[i] = scoreList[i - 1]
                tempnamelist[i] = nameList [i-1]
            else:
                tempscorelist[i] = scoreList[i]
                tempnamelist[i] = nameList[i]

        for i in range(5):
            scoreList[i] = tempscorelist[i]
            nameList[i] = tempnamelist[i]

        HSfile = open('hsscore.txt', 'w')

        for i in range(5):
            HSfile.write(nameList[i] + "\n")
        for i in range(5):
            HSfile.write(str(scoreList[i]) + "\n")

        HSfile.close()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            keycheck()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            shape.drop()
    shadowshape.update(shape)

    shape.falling()
    time.sleep(0.25 - gameboard.level * 0.04)
    if gameboard.slowtimeon == True:
        slowtimedelay +=1
        if slowtimedelay ==24:
            slowtimedelay= 0
            gameboard.slowtimeon = False
        time.sleep(0.25 - gameboard.level * 0.01)
    if shape.active == False:
        gameboard.clearfullrows()
        shape = nextshape
        shadowshape = Shadowshape(shape.shapenum)
        nextshape = Shape()
    if gameboard.getlost():
        checkHS()
        print('L')
        gameover = True

    while gameover:
        bg1 = pygame.image.load('gameover.jpg')
        screen.blit(bg1,(0,0))

        PressAnyKeyToStart1 = myfont.render('Press any Key To Start', 1, Red)
        screen.blit(PressAnyKeyToStart1, (210, 75))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                shape = Shape()
                nextshape = Shape()
                gameboard = Gameboard(White, shape.blocklist[0].size)
                gameover = False

    drawscreen()
