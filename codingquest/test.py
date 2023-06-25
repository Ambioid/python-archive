height = 42
data = open("huffmanTree.txt", "r").read().splitlines()
key = {}
print(key)

for y in range(height):  # Go through every row
    temp = ""

    for x in range(2, len(data[y])):  # Run loop through every character as long as its a number (1 or 0)
        print(x,y)
        temp += str(data[y][x])
        x += 1
        # print(data[y][x], int(temp))
    key[str(temp)] = data[y][:1]
    # print("\n")
print(key)