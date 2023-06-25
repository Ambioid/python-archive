height = 42
matrix = [[0 for x in range(height)]]
data = open("huffmanTree.txt", "r").read().splitlines()

encodedMessage = "1724cf8567eb02c3d384b21a63f588c5fd0b87a65c03ea4534a3fbf47e9d7207ac2b3f409a570847d18fbf585670f58002394a99fd0afa3ae482e60f42e1eb24172c82ade8923eb2488702c2beb11ca5eb287aace8fe8b2648050c8423efd6236734c7eb0acfd0660861f4d3a5019bd1a7ac2b387aa2d724c421e9a860940f582633807bf4afe8923e85c3d12362087a36f5d397aace427924611f5970fae9cbdfa80632845bd6429cbd6529d71940413dfff"
message = str(bin(int(encodedMessage, 16))[2:])

print(data)
key = {}

for y in range(height):  # Go through every row
    temp = ""

    for x in range(2, len(data[y])):  # Run loop through every character as long as its a number (1 or 0)
        temp += str(data[y][x])
        x += 1
        # print(data[y][x], int(temp))
    key[str(temp)] = data[y][:1]
print(key)

print("\n", key)
print(" Message:", message, "\n")

progress = 0
final = ''
i = 0


while message:  # Iterate once through list,
    i += 1
    temp = str(message)[:i]
    print(message, i)
    print(temp, "\n")


    if temp in key:            # start from left and smallest, check and increase until match
        final += str(key[temp])
        print("Found", temp, final, message, "\n")
        message = message[len(str(temp)):]
        i = 0
    if temp == "1111111":
        break


print(final)

# print(data)
