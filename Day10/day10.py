
def parse_input(input_text):
    parsed_data = []
    lines = input_text.strip().split('\n')

    for line in lines:
        parsed_data.append(line)

    return parsed_data


def solve1(input):
    totalSteps = 0


    for lineNum, line in enumerate(input):
        for columnNum, character in enumerate(line):
            if character == 'S':
                startPos = (lineNum, columnNum, '')

    fromSouth = {'|': (-1, 0, 'north'), 'F': (-1, 1, 'east'), '7': (-1, -1, 'west'), 'S': (0 ,0 ,0)}
    fromNorth = {'|': (1, 0, 'south'), 'L': (1, 1, 'east'), 'J': (1, -1, 'west'), 'S': (0 ,0 ,0)}
    fromWest = {'-': (0, 1, 'east'), 'J': (-1, 1, 'north'), '7': (1, 1, 'south'), 'S': (0 ,0 ,0)}
    fromEast = {'-': (0, -1, 'west'), 'L': (-1, -1, 'north'), 'F': (1, -1, 'south'), 'S': (0 ,0 ,0)}


    loop = False
    pos = startPos

    # Look north
    if input[pos[0] - 1][pos[1]] in fromSouth.keys():
        totalSteps += 1
        pos = (pos[0] - 1, pos[1], fromSouth[input[pos[0] - 1][pos[1]]][2])

    # Look south
    elif input[pos[0] + 1][pos[1]] in fromNorth.keys():

        totalSteps += 1
        pos = (pos[0] + 1, pos[1],
               fromNorth[input[pos[0] + 1][pos[1]]][2])

    # Look west
    elif input[pos[0]][pos[1] - 1] in fromEast.keys():
        totalSteps += 1
        pos = (pos[0], pos[1] - 1,
               fromEast[input[pos[0]][pos[1] - 1]][2])

    # Look east
    else:
        totalSteps += 1
        pos = (pos[0], pos[1] + 1,
               fromWest[input[pos[0]][pos[1] + 1]][2])


    while not loop:
        # Look north
        if pos[2] == 'north':
            totalSteps += 1
            pos = (pos[0] - 1, pos[1], fromSouth[input[pos[0] - 1][pos[1]]][2])

        # Look south
        elif pos[2] == 'south':
            totalSteps += 1
            pos = (pos[0] + 1, pos[1],
                   fromNorth[input[pos[0] + 1][pos[1]]][2])

        # Look west
        elif pos[2] == 'west':
            totalSteps += 1
            pos = (pos[0], pos[1] - 1,
                   fromEast[input[pos[0]][pos[1] - 1]][2])
        # Look east
        if pos[2] == 'east':
            totalSteps += 1
            pos = (pos[0], pos[1] + 1,
                   fromWest[input[pos[0]][pos[1] + 1]][2])

        if input[pos[0]][pos[1]] == 'S':
            break

    return totalSteps / 2


def solve2(input):

    for lineNum, line in enumerate(input):
        for columnNum, character in enumerate(line):
            if character == 'S':
                startPos = (lineNum, columnNum, '')

    fromSouth = {'|': (-1, 0, 'north'), 'F': (-1, 1, 'east'), '7': (-1, -1, 'west'), 'S': (0 ,0 ,0)}
    fromNorth = {'|': (1, 0, 'south'), 'L': (1, 1, 'east'), 'J': (1, -1, 'west'), 'S': (0 ,0 ,0)}
    fromWest = {'-': (0, 1, 'east'), 'J': (-1, 1, 'north'), '7': (1, 1, 'south'), 'S': (0 ,0 ,0)}
    fromEast = {'-': (0, -1, 'west'), 'L': (-1, -1, 'north'), 'F': (1, -1, 'south'), 'S': (0 ,0 ,0)}


    loop = False
    pos = startPos

    lines = []

    # Look north
    if input[pos[0] - 1][pos[1]] in fromSouth.keys():
        pos = (pos[0] - 1, pos[1], fromSouth[input[pos[0] - 1][pos[1]]][2])

    # Look south
    elif input[pos[0] + 1][pos[1]] in fromNorth.keys():
        pos = (pos[0] + 1, pos[1],
               fromNorth[input[pos[0] + 1][pos[1]]][2])

    # Look west
    elif input[pos[0]][pos[1] - 1] in fromEast.keys():
        pos = (pos[0], pos[1] - 1,
               fromEast[input[pos[0]][pos[1] - 1]][2])

    # Look east
    else:
        pos = (pos[0], pos[1] + 1,
               fromWest[input[pos[0]][pos[1] + 1]][2])

    lines.append(pos)

    while not loop:
        # Look north
        if pos[2] == 'north':
            pos = (pos[0] - 1, pos[1], fromSouth[input[pos[0] - 1][pos[1]]][2])

        # Look south
        elif pos[2] == 'south':
            pos = (pos[0] + 1, pos[1],
                   fromNorth[input[pos[0] + 1][pos[1]]][2])

        # Look west
        elif pos[2] == 'west':
            pos = (pos[0], pos[1] - 1,
                   fromEast[input[pos[0]][pos[1] - 1]][2])
        # Look east
        elif pos[2] == 'east':
            pos = (pos[0], pos[1] + 1,
                   fromWest[input[pos[0]][pos[1] + 1]][2])

        lines.append(pos)

        if input[pos[0]][pos[1]] == 'S':
            break

    enclosed = 0
    borderLines = [(i[0], i[1]) for i in lines]
    borderLines = sorted(borderLines, key=lambda element: (element[0], element[1]))


    prevBorderColumn = -1
    currentLine = -1
    bordersInLine = 0

    # for lineNum, line in enumerate(input):
    #     for columnNum, character in enumerate(line):
    #         if (lineNum, columnNum) in borderLines:
    #             continue
    #
    #         bordersInLine = 0
    #         x = columnNum
    #
    #         while x < len(line):
    #             c = input[lineNum][x]
    #             if (lineNum, x) in borderLines and c in '|LJ':
    #                 bordersInLine += 1
    #             x += 1
    #
    #         if bordersInLine % 2 == 1:
    #             enclosed += 1


    for borderLine in borderLines:
        if currentLine != borderLine[0]:
            prevBorderColumn = -1
            bordersInLine = 0
            currentLine = borderLine[0]

        if bordersInLine % 2 == 1 and prevBorderColumn != -1:
            enclosed += borderLine[1] - prevBorderColumn - 1

        if input[borderLine[0]][borderLine[1]] in '|LJ':
            bordersInLine += 1
        prevBorderColumn = borderLine[1]

    return enclosed


with open('input.txt', 'r') as file:
    lines = file.read()

    input = parse_input(lines)
    solution = solve1(input)
    print(solution)

    total = solve2(input)
    print(total)
