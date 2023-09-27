###### IMPORT ######

import copy
from math import *
import time


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
def takeGameCutout(col, row, mSize, team):
    gameBoardCutout = []

    for Xoffset in range(0, mSize): # takes a cutout of the game board of a certain size at a specific location for examining
        columnOfGameBoardCutout = []
        #columnOfGameBoardCutout.append(myboard[col+Xoffset][row])
        for Yoffset in range(0, mSize):
            if row + Yoffset <= 5 and col + Xoffset <= 6:
                columnOfGameBoardCutout.append(myboard[col+Xoffset][row+Yoffset])
            else:
                columnOfGameBoardCutout.append(0)
        
        gameBoardCutout.append(columnOfGameBoardCutout)

    #print(gameBoardCutout)
    filteredMatrix = []

    for x in range(len(gameBoardCutout)): # filters the game board cutout to only look for coins of a specific team. will return a matrix with only 1s and 0s
        rowOfFilteredMatrix = []
        for y in range(len(gameBoardCutout[x])):
            rowOfFilteredMatrix.append(int(team == gameBoardCutout[x][y]))
        filteredMatrix.append(rowOfFilteredMatrix)

    #print(filteredMatrix)
    return filteredMatrix

def detectMatrixMatch(filteredCutout, winMatrix, mSize): # function for checking if the coins in a matrix signify a win
    match = 1
    for row in range(mSize):
        for column in range(mSize):
            if winMatrix[column][row] == 1:
                if filteredCutout[column][row] != 1:
                    match = 0
    #print(match)
    return match
    

def checkforPoints(mType, mSize, team): # function to oversee the convolution of a single matrix at all locations on the board
    score = 0
    for row in range(len(myboard)):
        for column in range(len(myboard[row])):
            filteredMatrix = takeGameCutout(col = column, row = row, mSize = mSize, team = team)
            score += detectMatrixMatch(filteredCutout = filteredMatrix, winMatrix = mType, mSize = mSize)
    
    return score


def runCheck(winWeight, thrStkWeight): # function to oversee the full-board convolution of all different checking Matrices

    boardScore = 0
    boardScore += (checkforPoints(mType = winMatrix1, mSize = 4, team = 1)) * winWeight
    boardScore += (checkforPoints(mType = winMatrix2, mSize = 4, team = 1)) * winWeight
    boardScore += (checkforPoints(mType = winMatrix3, mSize = 4, team = 1)) * winWeight
    boardScore += (checkforPoints(mType = winMatrix4, mSize = 4, team = 1)) * winWeight # runs the checkForPoints function for every possible configuration of a win on red

    boardScore -= (checkforPoints(mType = winMatrix1, mSize = 4, team = 2)) * winWeight
    boardScore -= (checkforPoints(mType = winMatrix2, mSize = 4, team = 2)) * winWeight
    boardScore -= (checkforPoints(mType = winMatrix3, mSize = 4, team = 2)) * winWeight
    boardScore -= (checkforPoints(mType = winMatrix4, mSize = 4, team = 2)) * winWeight # runs the checkForPoints function for every possible configuration of a win on yellow

    return boardScore

    #checkforPoints(mType = threeStkMatrix1, mSize = 9)
    #checkforPoints(mType = threeStkMatrix2, mSize = 9)
    #checkforPoints(mType = threeStkMatrix3, mSize = 9)
    #checkforPoints(mType = threeStkMatrix4, mSize = 9) # runs the checkForPoints function for every possible configuration of a 3-stack


def mainRun(wcBoard): # master function to oversee all function operations (unnecessary abstraction perhaps?)
    #start = time.time()
    global myboard
    myboard = copy.deepcopy(wcBoard) # creates a deepcopy of the passed board to avoid editing the original
    boardScore = runCheck(winWeight=1, thrStkWeight=0)
    #print(time.time() - start)

    #print(wcBoard)
    return boardScore # returns the weighted score of the board state at hand back to main.py

