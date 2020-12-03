"""
--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

f = open("../inputs/day3", "r")
line_nr = 0

puzzle = {}

for line in f:
    line_nr += 1
    puzzle[line_nr] = line.split("\n")[0]

width = len(puzzle[1])
total_lines = line_nr

multiplication = 1

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for slope in slopes:
    line_nr = slope[1] + 1
    pos = slope[0]
    count = 0
    while line_nr <= total_lines:
        if puzzle[line_nr][pos % width] == "#":
            count += 1
        line_nr += slope[1]
        pos += slope[0]
    print(count)
    multiplication *= count

print(multiplication)