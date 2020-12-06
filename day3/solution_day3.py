# Advent of Code - Day 3
#
# Part 1: given a arboreal map consisting of spaces (.) and trees (#). Count the trees encountered when navigating from
#   the top left point of the map down to the bottom, using a slope of right 3, down 1. The tree map repeats laterally.
#   ..##.......
#   #...#...#..
#   .#....#..#.
#   ..#.#...#.#
#   .#...##..#.
#   ..#.##.....
#   .#.#.#....#
#   .#........#
#   #.##...#...
#   #...##....#
#   .#..#...#.#


# Load data as simple array, stripping return carriage away
print('#############################################')
tree_map = []
text_input = open("input.txt", "r")
for i in text_input:
    tree_map.append(i.strip())
text_input.close()
print('Loaded tree_map')

print('Part 1:')
# make function to find tree even when it goes out of the array bounds laterally (using modulus)
def find_tree(tree_map, xpos, ypos):
    temp_array = tree_map[ypos]
    temp_x = xpos % len(temp_array)
    return temp_array[temp_x] == '#'  # check if its a '#' tree


def tobogan_down(tree_map, xslope, yslope):
    trees_encountered = 0
    xpos = 0
    ypos = 0
    while ypos < (len(tree_map)-1):
        xpos = xpos + xslope
        ypos = ypos + yslope
        if find_tree(tree_map, xpos, ypos):
            trees_encountered = trees_encountered + 1
    return trees_encountered


print(f'trees encountered: {tobogan_down(tree_map, 3, 1)}')

# Part 2: find the amount of trees encountered using a range of slops and multiply them together

print('Part 2:')
# define multiply
def multiply(in_iter):
    product = 1
    for i in in_iter:
        product = product * i
    return product

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees_encountered = []
for slope in slopes:
    trees_encountered.append(tobogan_down(tree_map, slope[0], slope[1]))

print(f'product of trees encountered: {multiply(trees_encountered)}')