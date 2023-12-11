card_strength = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
                 '2': 2}
card_strength_p2 = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
                    '2': 2, 'J': 1}


def parse_input(input_text):
    parsed_data = []
    sections = input_text.split('\n')

    for section in sections:
        parsed_data.append(section.strip().split())

    return parsed_data


def twoOccurence(hand):
    for c in hand:
        if hand[c] == 4:
            return True
    return False


def threeOccurence(hand):
    for c in hand:
        if hand[c] == 3:
            return True
    return False


def sort_cards_by_strength(cards):
    def get_card_value(card):
        return (
        card_strength[card[0][0]], card_strength[card[0][1]], card_strength[card[0][2]], card_strength[card[0][3]],
        card_strength[card[0][4]])

    cards.sort(key=get_card_value, reverse=False)
    return cards


def solve1(input):
    solution = 0

    fiveOfAKind = []
    fourOfAKind = []
    fullHouse = []
    threeOfAKind = []
    twoPair = []
    onePair = []
    highCard = []

    for hand in input:
        b = dict.fromkeys(hand[0], 0)
        for i in hand[0]:
            b[i] += 1
        if len(b) == 1:
            fiveOfAKind.append(hand)
        elif len(b) == 2:
            if twoOccurence(b):
                fourOfAKind.append(hand)
            else:
                fullHouse.append(hand)
        elif len(b) == 3:
            if threeOccurence(b):
                threeOfAKind.append(hand)
            else:
                twoPair.append(hand)
        elif len(b) == 4:
            onePair.append(hand)
        else:
            highCard.append(hand)

    highCard = sort_cards_by_strength(highCard)
    onePair = sort_cards_by_strength(onePair)
    twoPair = sort_cards_by_strength(twoPair)
    threeOfAKind = sort_cards_by_strength(threeOfAKind)
    fullHouse = sort_cards_by_strength(fullHouse)
    fourOfAKind = sort_cards_by_strength(fourOfAKind)
    fiveOfAKind = sort_cards_by_strength(fiveOfAKind)

    cards = [*highCard, *onePair, *twoPair, *threeOfAKind, *fullHouse, *fourOfAKind, *fiveOfAKind]

    multiplier = 1
    for card in cards:
        solution += int(card[1]) * multiplier
        multiplier += 1

    return solution


def twoOccurenceP2(hand):
    check = 0
    for c in hand:
        if hand[c] == 2:
            check += 1
        elif c == 'J' and hand['J'] > 0:
            check += 1

    if check == 2:
        return True  # Two pair
    return False


def threeOccurenceP2(hand):
    check = 0
    for c in hand:
        if hand[c] == 2 or hand[c] == 3:
            check += 1
    if check == 2:
        return False
    return True


def sort_cards_by_strength_p2(cards):
    def get_card_value(card):
        return (card_strength_p2[card[0][0]], card_strength_p2[card[0][1]], card_strength_p2[card[0][2]],
                card_strength_p2[card[0][3]], card_strength_p2[card[0][4]])

    cards.sort(key=get_card_value, reverse=False)
    return cards


def solve2(input):
    solution = 0

    fiveOfAKind = []
    fourOfAKind = []
    fullHouse = []
    threeOfAKind = []
    twoPair = []
    onePair = []
    highCard = []

    for hand in input:
        b = dict.fromkeys(hand[0], 0)
        b['J'] = 0
        for i in hand[0]:
            b[i] += 1
        b = dict(sorted(b.items(), key=lambda item: item[1], reverse=True))
        for c in b:
            if c == 'J' and b[c] == 5:
                fiveOfAKind.append(hand)
                break
            elif c == 'J':
                continue
            occurence = b[c] + b['J']
            if occurence == 5:
                fiveOfAKind.append(hand)
                break
            elif occurence == 4:
                fourOfAKind.append(hand)
                break
            elif occurence == 3:
                if threeOccurenceP2(b):
                    threeOfAKind.append(hand)
                else:
                    fullHouse.append(hand)
                break
            elif occurence == 2:
                if twoOccurenceP2(b):
                    twoPair.append(hand)
                else:
                    onePair.append(hand)
                break
            else:
                highCard.append(hand)
                break

    highCard = sort_cards_by_strength_p2(highCard)
    onePair = sort_cards_by_strength_p2(onePair)
    twoPair = sort_cards_by_strength_p2(twoPair)
    threeOfAKind = sort_cards_by_strength_p2(threeOfAKind)
    fullHouse = sort_cards_by_strength_p2(fullHouse)
    fourOfAKind = sort_cards_by_strength_p2(fourOfAKind)
    fiveOfAKind = sort_cards_by_strength_p2(fiveOfAKind)

    cards = [*highCard, *onePair, *twoPair, *threeOfAKind, *fullHouse, *fourOfAKind, *fiveOfAKind]

    multiplier = 1
    for card in cards:
        solution += int(card[1]) * multiplier
        multiplier += 1

    return solution


with open('input.txt', 'r') as file:
    lines = file.read()

    input = parse_input(lines)
    solution = solve1(input)
    print(solution)

    total = solve2(input)
    print(total)
