# Advent of Code - Day 1
#
# Part 1: find two numbers which sum up to 2020

# Load data as simple array
print('#############################################')
array = []
text_input = open("input.txt", "r")
for i in text_input:
    array.append(int(i))
text_input.close()
print('Loaded array')

# ensure array is loaded
print(array[0:3])

# define multiplication function working on iteration
def multiply(in_iter):
    product = 1
    for i in in_iter:
        product = product * i
    return product

# define sum-finding function, in this case just looping through the array
def find_two_sums(in_array, sum_trgt):
    for i in in_array:
        for j in in_array:
            if i+j == sum_trgt:
                # note i==j can occur here, to eliminate use:
                # & (i != j)
                print(f'i: {i}, j: {j}')
                return ((i,j))
    return(None)

# apply function on array
print('Find two number sum for array')
two_nums = find_two_sums(array, 2020)

print(f'Product of numbers is : {multiply(two_nums)}')

print('#############################################')
# Part 2: find three numbers which sum up to 2020

# define sum-finding function, in this case just looping through the array
def find_three_sums(in_array, sum_trgt):
    for i in in_array:
        for j in in_array:
            for k in in_array:
                if i+j+k == sum_trgt:
                    # note i==j can occur here, to eliminate use:
                    # & (i != j & i != k & j != k)
                    print(f'i: {i}, j: {j}, k: {k}')
                    return ((i,j,k))
    return(None)

# apply function on array
print('Find three number sum for array')
three_nums = find_three_sums(array, 2020)

print(f'Product of numbers is : {multiply(three_nums)}')

print('#############################################')
