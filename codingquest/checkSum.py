length = 11
height = 19
matrix = [[0 for x in range(length)] for y in range(height)]
data = open("checkSums.txt", "r").read().split()

for i in range(len(data)):
    data[i] = int(data[i], 16)

for y in range(height):
    for x in range(length):
        try:
            matrix[y][x] = data[x + (length * y)]
        except:
            pass
del matrix[height-1][length-1]


for y in range(height-1):
    if (sum(matrix[y])-matrix[y][length-1]) % 256 != matrix[y][length-1]:
        # Add every part in row together (Sum) then subtract the checksum, and see if the mod of that is same as sum
        difference = (sum(matrix[y])-matrix[y][length-1]) % 256 - matrix[y][length-1]
        print("Row", y, difference, False)
        errY = y #erroneousY

for x in range(length-1):
    #print((sum( [ i[x] for i in matrix] )-matrix[height-1][x]) % 256)
    if (sum( [ i[x] for i in matrix] )-matrix[height-1][x]) % 256 != matrix[height-1][x]:
        #difference = (sum( [ i[x] for i in matrix] )-matrix[height-1][x]) - matrix[height-1][x]
        print("Column", x, difference, False)
        errX = x #erroneousX

print("Erronious spot is:", matrix[errY][errX])
print("Correct Value is:", matrix[errY][errX]-difference)
print("Input Value:", matrix[errY][errX]*(matrix[errY][errX]-difference))

print("")
for i in range(height):
    print(matrix[i])
