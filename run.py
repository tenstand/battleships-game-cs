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
