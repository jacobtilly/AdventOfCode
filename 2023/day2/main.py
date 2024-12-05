import re
from aocd import get_data
import os

# Jacob Tilly, dec 2023

def getPuzzleInput(day, debug = False):
    if debug:
        testData = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
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

def createSensibleInput(puzzleInput):
    inputList = [x for x in puzzleInput.splitlines()]
    inputObjectsList = []
    for item in inputList:
        # Game
        totalBlue, totalRed, totalGreen = 0, 0, 0
        gameId = (item.split(":")[0])[5:]
        sessions = [x.strip() for x in item.split(":")[1].split(";")]
        gameObject = {
            "game": gameId,
            "sessions": [],
            "totals": {
                "blue": 0,
                "red": 0,
                "green": 0
            }
        }
        for session in sessions: # 1 red 2 blue
            countBlue, countRed, countGreen = 0, 0, 0
            colorParts = [x.strip() for x in session.split(",")]
            for colorPart in colorParts: # 1 red
                if "blue" in colorPart:
                    countBlue += int(colorPart[:colorPart.index("blue")])
                    totalBlue += countBlue
                if "green" in colorPart:
                    countGreen += int(colorPart[:colorPart.index("green")])
                    totalGreen += countGreen
                if "red" in colorPart:
                    countRed += int(colorPart[:colorPart.index("red")])
                    totalRed += countRed
            sessionObject = {
                "blue": countBlue,
                "red": countRed,
                "green": countGreen
            }
            gameObject["sessions"].append(sessionObject)
        gameObject["totals"]["blue"], gameObject["totals"]["red"], gameObject["totals"]["green"] = int(totalBlue), int(totalRed), int(totalGreen)
        inputObjectsList.append(gameObject)

    return inputObjectsList

def p1(inputObjects):
    result = 0
    # Which games are possible if we have 12 red cubes, 13 green cubes, and 14 blue cubes?
    for game in inputObjects:
        possibleGame = True
        for session in game["sessions"]:
            if session["blue"] > 14 or session["red"] > 12 or session["green"] > 13:
                possibleGame = False
                break
        if possibleGame:
            result += int(game["game"])
    
    return result

def p2(inputObjects):
    result = 0
    for game in inputObjects:
        highestBlue, highestRed, highestGreen = 0, 0, 0
        for session in game["sessions"]:
            if session["blue"] > highestBlue:
                highestBlue = session["blue"]
            if session["red"] > highestRed:
                highestRed = session["red"]
            if session["green"] > highestGreen:
                highestGreen = session["green"]
        power = highestBlue * highestRed * highestGreen
        result += power
    return result

input = getPuzzleInput(2)
sensibleInput = createSensibleInput(input)

print(p1(sensibleInput))
print(p2(sensibleInput))