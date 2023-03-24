###### IMPORT ######

import copy


###### VARIABLES ######
myboard = []
boardScore = 0

## Matrices with checkable arrangements
winMatrix1 = [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]] # vertical win
winMatrix2 = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]] # horizontal win
winMatrix3 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] # LeftDown RightUp diagonal win
winMatrix4 = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]] # LeftUp RightDown diagonal win

threeStkMatrix1 = [[1,1,1],[0,0,0],[0,0,0]] # vertical 3-stack
threeStkMatrix2 = [[1,0,0],[1,0,0],[1,0,0]] # horizontal 3-stack
threeStkMatrix3 = [[1,0,0],[0,1,0],[0,0,1]] # LeftDown RightUp diagonal 3-stack
threeStkMatrix4 = [[0,0,1],[0,1,0],[1,0,0]] # LeftUp RightDown diagonal 3-stack

###### FUNCTIONS ######

def convolveMatrix(col, row, mSize, team): # function for convolving a checking Matrix at a specific location
    None


def checkforPoints(mType, mSize, team): # function to oversee the convolution of a single matrix at all locations on the board
    None


def runCheck(winWeight, thrStkWeight): # function to oversee the full-board convolution of all different checking Matrices

    checkforPoints(mType = winMatrix1, mSize = 16)
    checkforPoints(mType = winMatrix2, mSize = 16)
    checkforPoints(mType = winMatrix3, mSize = 16)
    checkforPoints(mType = winMatrix4, mSize = 16) # runs the checkForPoints function for every possible configuration of a win

    checkforPoints(mType = threeStkMatrix1, mSize = 9)
    checkforPoints(mType = threeStkMatrix2, mSize = 9)
    checkforPoints(mType = threeStkMatrix3, mSize = 9)
    checkforPoints(mType = threeStkMatrix4, mSize = 9) # runs the checkForPoints function for every possible configuration of a 3-stack


def mainRun(wcBoard): # master function to oversee all function operations (unnecessary abstraction perhaps?)
    global myboard
    myboard = copy.deepcopy(wcBoard) # creates a deepcopy of the passed board to avoid editing the original


    return boardScore # returns the weighted score of the board state at hand back to main.py

