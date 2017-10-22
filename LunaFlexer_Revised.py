import pygame, random, math, serial

pygame.init()

black = (0,0,0)
pink = (244,66,223)
white = (255,255,255)
size = [1000,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flexi")
done = False
pressed = False
clock = pygame.time.Clock()

ser = serial.Serial('COM1', 9600)

def ball(x,y): #draw ball
    pygame.draw.circle(screen,black,[x,y],10)

def moveBar(x1,y1,x,y): #draw bar
    pygame.draw.rect(screen, pink, (x1,y1, x,y))

def updateBars(): #update bar position
    if bar:
        for i in range(len(bar)):
            moveBar(bar[i][0]-5,bar[i][1],25,75)
            bar[i][0]-=5
            if bar[i][1]<-30:
                bar[i] = []

def createBar():
    bar.append([1000,425])
#def barLine:


bar = [[1000,425]]
up = False
count = 0
x=15
y=500-15
velocity=0
accel = 1
totalPos = 0
movement = 0
xmov = 0
start = False
font = pygame.font.SysFont(None, 25)
counter = 0
while not done:
    #Input


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
        if event.type == pygame.KEYDOWN:
            if not start:
                xmov = 3
                start = True
            if event.key == pygame.K_UP:
                if not pressed:
                    up = True
                    pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed = False

    voltage = float(ser.readline())
    if voltage >= 400:
        if not start:
            xmov = 3
            start = True
            if not pressed:
                up = True
                pressed = True
    else:
        pressed = False

    if not start:
        text = font.render("Flex To Start", True, black)
    #Blank Screen
    screen.fill(white)
    screen.blit(text, [150, 150])
    #Update Ball
    if up:
        if count < 5:
            velocity = -15
            count+=1
        else:
            count = 0
            up = False
    if(y>500-15):
        y=500-15
    if(x>500):
        x=500
    ball(x,y)
    counter+=1
    if counter>=80:
        counter = 0
        createBar()
    updateBars()
    y+=velocity+accel
    if accel == -40:
        velocity = 5
        accel = 1
    else:
        velocity += accel
    x+=xmov
    totalPos+=xmov
    #Display Score
    if start:
        text = font.render("Score: " + str(int(totalPos/12)), True, black)
        screen.blit(text, [10, 10])

    #Flip Display
    pygame.display.flip()

    #Display Tick
    clock.tick(60)
pygame.quit()
