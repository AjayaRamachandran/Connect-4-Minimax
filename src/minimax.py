###### IMPORT ######
import random as rand
import time
import copy
from math import *

import windetection
import transpositiontable
###### VARIABLES ######
simLevel = 5
testBoard = []

###### FUNCTIONS ######
def checkIfFull(sampleBoard):
    full = True
    sampleBoardCopy = copy.deepcopy(sampleBoard)

    for column in sampleBoardCopy:
        for row in column:
            if row == 0:
                full = False

    return(full)


def simAddCoin(column, variation, team): # simulates the placing of a coin in a certain column then returns the new gameState
    simheight = 5
    variationCopy = copy.deepcopy(variation)
    columnCopy = column
    teamCopy = int(team)

    if variationCopy[columnCopy][simheight] == 0: 
        while variationCopy[columnCopy][simheight - 1] == 0 and not simheight == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
            simheight -= 1
        variationCopy[columnCopy][simheight] = teamCopy # fill said slot with red or yellow piece based on whose turn it is

        return(variationCopy) # returns success/fail based on whether the slot is a valid move
    else:
        return("fail") # if added coin is in an already full column, it cannot be placed, so function returns "fail"


def simulateChildren(state, team, depth):
    boardCopy = copy.deepcopy(state)
    children = []
    '''
    optimizedChoice = transpositiontable.optimizedChoose(state) # checks the transpositionTable to find which column was searched successfully in similar game states
    if optimizedChoice != -1:
        testCol = optimizedChoice
        testBoard = copy.deepcopy(boardCopy)
        if checkIfFull(testBoard) == False: # if the board is full, don't run this bit
            simState = simAddCoin(column=testCol, variation=testBoard, team=team) # runs the simAddCoin functions for every column
            if not simState == "fail": # excludes columns where the next move would exit the top of the board
                children.append((copy.deepcopy(simState), testCol))
                if depth == 0:
                    listOfChildrenColumns.append(testCol)
    '''
    for iter in range(7): # runs across every column
        testCol = int(4 + (((iter % 2 - 0.5) * 2) * round(iter / 2 + 0.1))) - 1
        testBoard = copy.deepcopy(boardCopy)
        if checkIfFull(testBoard) == False: # if the board is full, don't run this bit
            simState = simAddCoin(column=testCol, variation=testBoard, team=team) # runs the simAddCoin functions for every column
            if not simState == "fail": # excludes columns where the next move would exit the top of the board
                children.append((copy.deepcopy(simState), testCol))
                if depth == 0:
                    listOfChildrenColumns.append(testCol)
    
    return children


def minimax(state, depth, alpha, beta, maximizingPlayer):
    global iters
    iters += 1
    gameState = copy.deepcopy(state)
    gameOver = (windetection.mainRun(gameState) != 0)

    
    if depth == simLevel or gameOver:
        score = windetection.mainRun(gameState)
        #transpositiontable.add((gameState, score))
        return score
    
    if maximizingPlayer:
        maxEval = -100000
        family = simulateChildren(gameState, ((depth % 2 == 0) + 1), depth)
        for child in family:
            eval = minimax(child[0], depth+1, alpha, beta, False)
            #print(str(eval) + "lvl" + str(depth))
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                #transpositiontable.add(child)
                break
        return maxEval
    else:
        minEval = 100000
        family = simulateChildren(gameState, ((depth % 2 == 0) + 1), depth)
        for child in family:
            #print(child)
            eval = minimax(child[0], depth+1, alpha, beta, True)
            #print(str(eval) + "lvl" + str(depth))
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                #transpositiontable.add(child)
                break
            if depth == 0:
                listOfChildrenScores.append(minEval)
        return minEval
    

def aiTest(board): # master function, cues tree simulation and minimax algorithm
    global boardCopy
    global listOfChildrenColumns
    global listOfChildrenScores
    global iters

    boardCopy = copy.deepcopy(board)
    listOfChildrenColumns = []
    listOfChildrenScores = []
    iters = 0

    minimax(boardCopy, 0, -100000, 100000, False)
    print(iters)
    print(listOfChildrenScores)

    if len(listOfChildrenScores) > 0:
        aiMove = listOfChildrenColumns[listOfChildrenScores.index(min(listOfChildrenScores))]
    else:
        aiMove = "None"
    #aiMove = rand.randint(0,6) # test
    return(aiMove)


def aiPlay():
    time.sleep(0)