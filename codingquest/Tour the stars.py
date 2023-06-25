data = open("starTour.txt", "r").read().split()

print(data)
totDist = 0

for y in range(int(len(data)/3)-1): #For every row
    rowRaw = 0
    for x in range(3):            #Check every part in row

        rowRaw += (int(data[x+(y)*3])- int(data[x+(y+1)*3]))**2

        print(x+1, data[x+y*3])
        #print("Raw: ", x, rowRaw)
    totDist += int(rowRaw**0.5)
    print("Newline: ", int(rowRaw**0.5))



    #print("New Row")
print("Total Distance:", totDist)
