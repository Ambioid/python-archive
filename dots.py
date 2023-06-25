import random
import pygame
import time

# All the pygame setup
pygame.init()
width = 1000
height = width / 2
screen = pygame.display.set_mode([width, int(height)])
pygame.display.set_caption("Geometry")
white = (255, 255, 255)


dots = []
velocity = []


def new():
    side = random.randint(1,2) #1=x #2=y
    x = random.uniform(1, width)
    y = random.uniform(1, height)

    o = random.randint(0, 1)
    if side==1:
        x = width * o
    else:
        y = height * o
    if o == 0:
        o = 1
    else:
        o = -1
    speedx = (random.uniform(0, 2)/10 * o)
    speedy = (random.uniform(0, 2)/10 * o)

    dots.append([x, y])
    velocity.append([speedx,speedy])


for m in range(0, 35):
    new()

while True:
    pygame.event.get()
    screen.fill((0, 0, 0))
    for i in range(len(dots)):

        dots[i][0] += velocity[i][0]
        dots[i][1] += velocity[i][1]
        pygame.draw.circle(screen, white, dots[i], 3)

        for g in range(i, len(dots)):
            if ((abs((dots[i][0])-(dots[g][0]))**2 )+  (abs((dots[i][1])-(dots[g][1]))**2 ))**0.5 <150:
                pygame.draw.line(screen, white, dots[i], dots[g], 2)

        if dots[i][0] > width or dots[i][0] < 0 or dots[i][1] > height or dots[i][1] < 0:
            new()
            del dots[i]
            del velocity[i]

    pygame.display.flip()


