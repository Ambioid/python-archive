
fileName = "BoatPic.pbm"
#fileName = "A.pbm"
def read(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
        image = []
        #Read meta data
        maxWidth = int(lines[1][0])*10 +int(lines[1][1].strip())
        maxHeight = int(lines[1][0])*10 +int(lines[1][1].strip())
        print("Meta data reports image resolution of ",maxWidth,"x",maxHeight,"\n")
        #Read image data
        for line in lines[2:]:
            t = list(map(int, line.strip().split()))
            image.append(t)
    return maxWidth,image
