stringInput = input("Input string to encrypt please!\n")
offset = int(input("input how many letters to shift the message \n"))
finishedMessage = ""

for i in range(len(stringInput)):
    if stringInput[i].isalpha():
        finishedMessage += (chr(ord(stringInput[i]) + offset))

        while ord(finishedMessage[i]) < 65 or ((ord(finishedMessage[i])) < 97 and ord(stringInput[i]) > 96): #If too far left
            finishedMessage = finishedMessage[:i] + (chr(ord(finishedMessage[i])+26))

        while ord(finishedMessage[i]) > 122 or ((ord(finishedMessage[i])) > 90 and ord(stringInput[i]) < 91):  # If too far right
            finishedMessage = finishedMessage[:i] + (chr(ord(finishedMessage[i]) - 26))
    else:
        finishedMessage += stringInput[i]
print(finishedMessage)

