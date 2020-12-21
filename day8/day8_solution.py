# Advent of Code - Day 7
# Part 1: find the accumulated variable in a set of instructions just as it enters an infinite loop


def read_instruction_debug(inst_list, prog_pointer, curr_accummulator):
    alt_pointer = prog_pointer
    if inst_list[prog_pointer][0] == 'acc':
        curr_accummulator += int(inst_list[prog_pointer][1])
        prog_pointer += 1
        alt_pointer = None
    elif inst_list[prog_pointer][0] == 'jmp':
        alt_pointer += 1
        prog_pointer += int(inst_list[prog_pointer][1])
    else:
        alt_pointer += int(inst_list[prog_pointer][1])
        prog_pointer += 1

    return [prog_pointer, curr_accummulator, alt_pointer]

def run_program(instructions, pointer, history, accumulator):
    [pointer, accumulator, alternative] = read_instruction_debug(instructions, pointer, accumulator)
    if alternative:
        print(f'alternative found {alternative}')
    if pointer in history:
        print(f'hit infinite loop on instruction {pointer}:{instructions[pointer]}')
        return accumulator
    else:
        history.append(pointer)
        return run_program(instructions, pointer, history, accumulator)


print('#############################################')
instructions = []
count = 0
text_input = open("day8/test.txt", "r")
for line in text_input:
    instructions.append(line.strip().split())
text_input.close()
print('Loaded instructions responses')

run_program(instructions, pointer, history, accumulator)