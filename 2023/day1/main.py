import re
from aocd import get_data
import os

# Jacob Tilly, dec 2023

def getPuzzleInput(day, debug = False):
    if debug:
        testData = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen"""
        return testData
    if os.path.isfile("2023/day"+str(day)+"/input.txt"):
        puzzleInput = open("2023/day"+str(day)+"/input.txt", "r").read()
        return puzzleInput
    else:
        onlineInput = get_data(year=2023, day=day)
        file = open("2023/day"+str(day)+"/input.txt", "w")
        file.write(onlineInput)
        file.close()
        return onlineInput

def p1(puzzleInput):
    inputList = puzzleInput.splitlines()
    calibrationSum = 0

    for input in inputList:
        digits = re.findall(r"\d", input)
        firstDigit = digits[0]
        lastDigit = digits[-1]
        calibrationSum += int(str(firstDigit) + str(lastDigit))
        
    return calibrationSum

def p2(puzzleInput):
    inputList = puzzleInput.splitlines()
    calibrationSum = 0

    translationTable = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for line in inputList:
        # Use lookahead to find overlapping matches
        digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        if digits:
            # Translate words to digits
            firstDigit = translationTable.get(digits[0], digits[0])
            lastDigit = translationTable.get(digits[-1], digits[-1])

            # Ensure they are integers
            firstDigit = int(firstDigit) if isinstance(firstDigit, str) else firstDigit
            lastDigit = int(lastDigit) if isinstance(lastDigit, str) else lastDigit

            calibrationSum += int(f"{firstDigit}{lastDigit}")

    return calibrationSum

input = getPuzzleInput(1)

print(p1(input))
print(p2(input))