from random import randint

# Legend:
EMPTY = 0
SHIP = 1
HIT = 2
MISS = 3

def getBoard(boardSize):
    board = []
    for i in range(boardSize):
        board.append([EMPTY] * boardSize)
    return board

# Output the board to the console:
def printBoard(board):
    for row in board:
        rowStr = ""
        for cell in row:
            cellStr = str(cell)
            rowStr += cellStr
        print(rowStr)

# Output the board to the console with row and column indexes and hidden ships:
def printPlayBoard(board):
    rowIndex = " "
    rowBorder = "-"
    colIndex = 0

    for i in range(len(board[0])):
        rowIndex = rowIndex + " " + str(i)
        rowBorder += "--"

    print(rowIndex)
    print(rowBorder)

    for row in board:
        rowStr = str(colIndex) + "|"
        colIndex += 1
        for cell in row:
            if(cell == HIT):
                cellStr = "* "
            else:
                if(cell == MISS):
                    cellStr = "X "
                else:
                    cellStr = "O "
            rowStr += cellStr

        print(rowStr)
    
    print("\n")

    def getNumberOfShips(board):
        numberOfShips = 0
    for row in board:
        for cell in row:
            if(cell == SHIP):
                numberOfShips += 1
    return numberOfShips

    def getRandomCoords(board):
        x = randint(0, len(board) - 1)
        y = randint(0, len(board) - 1)
    return x, y
    
# Create ships in random locations:
    def addShips(board, numberOfShips):
        for i in range(numberOfShips):
            shipRow, shipColumn = getRandomCoords(board)
            setValue(board, shipRow, shipColumn, SHIP)

# Returns the value at the provided co-ordinates:
    def getValue(board, x, y):
        return board[y][x]

# Sets the value at the co-ordinates of the board:
    def setValue(board, x, y, value):
        board[y][x] = value

# Validate user input:
def validate(board, x, y):
    validRange = range(len(board[0]))
    try:
        x = int(x)
        y = int(y)
        if(x not in validRange or y not in validRange):
            print("Out of range!")
            return False
        else:
            value = getValue(board, x, y)
            if(value > SHIP):
                print("You've tried those co-ordinates already!")
                return False
            else:
                return True
    except ValueError:
        print("Please use valid co-ordinates")
        return False

def takeTurn(board):
    printPlayBoard(board)
    x = raw_input("Enter co-ordinate X: ")
    y = raw_input("Enter co-ordinate Y: ")

    isValid = validate(board, x, y)

    if(isValid):
        x = int(x)
        y = int(y)
        value = getValue(board, x, y)
        print("\n")
        if(value == SHIP):
            setValue(board, x, y, HIT)
            print("* * * * * * * *")
            print("* Direct hit! *")
            print("* * * * * * * *")

        else:
            print("Sorry, you missed")
            setValue(board, x, y, MISS)
        return True
        
    return False
   
# Play a full game. Returns 1 for a win, 0 for a loss
    def playGame():
        BOARD_SIZE = 3
        NUMBER_OF_SHIPS = 3
        BOARD = getBoard(BOARD_SIZE)

    addShips(BOARD, NUMBER_OF_SHIPS)
    numberOfTurns = 5

    while(getNumberOfShips(BOARD) > 0 and numberOfTurns > 0):
        status = str(getNumberOfShips(BOARD)) + " ships left. "
        status += str(numberOfTurns) + " turns left"
        print(status)
        print("\n")

        if(takeTurn(BOARD)):
            numberOfTurns -= 1