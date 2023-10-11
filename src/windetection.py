###### IMPORT ######

import copy
from math import *
import time


###### VARIABLES ######
myboard = []
boardScore = 0

# winType = 1, 2, 3, 4 correspond to vertical, horizontal, LDRU diagonal, LURD diagonal wins respectively

###### FUNCTIONS ######

def advancedGameCutout(col, row, winType, team):
    advancedGameBoardCutout = []

    if winType == 1:
        for Yoffset in range(0, 4):
            if row + Yoffset <= 5 and col <= 6:
                advancedGameBoardCutout.append(myboard[col][row+Yoffset])
            else:
                advancedGameBoardCutout.append(0)
    
    if winType == 2:
        for Xoffset in range(0, 4):
            if row <= 5 and col + Xoffset <= 6:
                advancedGameBoardCutout.append(myboard[col+Xoffset][row])
            else:
                advancedGameBoardCutout.append(0)
        
    if winType == 3:
        Yoffset = -1
        for Xoffset in [0,1,2,3]:
            Yoffset += 1
            if row + Yoffset <= 5 and col + Xoffset <= 6:
                advancedGameBoardCutout.append(myboard[col+Xoffset][row+Yoffset])
            else:
                advancedGameBoardCutout.append(0)
        
    if winType == 4:
        Yoffset = -1
        for Xoffset in [3,2,1,0]:
            Yoffset += 1
            if row + Yoffset <= 5 and col + Xoffset <= 6:
                advancedGameBoardCutout.append(myboard[col+Xoffset][row+Yoffset])
            else:
                advancedGameBoardCutout.append(0)

    if all(item == team for item in advancedGameBoardCutout):
        return 1
    else:
        return 0

def checkforPoints(playerWinWeight, aiWinWeight, thrStkWeight): # function to oversee the convolution of a single matrix at all locations on the board

    score = 0
    for column in range(len(myboard)):
        for row in range(len(myboard[column])):
            score += advancedGameCutout(col=column, row=row, winType=1, team=1) * playerWinWeight
            score += advancedGameCutout(col=column, row=row, winType=2, team=1) * playerWinWeight
            score += advancedGameCutout(col=column, row=row, winType=3, team=1) * playerWinWeight
            score += advancedGameCutout(col=column, row=row, winType=4, team=1) * playerWinWeight

            score -= advancedGameCutout(col=column, row=row, winType=1, team=2) * aiWinWeight
            score -= advancedGameCutout(col=column, row=row, winType=2, team=2) * aiWinWeight
            score -= advancedGameCutout(col=column, row=row, winType=3, team=2) * aiWinWeight
            score -= advancedGameCutout(col=column, row=row, winType=4, team=2) * aiWinWeight
    
    return score


def mainRun(wcBoard): # master function to oversee all function operations (unnecessary abstraction perhaps?)
    #start = time.time()
    global myboard
    myboard = copy.deepcopy(wcBoard) # creates a deepcopy of the passed board to avoid editing the original
    boardScore = checkforPoints(playerWinWeight= 2, aiWinWeight = 1, thrStkWeight=0)
    #print(time.time() - start)

    #print(wcBoard)
    return boardScore # returns the weighted score of the board state at hand back to main.py

