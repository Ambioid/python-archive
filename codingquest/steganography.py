import binascii
from PIL import Image

img = Image.open("inputPic.png")
imgWidth = 15

red = list(img.getchannel('R').getdata())
#print(red)

for i in range(len(red)):
    red[i] = bin(red[i])


#print(red)
binMsg = ''
for i in range(len(red)):
    #print(i, binMsg)
    #if (i % 8) == 0:
    #    binMsg += " "
    binMsg += str(red[i][-1])

binascii.unhexlify('%x' % int(binMsg))
print(binMsg)