"""
--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

f = open("../inputs/day1", "r")

sum1 = 2020
sum2 = 0
array = []
found = False

for line in f:
    array.append(int(line))

print(array)

for nr1 in array:
    sum2 = sum1 - nr1
    for nr2 in array:
        if sum2 - nr2 in array and nr2 != nr1:
            found = True
            break
    if found:
        break



print(nr1 * nr2 * (sum2 - nr2))