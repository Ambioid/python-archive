import random

numbers = list(range(1, 2001))  # Create a list of numbers
random.shuffle(numbers)  # Random order
#numbers.reverse()


print(numbers)
print("Begin sort!")

i = 0
swaps = 0

while True:

    print(numbers, end=": ")
    print(swaps)

    if numbers[i] > numbers[i + 1]:  # If the one in front is larger than the one after
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        sorted = False
        swaps += 1
        print(numbers, end = ": ")
        print(swaps)
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


print("Sorting Finished. Final numbers:")
print(numbers)
