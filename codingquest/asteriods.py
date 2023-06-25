length = 100
matrix = [[0 for x in range(length)] for y in range(length)]
data = open("asteriods.txt", "r").read().split()

asteroids = []
asteroidCount = 0
for i in range(length):
    for u in range(length):
        matrix[i][u] = int(data[u + length * i])
totalMass = sum([sum(i) for i in zip(*matrix)])

for i in range(length):
    print(matrix[i])

def check(position, i, u, firstInAsteroid):
    global asteroids, asteroidCount, totalMass

    if i < 0 or u < 0:
        return 0
    if position > 0:
        print("X:", u, "Y:", i, "Checking:", position, firstInAsteroid)
        matrix[i][u] = 0
        asteroids.append([i,u])
        if firstInAsteroid:
            asteroidCount += 1
    else:
        return 0


    try:
        check(matrix[i+1][u], i+1, u, False)
    except:
        pass
    try:
        check(matrix[i-1][u], i-1, u, False)
    except:
        pass
    try:
        check(matrix[i][u+1], i, u+1, False)
    except:
        pass
    try:
        check(matrix[i][u-1], i, u-1, False)
    except:
        pass
    return position


for i in range(length):
    for u in range(length):
        check(matrix[i][u], i, u, True)

#print("")
#y = 3
#x = 1
#
#print(matrix[y][x])
#print(matrix[y+1][x])
#print(matrix[y-1][x])
#print(matrix[y][x+1])
#print(matrix[y][x-1])

print("Average = ", totalMass//asteroidCount)