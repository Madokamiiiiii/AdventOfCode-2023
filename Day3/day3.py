import re
from functools import reduce

solutionRes = 0
solutionRes2 = 0

def includeNumber(lines, index, lineNum):
    if lineNum < 0 or index < 0:
        return False
    try:
        if not lines[lineNum][index].isdigit() and not lines[lineNum][index] == "." and not lines[lineNum][index] == "\n":
            return True
        else:
            return False
    except:
        return False

def isNumber(lines, index, lineNum):
    if lineNum < 0 or index < 0:
        return False
    try:
        if lines[lineNum][index].isdigit():
            return True
        else:
            return False
    except:
        return False

def check(lines, number, lineNum, solution):
    for i in range(number[0]-1, number[1] + 1):
        if includeNumber(lines, i, lineNum - 1):
            solution += int(lines[lineNum][number[0]:number[1]])
            return solution
        if includeNumber(lines, i, lineNum):
            solution += int(lines[lineNum][number[0]:number[1]])
            return solution
        if includeNumber(lines, i, lineNum + 1):
            solution += int(lines[lineNum][number[0]:number[1]])
            return solution
    return solution

def check2(lines, number, lineNum, solution):
    found = []

    nextLine = [(m.start(0), m.end(0)) for m in re.finditer("\d+", lines[lineNum + 1])]
    prevLine = [(m.start(0), m.end(0)) for m in re.finditer("\d+", lines[lineNum - 1])]
    currLine = [(m.start(0), m.end(0)) for m in re.finditer("\d+", lines[lineNum])]

    for numberInLine in currLine:
        if number[0] in range(numberInLine[0]-1, numberInLine[1]+1):
            found.append(lines[lineNum][numberInLine[0]:numberInLine[1]])
    for numberInLine in prevLine:
        if number[0] in range(numberInLine[0]-1, numberInLine[1]+1):
            found.append(lines[lineNum - 1][numberInLine[0]:numberInLine[1]])
    for numberInLine in nextLine:
        if number[0] in range(numberInLine[0]-1, numberInLine[1]+1):
            found.append(lines[lineNum + 1][numberInLine[0]:numberInLine[1]])

    if len(found) > 1:
        result = reduce(lambda x, y: int(x)*int(y), found)
        solution += result.real

    return solution

def solution1(lines):
    global solutionRes
    for lineNum, value in enumerate(lines):
        numbers = [(m.start(0), m.end(0)) for m in re.finditer("\d+", value)]
        for number in numbers:
            solutionRes = check(lines, number, lineNum, solutionRes)

def solution2(lines):
    global solutionRes2
    for lineNum, value in enumerate(lines):
        numbers = [(m.start(0), m.end(0)) for m in re.finditer("\*", value)]
        for number in numbers:
            solutionRes2 = check2(lines, number, lineNum, solutionRes2)


with open('input.txt', 'r') as file:
    lines = file.readlines()
    solution1(lines)
    solution2(lines)






print(solutionRes)
print(solutionRes2)


