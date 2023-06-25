length = 6
matrix = [[0 for x in range(length)] for y in range(length)]
data = open("snakes.txt", "r").read()
listInfo = data.split()
diceRolls = data.splitlines()[length:]

for i in range(length):
    for u in range(length):
        if i % 2 == 1:  # If even
            matrix[(length-1) - i][u] = listInfo[u + length * i]
        else:
            matrix[(length-1) - i][u] = listInfo[((length-1) - u) + length * i]

pos1, pos2 = [1, 1], [1, 1]
moves = 0


def checkPos(player, pos):
    if player[1] >= length:
        print(pos, "Wins!", moves)
        return player
    print("Player", player, moves)
    while player[0] >= length:
        print("Minus")
        player[0] -= length
        # print(player,"\n")
        player[1] += 1
    while player[0] < 0:
        print("Plus")
        player[0] += length
        player[1] -= 1


def printMatrix():
    for i in range(length):
        print(i + 1, end='')
        if i == pos1[1] - 1 or i == pos2[1] - 1:  # If correct row
            print("[", end="")
            for u in range(length):
                if (pos1[0] - 1 == u and i == pos1[1] - 1) or (
                        pos2[0] - 1 == u and i == pos2[1] - 1):  # If correct spot
                    print("'X'", end=', ')
                else:
                    print("'", matrix[i][u], end="', ")
            print("]")
        else:
            print(matrix[i])
    print("")


def movePos(dist, player, pos):
    player[0] += dist
    checkPos(player, pos)
    print(player, dist, pos)
    player[0] += int(matrix[player[0]][player[1]])
    checkPos(player, pos)
    return player


for d in range(len(diceRolls)):
    print(diceRolls[d])
    moves += 1
    print(pos1, pos2)
    printMatrix()
    pos1 = movePos(int(diceRolls[d][0]), pos1, "Pos1")
    pos2 = movePos(int(diceRolls[d][2]), pos2, "Pos2")

    printMatrix()

    # print(matrix)
