# Advent of Code - Day 7
# Part 1: given a group of rule on how bags are contained within other bags, find which bags contain at least
#   one shiny gold bag.

# needed heavy help for this particularly regarding an elegant way of regex and using defaultdict to help build the p
#   parent-child dictionary

import re
from collections import defaultdict

print('#############################################')
# create defaultdictionary to avoid empty dict calls
parents = defaultdict(lambda: [])

# read in parent - children bag rules
text_input = open("input.txt", "r")
for line in text_input:
    parent = line.split(' bags contain ')[0]
    children = re.findall(r'\d+ ([\w ]+) bag', line)
    # r' ' - treat as raw string
    # \d - numbers
    # + - 1 or more of the preceding expression
    # ( ) - remembers the matched text, and only outputs what is inside the brackets - KEY PART
    # [ ] - matches any single character

    # build data dictionary
    for child in children:
        parents[child].append(parent)


def find_parents(bag, parents_input):
    temp_set = set(parents_input[bag])
    for parent_bag in parents_input[bag]:
        temp_set = temp_set.union(find_parents(parent_bag, parents_input))
    return temp_set
    # much more elegant way found after, using *() to unpack a list/set so it can be union'ed on the same level
    # return temp_set.union( *(find_parents(parent_bag, parents_input) for parent_bag in parents_input[bag]))


print(f'Sum of top level bags which can contain shiny gold {len(find_parents("shiny gold", parents))}')

# part two this time read the rules and build a table of the children, and count the total amount of bags required
# within a chosen bag
rules = defaultdict(lambda: [])
text_input = open("input.txt", "r")
for line in text_input:
    parent = line.split(' bags contain ')[0]
    children = re.findall(r'(\d+) ([\w ]+) bag', line)

    rules[parent] = children


def count_bags_in(bag, rule_set):
    temp = 0  # empty bags don't count since they are considered in the level above
    if rule_set[bag] == []:
        return 0
    for child in rule_set[bag]:
        # add current bags, + the bags within those multiplied by the number of bags
        temp = temp + int(child[0]) + (int(child[0]) * count_bags_in(child[1], rule_set))
    return temp


print(f'Sum of bags within shiny gold {count_bags_in("shiny gold", rules)}')
