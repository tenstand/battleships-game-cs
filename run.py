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