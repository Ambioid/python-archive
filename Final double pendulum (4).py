import pygame
import math
import random

mass1 = [4]
mass2 = [5]
length1 = [1000]
length2 = [1000]
angle1 = [-2]
angle2 = [2.2]
velocity1 = [0]
velocity2 = [0]

thickness = 3
grav = 1
total = 250
angleDiff = -0.0000001
FPS = 60

pygame.init()
width = 800
height = 750
screen = pygame.display.set_mode([width, int(height)])
pygame.display.set_caption("pendulum")
white = (255, 255, 255)
grey = (150,150,150)
hsb = pygame.Color(0, 0, 0)
#hsb = pygame.Color.hsva(0, 0, 0, 0)



clock = pygame.time.Clock()

for i in range(total-1):
    mass1.append(mass1[i])
    mass2.append(mass2[i])
    length1.append(length1[i])
    length2.append(length2[i])
    velocity1.append(velocity1[i])
    velocity2.append(velocity2[i])
    angle1.append(angle1[i] + angleDiff)
    angle2.append(angle2[i] + angleDiff)


while True:

    screen.fill([0,0,0])
    pygame.event.get()
    clock.tick(FPS)

    center = [width/2, height/10*4]


    for i in range(total):
        pygame.draw.circle(screen, white, center, 3)

        #print(velocity1[i], velocity2[i])
        while velocity1[i] > 10:
            velocity1[i] /= 10

        while velocity1[i] < -10:
            velocity1[i] /= 10

        while velocity2[i] > 10:
            velocity2[i] /= 10

        while velocity2[i] < -10:
            velocity2[i] /= 10


        acceleration1 = ((-grav * (2 * mass1[i] + mass2[i]) * math.sin(angle1[i])) + (-mass2[i] * grav * math.sin(angle1[i]-2*angle2[i])) + (-2*math.sin(angle1[i]-angle2[i])*mass2[i])*((velocity2[i]**2) * length2[i] + (velocity1[i]**2)*length1[i]*math.cos(angle1[i]-angle2[i]))) / (length1[i] * (2*mass1[i]+mass2[i]-mass2[i]*math.cos(2*angle1[i]-2*angle2[i])))
        acceleration2 = ((2 * math.sin(angle1[i]-angle2[i]))*(((velocity1[i]**2)*length1[i]*(mass1[i]+mass2[i]))+(grav * (mass1[i] + mass2[i]) * math.cos(angle1[i]))+((velocity2[i]**2)*length2[i]*mass2[i]*math.cos(angle1[i]-angle2[i])))) / (length2[i] * (2*mass1[i]+mass2[i]-mass2[i]*math.cos(2*angle1[i]-2*angle2[i])))


        velocity1[i] += acceleration1
        velocity2[i] += acceleration2

        angle1[i] += velocity1[i]*0.99
        angle2[i] += velocity2[i]*0.99


        pendulumEnd1 = [math.sin(angle1[i])*length1[i]/6+(center[0]),
                        math.cos(angle1[i])*length1[i]/6+(center[1])]
        pendulumEnd2 = [math.sin(angle2[i]) * length2[i]/6 + pendulumEnd1[0],
                        math.cos(angle2[i]) * length2[i]/6 + pendulumEnd1[1]]

        hsb.hsva = ((i / (total / 360)), 100, 90, 100)

        pygame.draw.line(screen, hsb, center, pendulumEnd1, thickness)
        pygame.draw.line(screen, hsb, pendulumEnd1, pendulumEnd2, thickness)

        hsb.hsva = ((i / (total / 360)), 70, 70, 100)
        pygame.draw.circle(screen, hsb, pendulumEnd2, mass1[i])
        pygame.draw.circle(screen, hsb, pendulumEnd1, mass1[i])

    pygame.display.flip()
