from collections import Counter
import pandas as pd

def getInput(day,demo = False):
    if demo:
        input = open("2021/"+day+"/demo.txt", "r").read()
    else:
        input = open("2021/"+day+"/input.txt", "r").read()
    return input

def createInputArray(input, separator):
    return [[char for char in row] for row in input.split(separator)]
    # Modifiera denna rad för att skapa data som makear sense

def mostFrequent(List):
    occurence_count = Counter(List)
    if occurence_count["1"] == occurence_count["0"]:
        return "1"
    else:
        return occurence_count.most_common(1)[0][0]

def leastFrequent(List): # modified for ugly solution to part 2...
    occurence_count = Counter(List)
    if occurence_count["1"] == occurence_count["0"]:
        return "0"
    elif occurence_count["1"] > occurence_count["0"]:
        return "0"
    else:
        return "1"

def part1(inputArray):
    charactersPerIndex = [[] for i in range(len(inputArray[0]))]
    mostFrequentArray = []
    leastFrequentArray = []
    for row in inputArray:
        for ind, char in enumerate(row):
            charactersPerIndex[ind].append(char)

    for row in charactersPerIndex:
        mostFrequentArray.append(mostFrequent(row))
    gamma = int(''.join(mostFrequentArray),2)

    for ind,row in enumerate(mostFrequentArray):
        mostFrequentOccurence = mostFrequent(row)
        if mostFrequentOccurence == "1":
            a = "0"
        else:
            a = "1"
        leastFrequentArray.append(a)

    epsilon = int(''.join(leastFrequentArray),2)

    result = gamma * epsilon
    return result
    

def part2(inputArray):
    oxygenarray = inputArray.copy()
    carbonarray = inputArray.copy()
    target = 0
    while len(oxygenarray) > 1:
        listsToRemove = []
        targetPositionValues = [item[target] for item in oxygenarray]
        mostFrequentValue = mostFrequent(targetPositionValues)
        for i, list in enumerate(oxygenarray):
            if list[target] != mostFrequentValue:
                listsToRemove.append(list)
        for item in listsToRemove:
            oxygenarray.remove(item)
        target += 1
    oxygenGeneratorRating = int(''.join(oxygenarray[0]),2)
    print("Oxygen generator rating:",oxygenGeneratorRating)

    target = 0
    while len(carbonarray) > 1:
        listsToRemove = []
        targetPositionValues = [item[target] for item in carbonarray]
        leastFrequentValue = leastFrequent(targetPositionValues)
        for i, list in enumerate(carbonarray):
            if list[target] != leastFrequentValue:
                listsToRemove.append(list)
        for item in listsToRemove:
            carbonarray.remove(item)
        target += 1
    carbonscrubber = int(''.join(carbonarray[0]),2)
    print("Carbon scrubber rating",carbonscrubber)
    
    return oxygenGeneratorRating * carbonscrubber


# Execute code below:

print("Part 1: " + str(part1(createInputArray(getInput("day3"),"\n"))))
print("Part 2: " + str(part2(createInputArray(getInput("day3"),"\n"))))