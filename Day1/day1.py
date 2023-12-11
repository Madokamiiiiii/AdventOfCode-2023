import re

total = 0

numberWordMap = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def takeIndex(elem):
    return elem[0]


with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        firstNum = [-1, 0]
        lastNum = [-1, 0]

        numberWordsIndex = [[i.start(), numberWordMap[numberWord]] for numberWord in numberWordMap.keys() for i in
                            re.finditer(numberWord, line)]
        if len(numberWordsIndex) > 0:
            numberWordsIndex.sort(key=takeIndex)
            firstNum = numberWordsIndex[0]
            lastNum = numberWordsIndex[-1]
        for i, character in enumerate(line):
            try:
                number = int(character)

                if i < firstNum[0] or firstNum[0] == -1:
                    firstNum = [i, number]
                if i > lastNum[0] or lastNum[0] == -1:
                    lastNum = [i, number]
            except:
                pass

        if lastNum == 0:
            lastNum = firstNum

        lineTotal = firstNum[1] * 10 + lastNum[1]
        print(lineTotal)
        total += lineTotal

print(total)
