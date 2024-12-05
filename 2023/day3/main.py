import re
from aocd import get_data
import os

# Jacob Tilly, dec 2023

def getPuzzleInput(day, debug = False):
    if debug:
        testData = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
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

def is_symbol(character):
    return re.match("[^\sA-Za-z0-9\.]", character) is not None

def get_adjacent_symbols(input, x, y):
    # Checking adjacent cells for symbols
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(input) and 0 <= nx < len(input[ny]) and is_symbol(input[ny][nx]):
                return True
    return False

def p1(input):
    matches = set()
    for y, row in enumerate(input):
        for x, char in enumerate(row):
            if char.isdigit():
                # Check if the digit is part of a larger number
                number = re.search(r'\d+', input[y][x:]).group()
                number_length = len(number)
                # Check adjacent cells of each digit of the number
                for i in range(x, x + number_length):
                    if get_adjacent_symbols(input, i, y):
                        matches.add(int(number))
                        break
    return sum(matches)

# Read input and process
inputTest = getPuzzleInput(3)
inputList = [x for x in inputTest.splitlines()]
print(p1(inputList))
