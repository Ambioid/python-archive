data = (open("Connect4.txt", "r").read()).split("\n")

matrix = [[0 for x in range(7)] for y in range(7)]
playerNum = 0
playerWins = {1: 0, 2: 0, 3: 0, 0: 0}



def printMatrix():
    for i in range(7):
        print(matrix[i])


def checkboard(board):
    # check if there is a winner
    # check rows
    for i in range(7):
        for j in range(4):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]:
                if board[i][j] != 0:
                    return board[i][j]
    # check columns
    for i in range(4):
        for j in range(7):
            if board[i][j] == board[i + 1][j] == board[i + 2][j] == board[i + 3][j]:
                if board[i][j] != 0:
                    return board[i][j]
    # check diagonals
    for i in range(4):
        for j in range(4):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]:
                if board[i][j] != 0:
                    return board[i][j]
    for i in range(4):
        for j in range(3, 7):
            if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3]:
                # make sure it isnt 0
                if board[i][j] != 0:
                    return board[i][j]
    return 0


printMatrix()
for y in range(len(data)):  # Repeat once for every line
    #y = 3
    check = 0
    for i in range(len(data[0])):  # Run through moves of game
        if playerNum < 3:
            playerNum += 1  # Once for every player from 1 to 3
        else:
            playerNum = 1

        u = 0
        while matrix[int(data[y][i]) - 1][u] != 0:  # If space filled, moves up one
            u += 1


        matrix[int(data[y][i]) - 1][u] = playerNum

        check = checkboard(matrix)
        if check:
            break
            print("Break")

    playerWins[check] += 1
    print("\nGame:", y,"Win:", check, "Total:", playerWins)
    printMatrix()
    matrix = [[0 for x in range(7)] for y in range(7)]
    playerNum = 0
print("\nFinished")
print(playerWins)

print("Total: ", playerWins[1] * playerWins[2] * playerWins[3])
