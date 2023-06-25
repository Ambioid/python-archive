import random
import pygame
import time

numbers = list(range(1, 21))  # Create a list of numbers
random.shuffle(numbers)  # Random order
# numbers.reverse()

# All the pygame setup
pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Insertion Sort")
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 255, 0)
waitTime = 0.5
rectDistance = 1.5
rectWidth = width / ((len(numbers) * rectDistance))

print(numbers, "\nSorting Begin:\n")
i = 0

def draw(color, j):
    pygame.draw.rect(screen, color,
                     [(rectWidth * rectDistance * (j + 0.75)) - rectWidth, (height / 4), rectWidth,
                      (height / 2 / len(numbers) * numbers[j])], 0)



def drawAll(color):
    screen.fill((0, 0, 0))
    j = 0
    while (j < len(numbers)):  # Draw the actual shapes
        draw(color, j)
        j = j + 1



j = 1
drawAll(white)
pygame.display.flip()
time.sleep(1)

while True:
    pygame.event.get()
    print("Numbers:", numbers)


    drawAll(white)
    draw(red, i)
    draw(red, i + 1)
    pygame.display.flip()
    time.sleep(waitTime / 2)  # pause for one second

    if numbers[i] > numbers[i + 1]:  # If the one in front is larger than the one after
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        sorted = False

        print("Numbers:", numbers)


        drawAll(white)
        draw(red, i)
        draw(red, i + 1)
        pygame.display.flip()
        time.sleep(waitTime / 2)  # pause for one second

        if i > 0:
            i -= 1
    else:
        i += 1

    if i >= len(numbers) - 1:  # Reaching the end of a line
        i = 0
        if sorted == True:
            break
        else:
            sorted = True

drawAll(white)
pygame.display.flip()


print("Sorting Finished. Final numbers:")
print(numbers)
drawAll(green)
pygame.display.flip()
time.sleep(5)
