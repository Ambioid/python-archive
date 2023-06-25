import pygame
import random

# Started but never finished this one
pygame.init()
width  = 600
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("N Body")

running = True
white = [255,255,255]


resolution = 60

columns = int(width/resolution)
rows = int(height/resolution)
field = [[0 for x in range(rows)] for y in range(columns)]


for x in range(columns):
    for y in range(rows):
        field[y][x] = random.random()
        field[y][x] = random.randrange(0,2)


print(field)
while running:
    pygame.event.get()
    screen.fill([127,127,127])
    for x in range(columns):
        for y in range(rows):
            pygame.draw.circle(screen, [field[x][y]*255, field[x][y]*255, field[x][y]*255], [x*resolution+resolution/2, y*resolution+resolution/2], 10 )


    pygame.display.flip()