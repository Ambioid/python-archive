import random

numbers = list(range(1,9))  # Create a list of numbers
random.shuffle(numbers)  # Random order
#numbers.reverse()

swaps = 0
i = 0
print(numbers, "\nSorting Begin:\n")
while True:
    random.shuffle(numbers)
    # print (numbers[i])
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:  # If the one in front is larger than the one after
            sorted = False

        i += 1


    # Reaching the end of a line
    print(numbers)
    i = 0
    if sorted == True:
       break
    else:
       sorted = True


    # print(i)

# if numbers[i] > numbers[i + 1]:
#    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print("Sorting Finished. Final numbers:")
print(numbers)