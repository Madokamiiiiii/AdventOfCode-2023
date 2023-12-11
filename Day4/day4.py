def parse_input(input_text):
    cards = []

    for card_entry in input_text:
        card_info = {}
        card_entry = card_entry.strip()
        card_number, numbers = card_entry.strip().split(":")

        numbers = numbers.split("|")
        numbers = [num.strip().split() for num in numbers]

        card_info['Winning'] = list(map(int, numbers[0]))
        card_info['Normal'] = list(map(int, numbers[1]))
        card_info['Index'] = card_number.split('Card')[1].strip()

        cards.append(card_info)

    return cards


def solve1(cards):
    total = 0
    for card in cards:
        winningNumbers = len(set(card['Winning']).intersection(set(card['Normal'])))
        if winningNumbers == 1:
            total += 1
            continue
        elif winningNumbers > 1:
            total += pow(2, winningNumbers - 1)
            continue
        else:
            continue

    return total


def getCards(intermediateCards, copyOfCards, cards):
    winningNumbers = len(set(cards[i]['Winning']).intersection(set(cards[i]['Normal'])))
    for i in range(int(cards[i]['Index']) + 1, int(cards[i]['Index']) + 1 + winningNumbers):
        if i < max:
            intermediateCards.append(copyOfCards[i])
            return intermediateCards


def solve2(cards):
    numCards = {}
    total = 0
    max = len(cards)

    for i in range(max):
        numCards[i] = 1

    for i in range(max):
        for k in range(numCards[i]):
            winningNumbers = len(set(cards[i]['Winning']).intersection(set(cards[i]['Normal'])))
            if winningNumbers == 0:
                continue
            for j in range(int(cards[i]['Index']), int(cards[i]['Index']) + winningNumbers):
                if j <= max:
                    numCards[j] += 1
        total += numCards[i]
    return total


with open('input.txt', 'r') as file:
    lines = file.readlines()

    cards = parse_input(lines)
    total = solve1(cards)
    print(total)

    total = solve2(cards)
    print(total)
