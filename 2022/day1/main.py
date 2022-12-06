input = open("2022/day1/input.txt", "r").read() # opens input file

inputArray = [ x for x in input.split("\n") ]
resultArray, currentSum = [], 0  # init

for item in inputArray:
    if item != "":
        currentSum += int(item)
    else:
        resultArray.append(currentSum)
        currentSum = 0

print("*"*20)
print("Day One")
print("Part One Answer: "+str(max(resultArray)))

resultArray.sort()
part2Array = resultArray[-3:]
part2Answr = sum(part2Array)

print("Part Two Answer: "+str(part2Answr))
print("*"*20)
