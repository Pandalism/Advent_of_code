# Advent of Code - Day 9
# Part 1: find which number is NOT a sum of two numbers in the previous 25 datapoints
# Part 2: find the contiguous set of numbers which add up the previously found invalid datapoint

def find_if_valid(data, number):
    temp_diff = [number - point for point in data]
    valid = False
    for idx, point in enumerate(temp_diff):
        if (point in data) and (data[idx] != point):
            valid = True
    return valid


def search_not_valid(data, preamble_len):
    for i in range(preamble_len, len(data)):
        if not find_if_valid(data[i-preamble_len:i], data[i]):
            print(f'Found invalid datapoint {data[i]} at {i}')
            break
    return i, data[i]


def find_contingous(data, trgt_sum):
    start_idx = 0
    end_idx = 0
    curr_sum = data[0]
    while curr_sum != trgt_sum:
        if end_idx > len(data):
            print('End of data reached, cumulative subarray not found')
            return None

        if curr_sum < trgt_sum:
            end_idx += 1
            curr_sum += data[end_idx]
        elif curr_sum > trgt_sum:
            curr_sum -= data[start_idx]
            start_idx += 1

    print(f'start: {start_idx}, end: {end_idx}, sum: {curr_sum}')
    return data[start_idx:end_idx+1]

def high_low_sum(array):
    return min(array) + max(array)

print('#############################################')
transmission = []
count = 0
text_input = open("input.txt", "r")
for line in text_input:
    transmission.append(int(line.strip()))
text_input.close()
print('Loaded transmission data')

part1 = search_not_valid(transmission, 25)

subarray = find_contingous(transmission[:part1[0]], part1[1])

print(f'Sum of high and low values in subarray: {high_low_sum(subarray)}')