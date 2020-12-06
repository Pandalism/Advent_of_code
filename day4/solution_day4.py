# Advent of Code - Day 4
#
# Part 1: given a list of passport key:value pairs, with each passport seperated by an empty row, find the number of
#   valid passports. A valid passport is one with byr, iyr, eyr, hgt, hcl, ecl, and pid keys

# declare functions
def passport_clean(passports):
    output = []
    start_idx = 0
    for idx, partial in enumerate(passports):
        if partial == '':
            output.append(' '.join(passports[start_idx:idx]))
            start_idx = idx + 1
    return output


def convert_to_dict(line):
    out_dict = dict()
    for pair in line.split():
        out_dict[pair.split(':')[0]] = pair.split(':')[1]
    return out_dict


# set req_keys
req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'pid']

#  load passports
print('#############################################')
passports = []
text_input = open("day4/input.txt", "r")
for i in text_input:
    passports.append(i.strip())
text_input.close()
print('Loaded passports')

# clean passports
passports = passport_clean(passports)
passport_dicts = []
for passport in passports:
    passport_dicts.append(convert_to_dict(passport))







