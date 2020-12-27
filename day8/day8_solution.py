# Advent of Code - Day 8
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
    # if alternative:
    #     print(f'alternative found {alternative}')
    if pointer in history:
        print(f'hit infinite loop on instruction {pointer}:{instructions[pointer]}')
        print(f'accumulator: {accumulator}')
        return accumulator
    else:
        history.append(pointer)
        return run_program(instructions, pointer, history, accumulator)


def run_program_exhaustive(instructions, pointer, history, accumulator, branch=None):
    # note current pointer
    history.append(pointer)
    # interpret next instruction
    [pointer, accumulator, alternative] = read_instruction_debug(instructions, pointer, accumulator)

    # check if win scenario:
    if pointer >= len(instructions):
        print(f'found successful branch.')
        print(f'current pointer: {pointer}, current accumulator: {accumulator}, current branch point: {branch}.')
        return [pointer, history, accumulator]

    # explore alternatives if possible:
    if (alternative != None) & (branch == None):
        # check if branch point is and immediate win scenario
        if alternative >= len(instructions):
            print(f'found successful branch.')
            print(
                f'current pointer: {alternative}, current accumulator: {accumulator}, last instruction is branch point: {history[-1]}')
            return [pointer, history, accumulator]
        # else check if branch point can be continued:
        else:
            if not alternative in history:
                print(f'found valid alternative branch at {history[-1]}, exploring now...')
                temp_history = history.copy()
                temp = run_program_exhaustive(instructions, alternative, temp_history, accumulator, branch=temp_history[-1])
                # if successful!
                if temp:
                    return temp

    # if neither win nor branch possible, check for lose scenario
    if pointer in history:
        # print(f'hit infinite loop on instruction {history[-1]}:{instructions[history[-1]]}, branched at: {branch}')
        return None

    # if neither win, nor branch, nor lose, continue as down chain
    return run_program_exhaustive(instructions, pointer, history, accumulator, branch=branch)


print('#############################################')
instructions = []
count = 0
text_input = open("input.txt", "r")
for line in text_input:
    instructions.append(line.strip().split())
text_input.close()
print('Loaded instructions responses')

pointer = 0
history = []
accumulator = 0
run_program(instructions, pointer, history, accumulator)
print('##############################################')

pointer = 0
history = []
accumulator = 0
run_program_exhaustive(instructions, pointer, history, accumulator)