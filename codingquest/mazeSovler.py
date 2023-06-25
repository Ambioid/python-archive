data = open("maze.txt", "r").read().split("\n")

#print(data)

startPoint = data[0].find(" ")
endX = data[-1].find(" ")

lowest = 0
win = 0
checked = []


class check:
    def __init__(self, x, y, len):
        self.x = x
        self.y = y
        self.len = len


checking = [check(startPoint, 0, 1)]

while win == 0:

    x = checking[0].x
    y = checking[0].y

    if data[y][x] != "#":  # If its not wall or edge
        if y == len(data) - 1:  # Check if win
            win = checking[0].len
            print("Win", win)
            quit()

        elif [x, y] not in checked:
            #print("Checked: ", checked)
            if y > lowest:
                #print("Lowest:", y, "X:", x, "Y:", y, checking[0].len)
                lowest = y
            checked += [[x, y]]
            #print("Checking List:", checking)
            print("X:", x, "Y:", y, "Length:", checking[0].len)

            checking.append(check(x + 1, y, checking[0].len+1))
            checking.append(check(x - 1, y, checking[0].len+1))
            checking.append(check(x, y + 1, checking[0].len+1))
            checking.append(check(x, y - 1, checking[0].len+1))

    checking.pop(0)

print(endX)
if win == 0:
    print("Failed")
else:
    print("Win!", win)
