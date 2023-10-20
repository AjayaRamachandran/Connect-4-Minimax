###### IMPORT ######

import copy
from math import *
import time


###### VARIABLES ######
myboard = []
boardScore = 0

# winType = 1, 2, 3, 4 correspond to vertical, horizontal, LDRU diagonal, LURD diagonal wins respectively

###### FUNCTIONS ######

def advancedGameCutout(col, row, winType, team, length, type):
    advancedGameBoardCutout = []

    if winType == 1:
        if row <= 6 - length:
            for Yoffset in range(0, length):
                if row + Yoffset <= 5 and col <= 6:
                    advancedGameBoardCutout.append(myboard[col][row+Yoffset])
                else:
                    advancedGameBoardCutout.append(0)
        else:
            return 0
    
    if winType == 2:
        if col <= 7 - length:
            for Xoffset in range(0, length):
                if row <= 5 and col + Xoffset <= 6:
                    advancedGameBoardCutout.append(myboard[col+Xoffset][row])
                else:
                    advancedGameBoardCutout.append(0)
        else:
            return 0

    if winType == 3:
        Yoffset = -1
        if row <= 6 - length and col <= 7 - length:
            for Xoffset in range(0, length):
                Yoffset += 1
                if row + Yoffset <= 5 and col + Xoffset <= 6:
                    advancedGameBoardCutout.append(myboard[col+Xoffset][row+Yoffset])
                else:
                    advancedGameBoardCutout.append(0)
        else:
            return 0

    if winType == 4:
        Yoffset = -1
        if row <= 6 - length and col <= 7 - length:
            for Xoffset in range(length-1, -1, -1):
                Yoffset += 1
                if row + Yoffset <= 5 and col + Xoffset <= 6:
                    advancedGameBoardCutout.append(myboard[col+Xoffset][row+Yoffset])
                else:
                    advancedGameBoardCutout.append(0)
        else:
            return 0

    if all(item == team for item in advancedGameBoardCutout):
        if type == "main":
            winCells = []
            if winType == 1:
                for iter in range(length):
                    winCells.append([col, row+iter])
            if winType == 2:
                for iter in range(length):
                    winCells.append([col+iter, row])
            if winType == 3:
                for iter in range(length):
                    winCells.append([col+iter, row+iter])
            if winType == 4:
                for iter in range(length):
                    winCells.append([col+3-iter, row+iter])
            return winCells
        else:
            return 1
    else:
        return 0

def checkforPoints(playerWinWeight, aiWinWeight, thrStkWeight, type): # function to oversee the convolution of a single matrix at all locations on the board
    totalScore = 0
    for column in range(len(myboard)):
        for row in range(len(myboard[column])):
            for winType in range(1,5):
                score = advancedGameCutout(col=column, row=row, winType=winType, team=1, length=4, type=type)
                if score == 1 or score == 0:
                    totalScore += score * playerWinWeight
                else:
                    return score
            for winType in range(1,5):
                score = advancedGameCutout(col=column, row=row, winType=winType, team=2, length=4, type=type)
                if score == 1 or score == 0:
                    totalScore -= score * aiWinWeight
                else:
                    return score
    
    return totalScore


def mainRun(wcBoard, type): # master function to oversee all function operations (unnecessary abstraction perhaps?)
    '''Takes in two different types of requests, "main" (main.py, reserved for telling wins) and "tree" (minimax.py, reserved for running algorithm).'''
    #start = time.time()
    global myboard
    myboard = copy.deepcopy(wcBoard) # creates a deepcopy of the passed board to avoid editing the original
    boardScore = checkforPoints(playerWinWeight = 2, aiWinWeight = 1, thrStkWeight=0, type=type)
    #print(time.time() - start)

    #print(wcBoard)
    return boardScore # returns the weighted score of the board state at hand back to main.py, or the cell coords of the winning cells if asked

