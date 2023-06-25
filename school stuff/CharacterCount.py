'''
Write a Python program to perfom character frequency analysis on a passage of
text read in from a text document.

Read the file into a suitable data structure (string or list). 

Iterate through the data, counting the occurances of each alphabet character (in upper and lower case), punctuation characters and spaces.
Store the results into a suitable data structure
   either a 2D array a list of lists  counted = [ [ ], [ ], [ ] ] 
    or a Dictionary counted = {key1:Value,key2:value,key3:value}
Retrieve the stored analysis data and print to the screen
'''
def readData(Filename):
    file = open(Filename,"r")#"r" for read only
    print("File open for reading")
    data = file.read() # or use readlines()
    file.close()
    print("File closed")
    return data

def counter():
    characterCount = 0 #initialised
    #need to add your character counters here
    return characterCount

def fieldSize(data):
    count = 0
    for i in data:
        count +=8 #increment 8-bit ASCII counter
    return count

from collections import Counter

text = readData("HuffmanText.txt")

print(Counter(text))

all_freq = {}

for i in text:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1


#print(text)

#print(fieldSize(text),"Bits")





import os
print(os.path.getsize("HuffmanText.txt"),"Bytes")

