
import pygame


# All the pygame setup
pygame.init()
width  = 600
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("N Body")

running = True
white = [255,255,255]

while running:

    pygame.event.get()
    screen.fill([0, 0, 0])
    pygame.draw.circle(screen, white, [width/2, height/2], 20 )


    pygame.display.flip()