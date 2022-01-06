import time

def createInputArray(input):
    return [int(row) for row in input.split(",")]

def createFishList(input:list):
    fishlist = [0,0,0,0,0,0,0,0,0]
    for fish in input:
        fishlist[fish] += 1
    return fishlist

def swimswim(fishList:list,swimtime:int):
    for _ in range(swimtime):
        poppedFish = fishList.pop(0)
        fishList[6] += poppedFish
        fishList.append(poppedFish) if poppedFish > 0 else fishList.append(0)
    return sum(fishList)

starttime = time.time()
print("Execution started!")
print("Part 1",swimswim(createFishList(createInputArray(open("2021/day6/input.txt", "r").read())),80))
print("Part 2",swimswim(createFishList(createInputArray(open("2021/day6/input.txt", "r").read())),256))
print("Execution time: %s seconds" % (round(time.time()-starttime, 5)))