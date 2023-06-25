import math
legoVol = 10*16*16 #mm
earthVol = (4/3)*math.pi*((6371*1000000)**3) #mm

legosInEarth = earthVol/legoVol
print(legosInEarth)

