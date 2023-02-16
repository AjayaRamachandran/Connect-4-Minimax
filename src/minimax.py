###### IMPORT ######
import random as rand
import time

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

    for column in sampleBoard:
        for row in column:
            if row == 0:
                notFull = False

    return(notFull)



def runAddCoin(column, variation, team, simDepth): # simulates the placing of a coin in a certain column then returns the new gameState
    simheight = 5
    print(variation) # debug

    #print(testBoard) # debug
    if variation[column][simheight] == 0: 
        while variation[column][simheight - 1] == 0 and not simheight == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
            simheight -= 1

        if team == "player":
            variation[column][simheight] = 1 # fill said slot with red piece
        elif team == "ai":
            variation[column][simheight] = 2 # fill said slot with yellow piece

        #print("hello world") # debug
        #print(simDepth)

        return(variation) # returns success/fail based on whether the slot is a valid move
    else:
        return("fail") # if added coin is in an already full column, it cannot be placed, so function returns "fail"



def mapVariations(board, mapTeam, runDepth): # calculates every possible next move given a board state
    global permutations

    for testCol in range(0,7): # runs across every column
        testBoard = board
        #print("three") # debug
        if checkIfFull(testBoard) == False:
            simState = runAddCoin(column=testCol, variation=testBoard, team=mapTeam, simDepth=runDepth) # runs the runAddCoin functions for every column
            if not simState == "fail": # excludes columns where the next move would exit the top of the board
                permutations += 1
                gameStateLibrary[nodeDepth+1].append(simState) # appends the simState to the library, inside the next nodeDepth
 


def simulate(depth): # runs the mapVariations functions for every board state in a certain nodeDepth
    #global testBoard
    global gameStateLibrary

    gameStateLibrary.append([]) # appends a placeholder in the position of the next nodeDepth
    print(depth)
    #print(gameStateLibrary)
    #print(gameStateLibrary[depth])
    #print("zero") # debug
    for variation in gameStateLibrary[depth]:
        #print("one") # debug

        if depth % 2 == 0:
            simTeam = "ai"
        else:
            simTeam = "player"

        mapVariations(board=variation, mapTeam=simTeam, runDepth=depth) # runs the mapVariations function if the simLevel limit is not reached



def simulateTree(): # head function for branch simulation
    global nodeDepth
    nodeDepth = 0
    for nodeDepth in range(simLevel): # runs the simulate function for every nodeDepth to the limit
        simulate(depth=nodeDepth)



def aiTest(board): # master function, cues tree simulation and minimax algorithm
    global gameStateLibrary

    #print(board)
    gameStateLibrary = [[]]
    gameStateLibrary[0].append(board) # primes simulation with zeroeth nodeDepth, which is the current board state
    
    print(gameStateLibrary) # debug

    simulateTree()
    print(gameStateLibrary)
    print(permutations)

    aiMove = rand.randint(0,6) # test

    time.sleep(0.2)
    #print(numAgentsTotal) # debug

    return(aiMove)



def aiPlay():
    time.sleep(0)

###### PSEUDOCODE ######

# spawns a simulation agent (which recursively spawns 7 more, etc.)

# once simulation is finished, the scoring script runs through every end state and assigns a numerical score (my score - opp score)

# minimax algorithm then runs, working its way up the tree until all 7 choices have a score assigned

# chooses the highest score (technically part of minimax)

# returns choice to main