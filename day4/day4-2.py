"""

"""

f = open("../inputs/day4", "r")

passports = []
pasp = {}

for line in f:
    if line == "\n":
        passports.append(pasp)
        pasp = {}
    keys_values = line.split("\n")[0].split()
    for key_value in keys_values:
        key, value = key_value.split(":")
        pasp[key] = value

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

count = 0
for pasp in passports:
    if all(key in pasp for key in required_fields):
        conds = []
        conds.append(int(pasp["byr"]) in range(1920, 2002+1) and int(pasp["iyr"]) in range(2010, 2020+1) and \
                int(pasp["eyr"]) in range(2020, 2030+1))
        conds.append( ("cm" in pasp["hgt"] and int(pasp["hgt"].split("cm")[0]) in range(150, 193 + 1)) or \
                ("in" in pasp["hgt"] and int(pasp["hgt"].split("in")[0]) in range(59, 76 + 1)))
        conds.append(pasp["hcl"][0] == "#" and all(i.isalpha() or i.isdigit() for i in pasp["hcl"].split("#")[1]))
        conds.append(pasp["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))
        conds.append(len(pasp["pid"]) == 9 and all(i.isdigit for i in pasp["pid"]))

        if all(x for x in conds):
            count += 1

print(count)