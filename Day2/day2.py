redCubes = 12
greenCubes = 13
blueCubes = 14

total = 0
totalPower = 0

def parse_input(input_string):
    games = {}

    game_sections = [section.strip() for section in input_string if section.strip()]

    for section in game_sections:
        game_info = section.split(':')
        game_number = game_info[0].strip().replace('Game ', '')

        # Split the game info by ';'
        game_data = game_info[1].split(';')
        game_data = [data.strip() for data in game_data if data.strip()]

        games[game_number] = []

        # Split individual counts of colors and store in a list
        for data in game_data:
            colors = data.split(',')
            color_count = {}
            for color in colors:
                count, color_name = color.strip().split()
                color_count[color_name] = int(count)
            games[game_number].append(color_count)

    return games

def isPossible(game):
    currRedCubes = 0
    currBlueCubes = 0
    currGreenCubes = 0

    for part in game:
        if part.get('blue', 0) > currBlueCubes:
            currBlueCubes = part['blue']
            if currBlueCubes > blueCubes:
                return False
        if part.get('red', 0) > currRedCubes:
            currRedCubes = part['red']
            if currRedCubes > redCubes:
                return False
        if part.get('green', 0) > currGreenCubes:
            currGreenCubes = part['green']
            if currGreenCubes > greenCubes:
                return False

    return True


def power(game):
    currRedCubes = 1
    currBlueCubes = 1
    currGreenCubes = 1

    for part in game:
        if part.get('blue', 0) > currBlueCubes:
            currBlueCubes = part['blue']
        if part.get('red', 0) > currRedCubes:
            currRedCubes = part['red']
        if part.get('green', 0) > currGreenCubes:
            currGreenCubes = part['green']

    return currGreenCubes * currBlueCubes * currRedCubes

with open('input.txt', 'r') as file:
    lines = file.readlines()
    games = parse_input(lines)
    for key, value in games.items():
        if isPossible(value):
            total += int(key)
        totalPower += power(value)

    print(total)
    print(totalPower)