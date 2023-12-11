
def parse_input(input_text):

    parsed_data = []
    lines = input_text.strip().split('\n')

    for line in lines:
        parsed_data.append(line)
        if all(ch == '.' for ch in line):
            parsed_data.append(line)

    parsed_data = double_columns_with_only_dots(parsed_data)
    return parsed_data


def double_columns_with_only_dots(arr):
    rows = len(arr)
    cols = len(arr[0])

    col = 0
    while col < cols:
        col_values = [arr[row][col] for row in range(rows)]

        if all(value == '.' for value in col_values):
            for row in range(rows):
                arr[row] = arr[row][:col] + '.' + arr[row][col:]
            col += 2
        else:
            col += 1
        cols = len(arr[0])

    return arr


def parse_input2(input_text):

    parsed_data = []
    lines = input_text.strip().split('\n')

    rowExpand = []

    for y, line in enumerate(lines):
        parsed_data.append(line)
        if all(ch == '.' for ch in line):
            rowExpand.append(y)

    colExpand = double_columns_with_only_dots2(parsed_data)
    return parsed_data, rowExpand, colExpand


def double_columns_with_only_dots2(arr):
    rows = len(arr)
    cols = len(arr[0])

    colExpand = []

    col = 0
    while col < cols:
        col_values = [arr[row][col] for row in range(rows)]

        if all(value == '.' for value in col_values):
            colExpand.append(col)

        col += 1

    return colExpand

def findShortestPath(fromGalaxy, galaxies):
    shortest = 0

    for galaxy in galaxies:
        deltaY = abs(galaxy[0] - fromGalaxy[0])
        deltaX = abs(galaxy[1] - fromGalaxy[1])
        total = deltaX + deltaY
        #if total != 0:
        #    if shortest == -1 or total < shortest:
        #        shortest = total
        shortest += total
    return shortest

def findShortestPath2(fromGalaxy, galaxies, rowExpand, colExpand):
    shortest = 0

    for galaxy in galaxies:
        deltaY = abs(galaxy[0] - fromGalaxy[0])
        deltaX = abs(galaxy[1] - fromGalaxy[1])

        for rows in range(min(galaxy[0], fromGalaxy[0]), max(fromGalaxy[0], galaxy[0])):
            if rows in rowExpand:
                deltaY += 999999
        for cols in range(min(galaxy[1], fromGalaxy[1]), max(fromGalaxy[1], galaxy[1])):
            if cols in colExpand:
                deltaX += 999999
        total = deltaX + deltaY

        shortest += total
    return shortest

def solve1(input):
    totalSteps = 0

    galaxies = []
    for y, line in enumerate(input):
        for x, character in enumerate(line):
            if character == '#':
                galaxies.append((y, x))

    for galaxy in galaxies:
        totalSteps += findShortestPath(galaxy, galaxies)

    return totalSteps / 2


def solve2(input, rowExpand, colExpand):
    totalSteps = 0

    galaxies = []
    for y, line in enumerate(input):
        for x, character in enumerate(line):
            if character == '#':
                galaxies.append((y, x))

    for galaxy in galaxies:
        totalSteps += findShortestPath2(galaxy, galaxies, rowExpand, colExpand)

    return totalSteps // 2

with open('input.txt', 'r') as file:
    input_text = file.read()

    input = parse_input(input_text)
    solution = solve1(input)
    print(solution)

    input, rowExpand, colExpand = parse_input2(input_text)
    total = solve2(input, rowExpand, colExpand)
    print(total)

