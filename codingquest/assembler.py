data = open("file.txt", "r").read().split("\n")

vari = {"A": 0, "B": 0, "C": 0, "D": 0, 'E': 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0}

i = 0
check = False
while i < len(data):
    split = data[i].split(" ")

    if split[0] == "END":
        print("End")
        quit()

    in1 = split[1]
    print(f'\n{i + 1}: {data[i]}, ', end="")

    try:
        in2 = split[2]
        if type(in2) == str:
            in2 = vari[in2]
    except:
        pass

    in2 = int(in2)

    if split[0] == "ADD":
        print(f'Adding ({vari[in1]} + {in2}) -> ', end="")
        vari[in1] += in2
        print(vari[in1], end="")
    elif split[0] == "MOD":
        vari[in1] = vari[in1] % in2
        print(vari[in1], end="")
    elif split[0] == "DIV":
        vari[in1] = vari[in1] // in2
        print(vari[in1], end="")
    elif split[0] == "MOV":
        vari[in1] = in2
        print(vari[in1], end="")
    elif split[0] == "CEQ":
        check = vari[in1] == in2
        print(f'Equal Check of {in1}, ({vari[in1]} == {in2}) -> {check}')

    elif split[0] == "CGE":
        check = int(vari[in1]) >= int(in2)
        print(f'Greater or Equal Check of {in1}, ({vari[in1]} >= {in2}) -> {check}')
    elif split[0] == "OUT":
        print("Final Output: ", vari[in1])

    if split[0] == "JMP":
        print(f'Jumping {i + 1} -> {i + 1 + int(in1)}', end="")
        i += int(in1)

    elif split[0] == "JIF":
        print("Jump ", i + 1, in1, check, "\n")
        if check:
            print(f'Jumping {i + 1} -> {i + 1 + int(in1)}', end="")
            i += int(in1)
        else:
            i += 1
    else:
        i += 1
