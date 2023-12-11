def parse_input(input_text):
    parsed_data = {}
    sections = input_text.split('\n')

    times = sections[0].strip().split(':')
    parsed_data['times'] = times[1].split()

    distance = sections[1].strip().split(':')
    parsed_data['distance'] = distance[1].split()

    return parsed_data


def parse_input2(input_text):
    parsed_data = {}
    sections = input_text.split('\n')

    times = sections[0].strip().split(':')
    parsed_data['times'] = int(times[1].replace(' ', ''))

    distance = sections[1].strip().split(':')
    parsed_data['distance'] = int(distance[1].replace(' ', ''))

    return parsed_data


def solve1(input):
    solution = 0

    for i in range(len(input['times'])):
        wins = 0
        time = int(input['times'][i])
        recordedDistance = int(input['distance'][i])
        for j in range(time):
            travelSpeed = j
            remainingTime = time - j
            travelDistance = travelSpeed * remainingTime
            if travelDistance > recordedDistance:
                wins += 1
        if solution == 0:
            solution = wins
        else:
            solution *= wins

    return solution


def solve2(input):
    solution = 0

    time = input['times']
    recordedDistance = input['distance']
    for j in range(time):
        travelSpeed = j
        remainingTime = time - j
        travelDistance = travelSpeed * remainingTime
        if travelDistance > recordedDistance:
            solution += 1

    return solution


with open('input.txt', 'r') as file:
    lines = file.read()

    input = parse_input(lines)
    solution = solve1(input)
    print(solution)

    input = parse_input2(lines)
    total = solve2(input)
    print(total)
