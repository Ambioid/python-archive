import time
import pygame
import random

# All the pygame setup
pygame.init()
width = 1000
height = width / 2
screen = pygame.display.set_mode([width, int(height)])
pygame.display.set_caption("Snake")
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
waitTime = 0.5
clock = pygame.time.Clock()
length = 5
alive = True
size = (width/50)
spot =  [[size*round((width/2)/size),size*round((height/2)/size)]]
pointSpot = [[size*round((width/2)/size),size*round((height/2)/size)+size*3], [size*round((width/2)/size)+size*2,size*round((height/2)/size)+size*2]]
direction = 0
pointMax = 5
keyPressed = False

pygame.draw.rect(screen, white, [spot[0][0], spot[0][1], size, size])
pygame.display.flip()

print ("spot", pointSpot)

def detectKey(afterHead, head):
    global direction
    # Cycles through all the events currently occuring
    for event in pygame.event.get():
        # Condition becomes true when keyboard is pressed
        if event.type == pygame.KEYDOWN:

            if (event.key == pygame.K_UP or event.key == pygame.K_w) and afterHead[1] == head[1]:
                direction = "up"
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and afterHead[1] == head[1]:
                direction = "down"
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and afterHead[0] == head[0]:
                direction = "left"
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and afterHead[0] == head[0]:
                direction = "right"

def points():
    global pointSpot, length
    if len(pointSpot) < pointMax:
        pointSpot.append([(size * round(random.randrange(0, width - size) / size)),
                          (size * round(random.randrange(0, height - size) / size))])

    for k in range(0,len(pointSpot)-1):
        if spot[len(spot)-1] == pointSpot[k]:
            length += 1
            del pointSpot[k]

        #print("spot", pointSpot, pointSpot[k])
        pygame.draw.rect(screen, green, [pointSpot[k][0], pointSpot[k][1], size, size])

while direction == False:
    detectKey([0,0],[0,0])
print(direction)


while alive:
    pygame.event.get()
    #print(spot[len(spot)-1], spot[0])


    #time.sleep(waitTime)
    clock.tick(20)
    detectKey(spot[len(spot) - 2], spot[len(spot) - 1])
    if direction == "up":
        spot.append([spot[len(spot)-1][0], spot[len(spot)-1][1]-size])
    if direction == "down":
        spot.append([spot[len(spot)-1][0], spot[len(spot)-1][1]+size])
    if direction == "left":
        spot.append([spot[len(spot)-1][0]-size, spot[len(spot)-1][1]])
    if direction == "right":
        spot.append([spot[len(spot)-1][0]+size, spot[len(spot)-1][1]])

    screen.fill([0, 0, 0])
    for i in range(len(spot)):
        pygame.draw.rect(screen, [(50/len(spot)*i)+205,(50/len(spot)*i)+205,(50/len(spot)*i)+205], [spot[i][0], spot[i][1], size, size])
    if len(spot) > length:
        del spot[0]

    points()
    for j in range(0, len(spot)-1): #Detect Collisions against self
        #print (j, spot[i], spot[j])
        if spot[len(spot)-1] == spot[j]:
            alive = False

    # Detect Collisions against walls
    if spot[len(spot)-1][0]<size or spot[len(spot)-1][0]>width-size or spot[len(spot)-1][1] < size or spot[len(spot)-1][1] > height-size:
        alive = False




    pygame.display.flip()
print("Game Over! Score:", length)
time.sleep(10)