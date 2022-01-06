import time

def getInput(day,demo = False):
    if demo:
        input = open("2021/"+day+"/demo.txt", "r").read()
    else:
        input = open("2021/"+day+"/input.txt", "r").read()
    return input

def createInputArray(input):
    return [row for row in input.split(",")] # Modifiera denna rad för att skapa data som makear sense

def part1(inputArray):
    input = createInputArray(getInput())
    result = input
    return result
def part2(inputArray):
    input = createInputArray(getInput())
    result = input
    return result

# Execute code below:
starttime = time.time()

print(part1())
print(part2())

print("Execution time: %s seconds" % (round(time.time()-starttime, 5)))