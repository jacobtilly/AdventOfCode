from aocd import get_data

# Jacob Tilly, dec 2022

puzzleInput = get_data(year=2022, day=3).splitlines() # get input for day 3 from aoc

p1, p2 = 0, 0 # init

# General: Priorities are 1-26 for a-z, 27-52 for A-Z

# Part 1
for line in puzzleInput: # loop through each line
    rs1, rs2 = line[0:int(len(line)/2)], line[int(len(line)/2):] # split line in half
    common = [match for match in rs1 if match in rs2][0] # find common letter
    p1 += ord(common) - 38 if common.isupper() else ord(common) - 96 # add priority to p1

print(p1) # print part 1 answer

# Part 2
numberGroups = len(puzzleInput) / 3 # get number of groups
groups = [[elf for elf in puzzleInput[(i-1)*3:i*3]] for i in range(1, int(numberGroups)+1)] # split puzzle input into groups of 3

for group in groups: # loop through each group
    usedLetters = [] # make sure that no double letters are used
    for letter in group[0]: # loop through each letter in first elf's list
        if letter in group[1] and letter in group[2] and letter not in usedLetters: # if letter is in all 3 lists
            usedLetters.append(letter) # add letter to usedLetters so it doesn't get counted twice
            p2 += ord(letter) - 38 if letter.isupper() else ord(letter) - 96 # add priority to p2

print(p2) # print part 2 answer