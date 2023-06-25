import hashlib

data = open("blockchain.txt", "r").read().split("\n")
print(data)

split = data[0].split("|")
data[0] = f'{split[0]}|{split[1]}|{split[2]}'

for i in range(len(data)):
    split = data[i].split("|")

    key = f'{split[0]}|{split[1]}|{split[2]}'
    hash = hashlib.sha256(key.encode('ascii')).hexdigest() #Hash first 3 parts together

    print(key)
    u = 0
    while (hash[:6]) != '000000': #Keep iterating through until hash is right
        u += 1
        hash = hashlib.sha256(f'{split[0]}|{u}|{split[2]}'.encode('ascii')).hexdigest()


    data[i] = f'{split[0]}||{u}|{split[2]}|{hash}' #Put Finished Hash on the end
    print(data[i])
    print(i, len(data))
    if i < len(data)-1:
        split = data[i+1].split("|")
        data[i+1] = f'{split[0]}|{split[1]}|{hash}' #Put hash on prevous hash of next entry

for i in range(len(data)):
    print(data[i])