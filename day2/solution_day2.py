# Advent of Code - Day 2
#
# Part 1: find number of passwords within text file that are valid
#   format is:
#       1-3 a: abcde
#       1-3 b: cdefg
#       2-9 c: ccccccccc
#   Where the password is after the colon and the password requirements are before.
#   The letter before the colon is required to be in the password a set amount of times, defined by the first
#   digit as a minimum and the second digit as a maximum.
#   On the first example, a must be present in the password (abcde) a minimum of 1 times and maximum of 3,
#   in this case it is valid.


# Load data as simple array
print('#############################################')
array = []
text_input = open("input.txt", "r")
for i in text_input:
    array.append(i)
text_input.close()
print('Loaded array')


def check_req(req, letter, pswrd):
    count = 0
    for i in pswrd:
        if i == letter:
            count = count + 1
    return ((int(req[0]) <= count) & (count <= int(req[1])))


def find_correct_pass(in_array):
    count = 0
    for line in in_array:
        req = line.split()[0].split('-')
        letter = line.split()[1][0]
        pswrd = line.split()[2]
        # print(f'Line: {line.strip()}, req: {req}, letter = {letter}, pswrd: {pswrd}')
        if check_req(req, letter, pswrd):
            # print(f'line: {line}')
            count = count + 1

    return (count)


print(f'Count of valid passwords (part 1 requirements): {find_correct_pass(array)}')

# Part 2: The password requirements are now
#   format is:
#       1-3 a: abcde
#       1-3 b: cdefg
#       2-9 c: ccccccccc
#   Where the password is after the colon and the password requirements are before.
#   The letter before the colon is required to be in the password in one of the two set positions, but not both,
#   as defined by the first digit and the second digit, using index of 1.
#   On the first example, a must be present in the password (abcde) in either the 1st or 3rd character,
#   in this case it is valid.

# tweak check_req
def check_req_part2(req, letter, pswrd):
    return (pswrd[int(req[0])-1] == letter) ^ (pswrd[int(req[1])-1] == letter)

# tweak find_correct_pass
def find_correct_pass_part2(in_array):
    count = 0
    for line in in_array:
        req = line.split()[0].split('-')
        letter = line.split()[1][0]
        pswrd = line.split()[2]
        # print(f'Line: {line.strip()}, req: {req}, letter = {letter}, pswrd_at_req: {pswrd[int(req[0])-1]}, pswrd_at_req2: {pswrd[int(req[1])-1]}')
        if check_req_part2(req, letter, pswrd):
            # print(f'line: {line}')
            count = count + 1

    return (count)


print(f'Count of valid passwords (part 2 requirements): {find_correct_pass_part2(array)}')
