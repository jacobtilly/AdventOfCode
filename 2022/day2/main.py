def getArrayFromInput(file):
    input = open(file, "r").read() # opens input file
    inputArray = [ x for x in input.split("\n") ]
    return inputArray

def createSensibleInput(inputArray):
    outputArray = []
    for item in inputArray:
        outputArray.append({"player1":item[0],"player2":item[2]})
    return outputArray

def rockPaperScissorRound(player1, player2):
    roundScore = 0
    match player2:
        case "X":
            roundScore += 1
            if(player1 == "A"):
                roundScore += 3
            if(player1 == "C"):
                roundScore += 6
        case "Y":
            roundScore += 2
            if(player1 == "B"):
                roundScore += 3
            if(player1 == "A"):
                roundScore += 6
        case "Z":
            roundScore += 3
            if(player1 == "C"):
                roundScore += 3
            if(player1 == "B"):
                roundScore += 6
    return roundScore

def rockPaperScissorsPart2(player1, neededOutcome):
    score = 0
    if(neededOutcome == "X"):
        score += 0
    if(neededOutcome == "Y"):
def part1():
    inputArray = getArrayFromInput("2022/day2/input.txt")
    sensibleInput = createSensibleInput(inputArray)
    player1Score, player2Score = 0, 0
    for item in sensibleInput:
        player1Score += rockPaperScissorRound(item["player1"], item["player2"])
    print("Part One Answer: "+str(player1Score))

def part2():
    inputArray = getArrayFromInput("2022/day2/input.txt")
    sensibleInput = createSensibleInput(inputArray)
    correctedInput = gnerateNewStrategicInputs(sensibleInput)
    player1Score, player2Score = 0, 0
    for item in correctedInput:
        player1Score += rockPaperScissorRound(item["player1"], item["player2"])
    print("Part Two Answer: "+str(player1Score))

print(part1())
print(part2())