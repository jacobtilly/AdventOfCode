def getInput(demo):
    if demo:
        input = open("2021/day1/demo.txt", "r").read()
    else:
        input = open("2021/day1/input.txt", "r").read()
    return input

def createInputArray(input, separator):
    return [row for row in input.split(separator)]

def part1(inputArray):
    sum = 0
    for idx, data in enumerate(inputArray):
        if data > inputArray[idx-1]:
            sum += 1
    return sum

def part2(inputArray):
    count = 0
    slidingSums = list()
    for idx, data in enumerate(inputArray):
        if(int(idx) > 1):
            slidingSum = int(data)+int(inputArray[idx-1])+int(inputArray[idx-2])
            slidingSums.append(slidingSum)
    for idx, data in enumerate(slidingSums):
        if data > slidingSums[idx-1]:
            count += 1
    return count

print(part1(createInputArray(getInput(False),"\n")))
print(part2(createInputArray(getInput(False),"\n")))