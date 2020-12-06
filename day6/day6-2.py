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
file_content = f.read()
groups = file_content.split("\n\n")


def common(lines):
    str1 = lines[0]
    dict1 = Counter(str1)
    common_dict = dict1
    for i in lines[1:]:
        dict2 = Counter(i)
        common_dict = common_dict & dict2

    common_ch = list(common_dict.elements())
    return len(common_ch)


total = 0
for group in groups:
    lines = group.split("\n")
    total += common(lines)

print(total)
