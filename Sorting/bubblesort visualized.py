# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import pygame
import time

# All the pygame setup
pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Bubble Sort")
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)



waitTime = 0.01
numbers = list(range(1, 21))  # Create a list of numbers
random.shuffle(numbers)  # Random order
print(numbers)  # prints..... the numbers......

rectDistance = 2
rectWidth = width/((len(numbers)*rectDistance)+1)


i = 0



def draw (color, j):
    pygame.draw.rect(screen, color,
        [(rectWidth * rectDistance * (j+1)) - rectWidth, (height / 4), rectWidth, (height / 2/len(numbers)*(numbers[j]))], 0)
                          # width X distance & iteration            # top at 1/6        #width   # height



def drawAll(color):
    screen.fill((0, 0, 0))
    j = 0
    while (j != len(numbers)):  # Draw the actual shapes
        draw(color, j)
        j = j + 1

j = 0
drawAll(white)

i = 0
print("Sorting Begin")

pygame.display.flip()


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break





    drawAll(white)
    draw(red,i)
    draw(red,i+1)
    pygame.display.flip()
    time.sleep(waitTime / 2)  # pause for one second

    if numbers[i] > numbers[i + 1]:  # If the one in front is larger than the one after
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        sorted = False
        print(numbers)


        drawAll(white)
        draw(red, i)
        draw(red, i + 1)
        pygame.display.flip()
        time.sleep(waitTime / 2)  # pause for one second


    i = i + 1
    if i >= len(numbers) - 1:  # Reaching the end of a line
        i = 0
        if sorted == True:
            break
        else:
            sorted = True

    pygame.display.flip()



print("Sorting Finished. Final numbers:")
print(numbers)

drawAll(green)
pygame.display.flip()
time.sleep(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
