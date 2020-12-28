# Advent of Code - Day 10
# Part 1: find the product of the number of 1 jolt differences with number of 3 jolt differences in a
# chain of jolt adapters.

def sort_diff_and_prod(data):
    # check if zero is present, add if not
    if 0 not in data:
        data.append(0)
    data.sort()
    diff = []
    for i in range(len(data)-1):
        diff.append(data[i+1] - data[i])
    # add one to take into account final adapter in device
    return diff.count(1) * (diff.count(3) + 1)


print('#############################################')
adapters = []
count = 0
text_input = open("input.txt", "r")
for line in text_input:
    adapters.append(int(line.strip()))
text_input.close()
print('Loaded adapters data')
print(f'Product: {sort_diff_and_prod(adapters)}')
