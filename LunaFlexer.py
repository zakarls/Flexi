import pygame, random, math, serial

pygame.init()

black = (0,0,0)
pink = (244,66,223)
white = (255,255,255)
size = 500,300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Luna Flexer")
done = False
pressed = False
clock = pygame.time.Clock()

threshold = 400
ser = serial.Serial('COM1', 9600)

def ball(x,y): #draw ball
    pygame.draw.circle(screen,black,[x,y],10)

def moveBar(x1,y1,x,y): #draw bar
    pygame.draw.rect(screen, pink, (x1,y1, x,y))

def updateBars(): #update bar position
    if not left_bar:
        for i in range(len(left_bar)):
            moveBar(left_bar[i][0]-5,left_bar[i][1],75,10)
            left_bar[i][0]-=5
            if left_bar[i][1]>900:
                left_bar[i] = []
    if not right_bar:
        for i in range(len(right_bar)):
            moveBar(right_bar[i][0]+5,right_bar[i][1],75,10)
            right_bar[i][0]+=5
            if right_bar[i][1] >900:
                right_bar[i] = []

#def barLine:
def drawLine(x1,y1,x2,y2):
    pygame.draw.line(screen,pink,[x1,y1],[x2,y2],4)

'''def updateLine():
    if rotlines:
        rotate_lines(rotlines, 1)

def rotate_lines(self, deg):
    """ Rotate self.polylines the given angle about their centers. """
    theta = math.radians(deg)  # Convert angle from degrees to radians
    cosang, sinang = math.cos(theta), math.sin(theta)

    for pl in self.polylines:
        # Find logical center (avg x and avg y) of entire polyline
        n = len(pl.lines)*2  # Total number of points in polyline
        cx = sum(sum(line.get_xdata()) for line in pl.lines) / n
        cy = sum(sum(line.get_ydata()) for line in pl.lines) / n

        for line in pl.lines:
            # Retrieve vertices of the line
            x1, x2 = line.get_xdata()
            y1, y2 = line.get_ydata()

            # Rotate each around whole polyline's center point
            tx1, ty1 = x1-cx, y1-cy
            p1x = ( tx1*cosang + ty1*sinang) + cx
            p1y = (-tx1*sinang + ty1*cosang) + cy
            tx2, ty2 = x2-cx, y2-cy
            p2x = ( tx2*cosang + ty2*sinang) + cx
            p2y = (-tx2*sinang + ty2*cosang) + cy

            # Replace vertices with updated values
            pl.set_line(line, [p1x, p2x], [p1y, p2y])

rotlines = [[[300,300],[400,400]]]'''

left_bar = [[]]
right_bar = [[]]
bars = []
up = False
count = 0
x=540
y=700-10
velocity=0
accel = 1
totalPos = 0
movement = 0
font = pygame.font.SysFont(None, 25)

while not done:
    #Input
    voltage = float(ser.readLine())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
        if voltage >= threshold:
            if not pressed:
                up = True
                pressed = True
        if voltage <= threshold:
            pressed = False

    #Blank Screen
    screen.fill(white)

    #Update Ball
    if up:
        if count < 5:
            velocity = -20
            count+=1
        else:
            count = 0
            up = False
    if y<200:
        y+=(200-y)
    if not left_bar:
        for i in range(len(left_bar)):
            left_bar[i][1]+=(200-y)
    if not right_bar:
        for i in range(len(right_bar)):
            right_bar[i][1]+=(200-y)

    '''if not rotlines:
        for i in range(len(rotlines)):
            rotlines[i][0][1] += (200-y)
            rotlines[i][1][1] += (200-y)
    movement+=(200-y)
    if movement%400 == 0:
        def random.randint(0,2):
            return {
                '0': barLine,
                '1': rotLine,
                '2': laser
            }.get(x, 9)

    '''
    ball(x,y)
    #updateLine()
    updateBars()
    temp = y
    y+=velocity+accel
    if(y>700-15):
        y=700-15
    totalPos += int(temp-y)
    if accel == -40:
        velocity = 5
        accel = 1
    else:
        velocity += accel

    #Display Score
    text = font.render("Score: " + str(totalPos-5), True, black)
    screen.blit(text, [10, 10])

    #Flip Display
    pygame.display.flip()

    #Display Tick
    clock.tick(60)

pygame.quit()
