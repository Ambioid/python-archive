data = open("Lottery.txt", "r").read().split()

winNums = [12, 48, 30, 95, 15, 55, 97]

print(data)
ticketLength = 6
winnings = 0

for y in range(int(len(data)/ticketLength)): #For every row
    rowMatches = 0
    for x in range(ticketLength):            #Check every part in row

        #for i in range(len(winNums)):
        #print(data[x+y*ticketLength])
        if int(data[x+y*ticketLength]) in winNums:
            rowMatches += 1
            print("True", data[x+y*ticketLength], rowMatches)

    if rowMatches == 6:
        winnings += 1000
    elif rowMatches == 5:
        winnings += 100
    elif rowMatches == 4:
        winnings += 10
    elif rowMatches == 3:
        winnings += 1


    #print("New Row")
print("Winnings:", winnings)
