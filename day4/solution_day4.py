# Advent of Code - Day 4
#
# Part 1: given a list of passport key:value pairs, with each passport seperated by an empty row, find the number of
#   valid passports. A valid passport is one with byr, iyr, eyr, hgt, hcl, ecl, and pid keys

# imports
import re


# declare functions
def passport_clean(passports):
    output = []
    start_idx = 0
    for idx, partial in enumerate(passports):
        if partial == '':
            output.append(' '.join(passports[start_idx:idx]))
            start_idx = idx+1
    output.append(' '.join(passports[start_idx:]))
    return output


def convert_to_dict(line):
    out_dict = dict()
    for pair in line.split():
        out_dict[pair.split(':')[0]] = pair.split(':')[1]
    return out_dict


def check_if_keys_present(in_dict, req_keys):
    not_present = 0;
    for key in req_keys:
        not_present = not_present + (not key in in_dict)
    return not not_present


# set req_keys
req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

#  load passports
print('#############################################')
passports = []
text_input = open("input.txt", "r")
for i in text_input:
    passports.append(i.strip())
text_input.close()
print('Loaded passports')

# clean passports
passports = passport_clean(passports)
# iterate through
count_valid = 0
for passport in passports:
    # convert to dictionaries and check if all required keys are loaded in
    count_valid = count_valid + check_if_keys_present(convert_to_dict(passport), req_keys)

print(f'Valid passports: {count_valid}')

print('#############################################')


# now need to check that the actual components are valid:
# build validation functions:

def validate_byr(in_dict):
    return (int(in_dict['byr']) >= 1920) & (int(in_dict['byr']) <= 2002)


def validate_iyr(in_dict):
    return (int(in_dict['iyr']) >= 2010) & (int(in_dict['iyr']) <= 2020)


def validate_eyr(in_dict):
    return (int(in_dict['eyr']) >= 2020) & (int(in_dict['eyr']) <= 2030)


def validate_hgt(in_dict):
    temp = in_dict['hgt']
    if temp[-2:] == 'cm':
        if (int(temp.strip('cm')) >= 150) & (int(temp.strip('cm')) <= 193):
            return True
    elif temp[-2:] == 'in':
        if (int(temp.strip('in')) >= 59) & (int(temp.strip('in')) <= 76):
            return True
    else:
        return False


def validate_hcl(in_dict):
    pattern = re.compile('^#[0-9a-fA-F]{6}$')
    return bool(pattern.match(in_dict['hcl']))


def validate_ecl(in_dict):
    return in_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(in_dict):
    pattern = re.compile('^[0-9]{9}$')
    return bool(pattern.match(in_dict['pid']))


# find valid passports:
count_valid = 0
for passport in passports:
    # convert to dictionaries and check if all required keys are loaded in
    temp = convert_to_dict(passport)
    # check if all keys are present
    if check_if_keys_present(temp, req_keys):
        if validate_byr(temp) and \
                validate_iyr(temp) and \
                validate_eyr(temp) and \
                validate_hgt(temp) and \
                validate_hcl(temp) and \
                validate_ecl(temp) and \
                validate_pid(temp):
            count_valid = count_valid + 1

print(f'Valid passports (part 2): {count_valid}')

print('#############################################')
