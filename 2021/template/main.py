import time

def getInput(day,demo = False):
    if demo:
        input = open("2021/"+day+"/demo.txt", "r").read()
    else:
        input = open("2021/"+day+"/input.txt", "r").read()
    return input

def createInputArray(input, separator):
    return [row for row in input.split(separator)]
    # Modifiera denna rad för att skapa data som makear sense

def part1(inputArray):
    return
def part2(inputArray):
    return

# Execute code below:
starttime = time.time()


print("Execution time: %s seconds" % (round(time.time()-starttime, 5)))