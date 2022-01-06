import time

def getInput(day,demo = False):
    if demo:
        input = open("2021/"+day+"/demo.txt", "r").read()
    else:
        input = open("2021/"+day+"/input.txt", "r").read()
    return input

def createInputArray(input):
    resultingArray = []
    for row in input.splitlines():
        rowAppendedObject = {"x1":0,"y1":0,"x2":0,"y2":0}
        for a, part in enumerate(row.split( "-> ")):
            for b, coordinate in enumerate(part.split(",")):
                if a == 0 and b == 0:
                    # Värdet vi har att göra med är x1
                    rowAppendedObject["x1"] = int(coordinate)
                elif a == 0 and b == 1:
                    rowAppendedObject["y1"] = int(coordinate)
                elif a == 1 and b == 0:
                    rowAppendedObject["x2"] = int(coordinate)
                elif a == 1 and b == 1:
                    rowAppendedObject["y2"] = int(coordinate)
        resultingArray.append(rowAppendedObject)
    return resultingArray

def createMap(sizeX, sizeY):
    map = []
    for i in range(0, sizeY+1):
        map.append([])
    for row in map:
        for i in range(0, sizeX+1):
            row.append(0)
    return map

def addLine(map, x1, y1, x2, y2, allowDiagonalLines = False):
    if y1 == y2:
        factor = 1 if x2 > x1 else -1
        for i in range(x1,x2+(1*factor),factor):
            map[y1][i] += 1
    elif x1 == x2:
        factor = 1 if y2 > y1 else -1
        for i in range(y1, y2+(1*factor), factor):
            map[i][x1] += 1
    elif allowDiagonalLines != False:
        xFactor = 1 if x2 > x1 else -1
        xRangeList = list(range(x1,x2+(1*xFactor),xFactor))
        yFactor = 1 if y2 > y1 else -1
        yRange = range(y1,y2+(1*yFactor),yFactor)
        for a, i in enumerate(yRange):
            map[i][xRangeList[a]] += 1
    return map

def findIntersectingLines(map):
    result = 0
    for row in map:
        for column in row:
            if column > 1:
                result += 1
    return result

def part1(array, map):
    for row in array:
        map = addLine(map, row["x1"],  row["y1"], row["x2"], row["y2"])
    return findIntersectingLines(map)

def part2(array, map):
    for row in array:
        map = addLine(map, row["x1"],  row["y1"], row["x2"], row["y2"], True)
    return findIntersectingLines(map)

starttime = time.time()

array = createInputArray(getInput("day5"))

sizeX, sizeY = max([max(row["x1"] for row in array),max(row["x2"] for row in array)]), max([max(row["y1"] for row in array),max(row["y2"] for row in array)])

map = createMap(sizeX, sizeY)

print("Del 1:",part1(array, map))

map = createMap(sizeX, sizeY)

print("Del 2:",part2(array, map))

print("Utförandet tog %s sekunder" % (round(time.time()-starttime, 5)))