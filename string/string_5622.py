# ------------------------------------------------------------------------------------ 5622 번
Phone = input()
P = list(Phone.upper())
tim = 0
for i in range(len(P)):
    if P[i] == "A" or P[i] == "B" or P[i] == "C":
        tim += 3
    elif P[i] == "F" or P[i] == "D" or P[i] == "E":
        tim += 4
    elif P[i] == "I" or P[i] == "G" or P[i] == "H":
        tim += 5
    elif P[i] == "J" or P[i] == "K" or P[i] == "L":
        tim += 6
    elif P[i] == "O" or P[i] == "N" or P[i] == "M":
        tim += 7
    elif P[i] == "P" or P[i] == "Q" or P[i] == "R" or P[i] == "S":
        tim += 8
    elif P[i] == "U" or P[i] == "T" or P[i] == "V":
        tim += 9
    elif P[i] == "Y" or P[i] == "X" or P[i] == "W" or P[i] == "Z":
        tim += 10
print(tim)