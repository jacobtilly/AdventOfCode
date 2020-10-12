# Advent of Code
# Day One Part Two
# Jacob Tilly

inputFile = open("2019/1/input.txt", "r")
inputString = inputFile.read()

inputArray = inputString.split("\n")

sum = 0

for mass in inputArray:
    fuel = int(mass) // 3 - 2
    sum += fuel

    while fuel > 0:
        fuel = fuel // 3 - 2
        sum += fuel

print(sum)