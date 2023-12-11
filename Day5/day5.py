# Parsing maps
map_names = [
    'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water',
    'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location'
]


def parse_input(input_text):
    parsed_data = {}
    sections = input_text.split('\n\n')

    # Parsing seeds
    seeds_section = sections[0].split(':')
    seed_values = list(map(int, seeds_section[1].strip().split()))
    parsed_data['seeds'] = seed_values

    for i, section in enumerate(sections[1:]):
        mapList = []
        lines = section.strip().split('\n')
        for line in lines[1:]:
            mapList.append([int(value) for value in line.strip().split()])
        parsed_data[map_names[i]] = mapList

    return parsed_data


def helper(mapList, previousNumber):
    for value in mapList:
        if previousNumber in range(value[1], value[1] + value[2]):
            return value[0] + previousNumber - value[1]
    return previousNumber


def solve1(inputMap):
    solution = 0

    for seed in inputMap['seeds']:
        previousNumber = seed
        for mapName in map_names:
            mapList = inputMap[mapName]
            previousNumber = helper(mapList, previousNumber)

        if solution == 0:
            solution = previousNumber
        elif previousNumber < solution:
            solution = previousNumber

    return solution


def solve2(inputMap):
    solution = 0

    seeds = []
    for i, seed in enumerate(inputMap['seeds']):
        if i % 2 == 0:
            newSeeds = range(seed, seed + inputMap['seeds'][i + 1])
            seeds.append(newSeeds)

    for seedSublist in seeds:

        for seed in seedSublist:
            previousNumber = seed
            for mapName in map_names:
                mapList = inputMap[mapName]
                previousNumber = helper(mapList, previousNumber)

            if solution == 0:
                solution = previousNumber
            elif previousNumber < solution:
                print(previousNumber)
                solution = previousNumber

    return solution


with open('input.txt', 'r') as file:
    lines = file.read()

    maps = parse_input(lines)
    solution = solve1(maps)
    print(solution)

    total = solve2(maps)
    print(total)
