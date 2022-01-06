def getInput(day,demo = False):
    if demo:
        input = open("2021/"+day+"/demo.txt", "r").read()
    else:
        input = open("2021/"+day+"/input.txt", "r").read()
    return input

def createInputArray(input):
    numbers, *boards = input.split("\n\n")
    numbers = [int(i) for i in numbers.split(",")]
    boards = [[[int(col) for col in row.split()] for row in board.split("\n")] for board in boards]
    return numbers, boards

def markBoard(number, board):
    for row in board:
        for col in range(0, len(row)):
            if row[col] == number:
                row[col] = "x"

def boardSum(board):
    sum = 0
    for row in board:
        for col in range(0, len(row)):
            if type(row[col]) == int:
                sum += row[col]
    return sum


def checkForWinner(board):
    winner = False
    for row in board:
        winner = all(elem in ["x"] for elem in row)
        if winner:
            return winner
    for col in range(0,5):
        winner = all(elem in ["x"] for elem in [row[col] for row in board])
        if winner:
            return winner

def allWinners(boards):
    allWon = True
    for board in boards:
        if not checkForWinner(board):
            allWon = False
    return allWon
    

def part1():
    numbers, boards = createInputArray(getInput("day4"))
    for number in numbers:
        for board in boards:
            markBoard(number,board)
            if checkForWinner(board):
                return boardSum(board)*number

def part2():
    numbers, boards = createInputArray(getInput("day4"))
    for number in numbers:
        for board in boards:
            markBoard(number,board)
            if allWinners(boards):
                return boardSum(board)*number

print("Del 1:",part1())
print("Del 2:",part2())