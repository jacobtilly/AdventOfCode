from typing import Match

def getInput(day,demo = False):
    if demo:
        input = open("2021/"+day+"/demo.txt", "r").read()
    else:
        input = open("2021/"+day+"/input.txt", "r").read()
    return input

def createInputArray(input, separator):
    return [{"instruction":row.split(" ")[0],"value":row.split(" ")[1],"delta-x":0,"delta-y":0} for row in input.split(separator)]

def part1(inputArray):
    position = {"x":0,"y":0}
    for row in inputArray:
        value = int(row["value"])
        match row["instruction"]:
            case 'forward':
                row["delta-x"] = value
            case 'up':
                row["delta-y"] = value
            case 'down':
                row["delta-y"] = -abs(value)
            case _:
                print("Okänt kommando")
        position["x"] += row["delta-x"]
        position["y"] += row["delta-y"]
    return position

def part2(inputArray):
    position = {"x":0,"y":0,"aim":0}
    for row in inputArray:
        value = int(row["value"])
        match row["instruction"]:
            case 'forward':
                row["delta-x"] = value
                row["delta-y"] = value * position["aim"]
            case 'up':
                position["aim"] += value
            case 'down':
                position["aim"] -= value
            case _:
                print("Okänt kommando")
        position["x"] += row["delta-x"]
        position["y"] += row["delta-y"]

    return position

# Execute code below:
# Part 1
position = part1(createInputArray(getInput("day2"),"\n"))
print(int(position["x"])*abs(int(position["y"])))

# Part 2
position = part2(createInputArray(getInput("day2"),"\n"))
print(int(position["x"])*abs(int(position["y"])))