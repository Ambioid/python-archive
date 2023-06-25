charSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"
key = "Roads? Where We're Going, We Don't Need Roads."
msg = "ftmpH.:lemGubTDmMb'YtfsublbnkKlMmOoKywmmOIpa.,3mNeEbl?(bVtkUy?xtoNtCkAg:;n)OlInqp2rjap6JwiG)9H'jHm: pjok'9njQbtOxusdql'b'VtkrBb5j!aMWGieIjOHfrw,j,ubsbm,xrufoKljGdob8q,APzqI:0fpi:.Jsipk6lueD):!wrwbd?j(LbmODCCz7:vjbANCsqp2ts);Of,?p; lulx,tXGbLmbTflKBbYlCCdle1bnYtGrCl1bnw:PrphBeYFviLoZD.7pb!)nrztr0lCvl8n'tqIHn8"
#print(charSet.find(key[0])+1+charSet.find(msg[0])+1)


i = 0
newMsg = ""
encoding = False

for x in range(len(msg)):
    if msg[x] in charSet:

        if i >= len(key):  # Wrap Around to front
            i -= len(key)
        if i < 0:  # Wrap Around to back
            i += len(key)
        print(i)

        newChar = charSet.find(msg[x])
        if encoding:
            newChar += charSet.find(key[i])+1
        else:
            newChar -= charSet.find(key[i])+1

        print(i, "Key:", key[i], charSet.find(key[i])+1)
        print(x, "Msg:", msg[x], charSet.find(msg[x])+1)
        while newChar >= len(charSet):
            newChar -= len(charSet)
        while newChar < 0:
            newChar += len(charSet)

        print(i, "Out:", charSet[newChar], newChar, "\n")
        newMsg += charSet[newChar]
        i += 1
        #print(finishedMsg)
    else:
        newMsg += msg[x]
        i += 1

print(newMsg)

