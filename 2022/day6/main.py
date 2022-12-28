from aocd import get_data

# Jacob Tilly, dec 2022

puzzleData = get_data(year=2022, day=6)

def part1():
    for i, x in enumerate(range(len(puzzleData)-3)):
        marker, markerCorrect = puzzleData[i:i+4], True # init
        for character in marker:
            markerCorrect = False if marker.count(character) > 1 else markerCorrect
        if markerCorrect:
            return marker, x+4

def part2():
    for i, x in enumerate(range(len(puzzleData)-13)):
        marker, markerCorrect = puzzleData[i:i+14], True # init
        for character in marker:
            markerCorrect = False if marker.count(character) > 1 else markerCorrect
        if markerCorrect:
            return marker, x+14


print(part1())
print(part2())