###### IMPORT ######
import random as rand
import time

###### VARIABLES ######
simLevel = 4
treeCoords = None
gameStateLibrary = [[]]
nodeDepth = 1
permutations = 0
testBoard = []

###### FUNCTIONS ######

def runAddCoin(column, variation, team):
    simheight = 5

    #print(testBoard)
    if variation[column][simheight] == 0:
        while variation[column][simheight - 1] == 0 and not simheight == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
            simheight -= 1

        if team == "player":
            variation[column][simheight] = 1 # fill said slot with red piece
        elif team == "ai":
            variation[column][simheight] = 2 # fill said slot with yellow piece

        return(variation) # returns success/fail based on whether the slot is a valid move
    else:
        return("fail")

 
def simulate(nodeDepth):
    global permutations
    global testBoard

    print(nodeDepth)
    for variation in gameStateLibrary[nodeDepth]:

        if nodeDepth == simLevel:
            None
        else:
            #print(nodeDepth)
            if nodeDepth % 2 == 0:
                simTeam = "ai"
            else:
                simTeam = "player"
            testCol = 1
            
            gameStateLibrary.append([])

            for testCol in range(0,7):
                testBoard = variation

                simState = runAddCoin(testCol, variation, simTeam)
                if not simState == "fail":
                    permutations += 1
                    gameStateLibrary[nodeDepth+1] = [simState]

def simulateTree():
    global nodeDepth
    nodeDepth = 0
    for iter in range(simLevel):
        simulate(nodeDepth=nodeDepth)
        nodeDepth += 1

        


def aiTest(board):
    gameStateLibrary[0].append(board)
    #print(board)
    print(gameStateLibrary)

    simulateTree()
    #print(permutations)

    aiMove = rand.randint(0,6)

    time.sleep(0.2)
    #print(numAgentsTotal)

    return(aiMove)

def aiPlay():
    time.sleep(0)

###### PSEUDOCODE ######

# spawns a simulation agent (which recursively spawns 7 more, etc.)

# once simulation is finished, the scoring script runs through every end state and assigns a numerical score (my score - opp score)

# minimax algorithm then runs, working its way up the tree until all 7 choices have a score assigned

# chooses the highest score (technically part of minimax)

# returns choice to main