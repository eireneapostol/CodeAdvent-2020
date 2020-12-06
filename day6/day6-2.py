"""
--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?


"""

from collections import Counter

f = open("../inputs/day6", "r")


def common(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    common_dict = dict1 & dict2
    common_ch = list(common_dict.elements())
    return ''.join(common_ch)


total = 0
next_line = f.readline()
common_chars = 0
common_str = common(next_line.split("\n")[0], next_line.split("\n")[0])
next_line = f.readline()

while next_line != "":
    if next_line == "\n":
        total += len(common_str)
        next_line = f.readline()
        if next_line != "":
            common_str = common(next_line, next_line)
        else:
            break
    else:
        next_line = next_line.split("\n")[0]
        common_str = common(common_str, next_line)
        next_line = f.readline()

total += len(common_str)
print(total)
