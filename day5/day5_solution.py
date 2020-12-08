# Advent of Code - Day 4
#
# Part 1: decode the positions and id of a seat based on the binary representation
#   For example, consider just the first seven characters of FBFBBFFRLR:
#   Start by considering the whole range, rows 0 through 127.
#       F means to take the lower half, keeping rows 0 through 63.
#       B means to take the upper half, keeping rows 32 through 63.
#       F means to take the lower half, keeping rows 32 through 47.
#       B means to take the upper half, keeping rows 40 through 47.
#       B keeps rows 44 through 47.
#       F keeps rows 44 through 45.
#   The final F keeps the lower of the two, row 44.
#   The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7).
#   The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.
#
#   For example, consider just the last 3 characters of FBFBBFFRLR:
#   Start by considering the whole range, columns 0 through 7.
#       R means to take the upper half, keeping columns 4 through 7.
#       L means to take the lower half, keeping columns 4 through 5.
#       The final R keeps the upper of the two, column 5.
#   So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# define imports
import numpy as np

# define table to input into translation function and map the output
in_trans = 'FBRL'
out_trans = '0110'
trantab = str.maketrans(in_trans, out_trans)

#  load passports and translate into binary and directly into seat_id
print('#############################################')
seat_ids = []
text_input = open("input.txt", "r")
for line in text_input:
    seat_ids.append(int(line.translate(trantab), base=2))
text_input.close()
print('Loaded passports')

# part 1: find highest seat_id
print(f'Highest seat_id = {max(seat_ids)}')

# part 2: find the gap in the seat_ids, in which your seat is (many assumptions here!)
# make array of seats all sorted:
npseat_id = np.array(sorted(seat_ids))

# find differential with itself offset by one, and find the highest difference
idx_of_gap = np.argmax(npseat_id[1:] - npseat_id[:-1])

seat_in_gap = npseat_id[idx_of_gap] + 1

print(f'The only seat not taken is: {seat_in_gap}')