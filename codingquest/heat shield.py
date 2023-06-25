data = open("heat shield.txt", "r").read().split("\n")
#print(data)


width = 20000
height = 100000
matrix = [[1 for x in range(width)] for y in range(height)]

for i in range(len(data)):
    split = data[i].split(" ")

    print(i)
    split[0] = int(split[0])
    split[1] = int(split[1])
    split[2] = int(split[2])
    split[3] = int(split[3])
    #print("\nShield", data[i])

    rows    = range(split[0], split[0]+split[2])
    columns = range(split[1], split[1]+split[3])
    #print(f'{rows}\n{columns}')
    for row in (rows):
        for column in (columns):
            try:
                matrix[column][row] = 0
            except:
                pass

#    for c in range(len(matrix)):
#        print(matrix[c])
#print("")
#for i in range(len(matrix)):
#    print(matrix[i])

print("Total Empty:", sum(list(map(sum, matrix))))