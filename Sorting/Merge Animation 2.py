import random
import pygame
import time
import math

# This is a 2nd version, because it shows the merge process itself rather than snapshots.
# I have highlisted the 0th element of each sublist to show where they start/end

# This is iterative merge sort, so it uses loops instead of recursion. I like it better this way

# Pygame setup and configuration stuff. Feel free to edit this, esp width and list length

inNums = list(range(1,2**8)) #Generates List of Nums: Edit this for different lengths

pygame.init()
width = 2000
height = width//2
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Merge Sort")
rectDistance = 1
rectWidth = width / ((len(inNums) * rectDistance))
waitTime = 0.5

random.shuffle(inNums)
nums = [[x] for x in inNums]
print(nums, "\n")

print(inNums, "\nSorting Begin:\n")


def draw(color, layer, num, pos, highlighted):
    if highlighted:
        color = (0, 0, 200)
    pygame.draw.rect(screen, color,
    [(rectWidth * rectDistance * (pos - 0.25))-rectWidth,(height / 10)*(layer+1), rectWidth,(height / 2 / len(inNums) * num)], 0)
    # width X distance & iteration            # top at 1/6        #width   # height


def drawAll(color):
    screen.fill((0, 0, 0))
    pos = 0
    for i in range(len(nums)):  # go through the sublists list
        for j in range(len(nums[i])): 
            pos += 1
            
            first = False # the blue is used to highlight the 1st of each sublist
            if j == 0:
                first = True
            draw(color, 1, nums[i][j], pos, first)


drawAll((255, 255, 255))
pygame.display.flip()
time.sleep(1)


# Run through enough to merge everything
for o in range(int(math.log(len(nums), 2))+1):  # Log finds how many line repeats
    
    for i in range(0, len(nums) // 2, 1):  # Run through each line's sublists

        nums.insert(i + 2, [])  # Add an empty replacement list

        while nums[i] or nums[i + 1]:  # Keep iterating until both empty
            drawAll((255, 255, 255))
            pygame.display.flip()
            time.sleep(0.01)
            # Empties both lists out to replacement, in order
            if (nums[i+1] < nums[i] and nums[i+1]) or nums[i] == []:

                nums[i + 2].insert(len(nums[i+2]), nums[i + 1][0])
                nums[i + 1].pop(0)
            else:
                nums[i + 2].insert(len(nums[i+2]), nums[i][0])
                nums[i].pop(0)

        nums = [x for x in nums if x]  # After that, clear the 2 lists

    print(nums)
    time.sleep(waitTime)

print((nums[0] == sorted(nums[0])))
print("\nSorting Finished. Final numbers:\n", nums[0])

drawAll((0, 255, 0))
pygame.display.flip()
time.sleep(3)
