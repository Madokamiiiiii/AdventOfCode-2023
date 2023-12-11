

def parse_input(input_text):
    parsed_data = []
    lines = input_text.strip().split('\n')

    for line in lines:
        parsed_data.append([int(i) for i in line.strip().split()])

    return parsed_data


def extrapolateValue(line):
    newLine = []
    for i in range(len(line)):
        if i == (len(line) - 1):
            if all(number == 0 for number in newLine):
                return 0
            else:
                return newLine[-1] + extrapolateValue(newLine)
        newLine.append(line[i + 1] - line[i])


def extrapolateValueBackwards(line):
    newLine = []
    for i in range(len(line)):
        if i == (len(line) - 1):
            if all(number == 0 for number in newLine):
                return 0
            else:
                return newLine[0] - extrapolateValueBackwards(newLine)
        newLine.append(line[i + 1] - line[i])


def solve1(input):
    solution = 0
    for line in input:
        solution += line[-1] + extrapolateValue(line)
    return solution


def solve2(input):
    solution = 0
    for line in input:
        solution += line[0] - extrapolateValueBackwards(line)
    return solution


with open('input.txt', 'r') as file:
    lines = file.read()

    input = parse_input(lines)
    solution = solve1(input)
    print(solution)

    total = solve2(input)
    print(total)
