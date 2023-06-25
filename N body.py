import pygame
import time
import math

# All the pygame setup
pygame.init()
width = 900
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("N Nbody")


running = True
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
yellow = [200, 200, 0]
grey = [100, 100, 100]


def drawLines(i):
    pygame.draw.line(screen, red, [Nbody[i].x, Nbody[i].y], [accX * 1000 + Nbody[i].x, accY * 1000 + Nbody[i].y])
    pygame.draw.line(screen, red, [Nbody[i].x, Nbody[i].y], [accX * 1000 + Nbody[i].x, Nbody[i].y])
    pygame.draw.line(screen, red, [Nbody[i].x, Nbody[i].y], [Nbody[i].x, accY * 1000 + Nbody[i].y])

    Nbody[i].coordList.append([Nbody[i].x, Nbody[i].y])
    for c in range(len(Nbody[i].coordList) - 1):
        pygame.draw.line(screen, pygame.color.Color('White'), Nbody[i].coordList[c], Nbody[i].coordList[c + 1], 1)

    if len(Nbody[i].coordList) > 600:
        del Nbody[i].coordList[0]


def drawDist():
    if len(Nbody) == 3:
        lineCenters = []
        for i in range(len(Nbody)-1):
            for u in range(i, len(Nbody)):
                if i == u:
                    continue
                pygame.draw.line(screen, grey, [Nbody[i].x, Nbody[i].y], [Nbody[u].x, Nbody[u].y])
                lineCenters.append([(Nbody[i].x + Nbody[u].x) / 2, (Nbody[i].y + Nbody[u].y) / 2])

        lineCenters.reverse()
        for i in range(len(Nbody)):
            pygame.draw.line(screen, red, [Nbody[i].x, Nbody[i].y], [lineCenters[i][0], lineCenters[i][1]])


class body:
    def __init__(self, size, color, x, y, xSpeed, ySpeed):
        self.size = size
        self.xSpeed = xSpeed / 10
        self.ySpeed = ySpeed / 10
        self.x = x
        self.y = y
        self.color = color
        self.coordList = []


Nbody = [body(100, green, 400, 300, 0.5, 0), body(10, blue, 200, 500, -3.5, -3)] # 2 body orbit
Nbody = [body(10, green, 200, 200, 0, 0), body(10, blue, 450, 450, 0, 0), body(10, red, 600, 100, 0, 0)]

while running:
    screen.fill((10, 10, 20))
    pygame.event.get()

    #time.sleep(0.005)


    for i in range(len(Nbody)):  # For loop, every iteration for every Body's internal physics
        for u in range(len(Nbody)):  # Repeat, every iteration for attraction between different body
            if u == i:
                continue

            yDist = (Nbody[u].y - Nbody[i].y)
            xDist = (Nbody[u].x - Nbody[i].x)

            distance = (((abs(xDist) ** 2) + (abs(yDist) ** 2)) ** 0.5)  # Hypotunse, both multiplied together

            if distance == 0:
                force = 0
            else:
                force = (Nbody[u].size * Nbody[i].size) / distance ** 2

            #if distance < Nbody[i].size + Nbody[u].size:
            #    force *= (distance / (Nbody[i].size + Nbody[u].size))**2

            accX = force * math.cos(math.atan2(yDist, xDist)) / Nbody[i].size
            accY = force * math.sin(math.atan2(yDist, xDist)) / Nbody[i].size

            Nbody[i].xSpeed += accX
            Nbody[i].ySpeed += accY

    for i in range(len(Nbody)):
        Nbody[i].x += Nbody[i].xSpeed
        Nbody[i].y += Nbody[i].ySpeed

        pygame.draw.circle(screen, Nbody[i].color, [Nbody[i].x, Nbody[i].y], Nbody[i].size)

        drawLines(i)
    drawDist()
    pygame.display.flip()
