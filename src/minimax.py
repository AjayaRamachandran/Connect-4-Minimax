###### IMPORT ######
import random as rand
import time
import copy

###### VARIABLES ######
simLevel = 4
treeCoords = None
gameStateLibrary = [[]]
nodeDepth = 0
permutations = 0
testBoard = []

###### FUNCTIONS ######

def checkIfFull(sampleBoard):
    notFull = True
    sampleBoardCopy = sampleBoard

    for column in sampleBoardCopy:
        for row in column:
            if row == 0:
                notFull = False

    return(notFull)



def simAddCoin(column, variation, team): # simulates the placing of a coin in a certain column then returns the new gameState
    simheight = 5
    variationCopy = variation
    columnCopy = column
    teamCopy = team

    if variationCopy[columnCopy][simheight] == 0: 
        while variationCopy[columnCopy][simheight - 1] == 0 and not simheight == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
            simheight -= 1

        if teamCopy == "player":
            variationCopy[columnCopy][simheight] = 1 # fill said slot with red piece
        elif teamCopy == "ai":
            variationCopy[columnCopy][simheight] = 2 # fill said slot with yellow piece


        return(variationCopy) # returns success/fail based on whether the slot is a valid move
    else:
        return("fail") # if added coin is in an already full column, it cannot be placed, so function returns "fail"



def mapVariations(board, mapTeam, runDepth): # calculates every possible next move given a board state
    global permutations
    mapTeamCopy = mapTeam
    runDepthCopy = runDepth
    boardCopy = copy.deepcopy(board)

    for testCol in range(0,7): # runs across every column
        testBoard = boardCopy
        if checkIfFull(testBoard) == False: # if the board is full, don't run this bit
            simState = simAddCoin(column=testCol, variation=testBoard, team=mapTeamCopy) # runs the simAddCoin functions for every column
            if not simState == "fail": # excludes columns where the next move would exit the top of the board
                permutations += 1
                gameStateLibrary[nodeDepth + 1].append(simState) # appends the simState to the library, inside the next nodeDepth
 


def simulate(depth): # runs the mapVariations functions for every board state in a certain nodeDepth
    #global testBoard
    global nodeDepth
    global gameStateLibrary

    gameStateLibrary.append([]) # appends a placeholder in the position of the next nodeDepth

    for variation in gameStateLibrary[nodeDepth]:

        if depth % 2 == 0:
            simTeam = "ai"
        else:
            simTeam = "player"

        mapVariations(board=variation, mapTeam=simTeam, runDepth=nodeDepth) # runs the mapVariations function if the simLevel limit is not reached



def simulateTree(): # head function for branch simulation
    global nodeDepth
    nodeDepth = 0
    for nodeDepth in range(simLevel): # runs the simulate function for every nodeDepth to the limit
        simulate(depth=nodeDepth)



def aiTest(board): # master function, cues tree simulation and minimax algorithm
    global gameStateLibrary

    gameStateLibrary = [[]]
    boardCopy = board
    gameStateLibrary[0].append(boardCopy) # primes simulation with zeroeth nodeDepth, which is the current board state
    
    simulateTree()

    aiMove = rand.randint(0,6) # test

    time.sleep(0.2)


    return(aiMove)



def aiPlay():
    time.sleep(0)

###### PSEUDOCODE ######

# spawns a simulation agent (which recursively spawns 7 more, etc.)

# once simulation is finished, the scoring script runs through every end state and assigns a numerical score (my score - opp score)

# minimax algorithm then runs, working its way up the tree until all 7 choices have a score assigned

# chooses the highest score (technically part of minimax)

# returns choice to main