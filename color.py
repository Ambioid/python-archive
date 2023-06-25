import pygame

pygame.init()
width = 800
height = 750
screen = pygame.display.set_mode([width, int(height)])
pygame.display.set_caption("Colors")
white = (255, 255, 255)
grey = (150,150,150)
hsb = pygame.Color(0, 0, 0)
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


while True:
    for i in range(36):
        hsb.hsva = (i*10, 100, 90, 100)
        screen.fill(hsb)
        pygame.display.flip()