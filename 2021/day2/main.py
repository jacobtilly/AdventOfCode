def getInput(day,demo = False):
    if demo:
        input = open("2021/"+day+"/demo.txt", "r").read()
    else:
        input = open("2021/"+day+"/input.txt", "r").read()
    return input

def createInputArray(input, separator):
    return [{"instruction":row.split(" ")[0],"value":row.split(" ")[1]} for row in input.split(separator)]

def part1(inputArray):
    position = {"x":0,"y":0}
    for row in inputArray:
        if row["instruction"] == "forward":
            position["x"] += int(row["value"])
        if row["instruction"] == "down":
            position["y"] += int(row["value"])
        if row["instruction"] == "up":
            position["y"] -= int(row["value"])
    return position

def part2(inputArray):
    position = {"x":0,"y":0,"aim":0}
    for row in inputArray:
        if row["instruction"] == "forward":
            position["x"] += int(row["value"])
            position["y"] += int(row["value"]) * position["aim"]
        if row["instruction"] == "down":
            position["aim"] += int(row["value"])
        if row["instruction"] == "up":
            position["aim"] -= int(row["value"])
    return position

# Execute code below:
# Part 1
position = part1(createInputArray(getInput("day2"),"\n"))
print(int(position["x"])*int(position["y"]))

# Part 2
position = part2(createInputArray(getInput("day2"),"\n"))
print(int(position["x"])*int(position["y"]))