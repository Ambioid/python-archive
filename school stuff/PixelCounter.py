import imageRead as ir
num_of_black = 0

# https://www.kylepaulsen.com/stuff/NetpbmViewer/

fileName = "BoatPic.pbm"
#fileName = "A.pbm"

metaData = ir.read(fileName)
maxSize = metaData[0]
image = metaData[1]

for r in range(maxSize):
    print(str(image[r]))
    for i in range(len(image[r])):
        if image[r][i]:
            num_of_black += 1

# Pixel count code goes here

print("\nNumber of black pixels = ", num_of_black)
