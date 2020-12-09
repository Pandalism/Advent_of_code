# Advent of Code - Day 6
# Part 1: given a list of a group of filled out answers, find the sum of

# def functions
def group_customs(customs):
    output = []
    start_idx = 0
    for idx, partial in enumerate(customs):
        if partial == '':
            output.append(' '.join(customs[start_idx:idx]))
            start_idx = idx+1
    output.append(' '.join(customs[start_idx:]))
    return output

def count_response_grouped(groups):
    out_sum = 0
    for group in groups:
        out_sum = out_sum + len(set(group.replace(' ','')))
    return out_sum


def count_response_grouped_part2(groups):
    out_sum = 0
    for group in groups:
        tmp_indiv = group.split()
        tmp_set = set(tmp_indiv[0])
        for i in range(len(tmp_indiv)-1):
            tmp_set.intersection_update(set(tmp_indiv[i+1]))
        out_sum = out_sum + len(tmp_set)
    return out_sum


print('#############################################')
customs = []
text_input = open("input.txt", "r")
for line in text_input:
    customs.append(line.strip())
text_input.close()
print('Loaded customs responses')

customs = group_customs(customs)
print('ordered customs responses into groups')

print(f'Sum of responses = {count_response_grouped(customs)}')

print(f'Sum of responses answered by all in a group = {count_response_grouped_part2(customs)}')