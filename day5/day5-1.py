f = open("../inputs/day5", "r")
seats = []


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

for line in f:
    line = line.split("\n")[0]
    row = 128
    column = 8
    minim = 0
    maxim = 128
    min_row = 0
    max_row = 8
    #print(line)
    for c in range(1,8):
        middle = (maxim-minim) / 2
        if line[c-1] == "F":
            maxim = maxim - middle
        if line[c-1] == "B":
            minim = minim + middle
        #print(minim, maxim)
    for c in reversed(range(1,4)):
        middle_row = (max_row - min_row) / 2
        if line[-c] == "R":
            min_row = min_row + middle_row
        if line[-c] == "L":
            max_row = max_row - middle_row
    #print((maxim-1) * 8 + max_row - 1)
    seats.append((maxim-1) * 8 + max_row - 1)

seats_int = [int(x) for x in seats]
print(find_missing(sorted(seats_int)))



