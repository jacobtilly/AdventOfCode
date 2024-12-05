from aocd import get_data

# Jacob Tilly, dec 2022

puzzleData = get_data(year=2022, day=4).splitlines() # get input for day 4 from aoc
# puzzleData = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8""".splitlines()

puzzleInput = list()
tempInput = list()
p1 = 0
p2 = 0

def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

# ARRAY [[[x, y], [z, a]], [[x, y], [z, a]]]

inputList = [[[x for x in splitted.split("-")] for splitted in item.split(",")] for item in puzzleData]
inputFormatted = list()

for item in inputList:
    partRangeToAppend = list()
    for part in item:
        rangeToAppend = range(int(part[0]), int(part[1])+1)
        partRangeToAppend.append(rangeToAppend)
    inputFormatted.append(partRangeToAppend)

for item in inputFormatted:
    if range_subset(item[0], item[1]) or range_subset(item[1], item[0]):
        p1 += 1
        

for item in inputFormatted:
    if range_subset(item[0], item[1]):
        p2 += 1

print(p1, p2)