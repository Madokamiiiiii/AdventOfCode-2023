from math import lcm


def parse_input(input_text):
    parsed_data = {}
    lines = input_text.strip().split('\n')

    for line in lines:
        if '=' in line:
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()[1:-1].split(', ')
            parsed_data[key] = value
        elif len(line) > 1:
            parsed_data['Instr'] = line.strip()

    return parsed_data


def loop(input, pos, steps):
    for instruction in input['Instr']:
        if instruction == 'R':
            pos = input[pos][1]
            steps += 1
        if instruction == 'L':
            pos = input[pos][0]
            steps += 1

        if pos == 'ZZZ':
            return True, pos, steps
    return False, pos, steps


def loop2(input, pos, steps, skip):
    skip2 = 0
    for instruction in input['Instr']:
        if skip != 0:
            skip -= 1
            continue
        if instruction == 'R':
            pos = input[pos][1]
            steps += 1
        if instruction == 'L':
            pos = input[pos][0]
            steps += 1
        skip2 += 1
        if pos.endswith('Z'):
            if len(input['Instr']) != skip2:
                return True, pos, steps, skip2
            return True, pos, steps, 0
    return False, pos, steps, 0


def solve1(input):
    steps = 0
    pos = 'AAA'

    while True:
        end, pos, steps = loop(input, pos, steps)
        if end:
            break

    return steps


def solve2(input):
    steps = 0
    starts = {}

    ends = {}
    zfound = {}

    for pos in input:
        if pos.endswith('A'):
            starts[pos] = pos
            zfound[pos] = 0
        if pos.endswith('Z'):
            ends[pos] = pos

    while True:
        for step in input['Instr']:
            steps += 1
            for pos in starts:
                if step == 'R':
                    starts[pos] = input[starts[pos]][1]
                else:
                    starts[pos] = input[starts[pos]][0]
                if starts[pos].endswith('Z') and zfound[pos] == 0:
                    zfound[pos] = steps

            if all([pos != 0 for pos in zfound.values()]):
                return lcm(*zfound.values())

    return steps


with open('input.txt', 'r') as file:
    lines = file.read()

    input = parse_input(lines)
    solution = solve1(input)
    print(solution)

    total = solve2(input)
    print(total)
