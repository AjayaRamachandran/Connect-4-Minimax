###### IMPORT ######
import random as rand
import time
import copy
from math import *

import windetection
import transpositiontable
import statepackager as spau # stands for [S]tate [P]ackage [A]nd [U]npackage
###### VARIABLES ######
simLevel = 6
testBoard = []

boardWidth = 7
boardHeight = 6

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
    simheight = boardHeight - 1
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
    for iter in range(boardWidth): # runs across every column
        testCol = int(4 + (((iter % 2 - 0.5) * 2) * round(iter / 2 + 0.1))) - 1 # CHANGE IF BOARD DIMENSIONS CHANGE
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
    gameOver = (windetection.mainRun(gameState, "tree") != 0)

    
    if depth == simLimit or gameOver:
        score = windetection.mainRun(gameState, "tree")
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
    
def naiveWinPrevention(): # runs if the AI is caught in a trap and the player is going to win in the very next move - blocks any wins possible, even if it opens a different win
    global boardCopy

    print("All levels of Minimax failed (ID:TRAP - player has two consecutive open wins | tags: <partially avoidable>, <imminent>). Commencing naive win prevention")

    currentBoardScore = windetection.mainRun(boardCopy, "tree") # finds the score of the current game state
    currentBestDiff = 0
    currentBestAIMove = 3
    listOfDiffs = []

    for testCol in range(len(boardCopy)): # if any game state after the AI plays is better than the current one (AKA a win is prevented) then find the best such move

        testPlayerMoveState = simAddCoin(column=testCol, variation=boardCopy, team=1)
        testAIMoveState = simAddCoin(column=testCol, variation=boardCopy, team=2)

        if testAIMoveState != "fail":
            testAIMoveScore = windetection.mainRun(testAIMoveState, "tree")
            testPlayerMoveScore = windetection.mainRun(testPlayerMoveState, "tree")
            diff = testPlayerMoveScore - testAIMoveScore
            listOfDiffs.append(diff)

            if currentBestDiff <= diff:
                currentBestDiff = diff
                currentBestAIMove = testCol

    print("In each column, what score is prevented when AI plays there: " + str(listOfDiffs))
    print("Naive win prevention states that the best move to play is in column " + str(currentBestAIMove))

    return currentBestAIMove

    

def aiPlay(board): # master function, cues tree simulation and minimax algorithm
    global boardCopy
    global listOfChildrenColumns
    global listOfChildrenScores
    global iters
    global simLimit

    boardCopy = copy.deepcopy(board)
    listOfChildrenColumns = []
    listOfChildrenScores = []
    iters = 0

    simLimit = simLevel

    minimax(boardCopy, 0, -100000, 100000, False)
    
    print("Number of game states searched: " + str(iters))
    print("Minimax scores of each column: " + str(listOfChildrenScores))

    if len(listOfChildrenScores) > 0:
        surefireLoss = 1
        for child in listOfChildrenScores:
            if child != 2:
                surefireLoss = 0

        simLimit = simLevel
        
        while surefireLoss == 1:

            if len(listOfChildrenScores) > 0:

                if surefireLoss == 1 and simLimit > 2:
                    simLimit = simLimit - 1

                    print("Minimax with SimLevel of " + str(simLimit + 1) + " failed (ID:TRAP - player has two consecutive open wins | tags: <unavoidable>, <later>). Repeating with SimLevel of " + str(simLimit))

                    listOfChildrenScores = []
                    listOfChildrenColumns = []
                    iters = 0

                    minimax(boardCopy, 0, -100000, 100000, False)

                    print("    Number of game states searched: " + str(iters))
                    print("    Minimax scores of each column: " + str(listOfChildrenScores))

                elif simLimit == 2:
                    return naiveWinPrevention() # if the player is going to win in the next turn because of a trap, play into the trap just in case they don't know they set it up

                surefireLoss = 1
                for child in listOfChildrenScores:
                    if child != 2:
                        surefireLoss = 0
                    
        aiMove = listOfChildrenColumns[listOfChildrenScores.index(min(listOfChildrenScores))] # returns the move that yields the lowest score (best for AI)
    else:
        aiMove = "None"
    #aiMove = rand.randint(0,6) # test
    return(aiMove)