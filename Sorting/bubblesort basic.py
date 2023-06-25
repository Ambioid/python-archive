import random

numbers = list(range(1, 21))  # Create a list of numbers
random.shuffle(numbers)  # Random order
numbers = ["Edna", "Adam", "Victor", "Charlie", "Jack", "Ken", "Maria"]
#numbers.reverse()

print(numbers)
swaps = 0
i = 0
print("Sorting Begin")
while True:

    # print (numbers[i])

    if numbers[i] > numbers[i + 1]:  # If the one in front is larger than the one after
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        sorted = False
        swaps += 1
        print(numbers, end = ": ")
        print(swaps)

    i += 1
    if i >= len(numbers) - 1:  # Reaching the end of a line
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
