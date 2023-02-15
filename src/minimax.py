###### IMPORT ######
import random as rand
import time

###### VARIABLES ######
simLevel = 10
treeCoords = None
gameStateLibrary = []
nodeDepth = 1


###### FUNCTIONS ######

def runAddCoin(column, testBoard, team):
    height = 5
    
    if testBoard[column][height] == 0:
        while testBoard[column][height - 1] == 0 and not height == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
            height -= 1

        if team == "player":
            testBoard[column][height] = 1 # fill said slot with red piece
        elif team == "ai":
            testBoard[column][height] = 2 # fill said slot with yellow piece

        return(testBoard) # returns success/fail based on whether the slot is a valid move
    else:
        return("fail")

 
def simulate(nodeDepth):

    for variation in gameStateLibrary[nodeDepth]:

        if nodeDepth == simLevel:
            None
        else:
            print(nodeDepth)
            if nodeDepth % 2 == 1:
                simTeam = "ai"
            else:
                simTeam = "player"
            testCol = 1
            
            gameStateLibrary.append([])

            for testCol in range(0,7):
                simState = runAddCoin(column=testCol, testBoard=variation, team=simTeam)
                if not simState == "fail":
                    gameStateLibrary[nodeDepth+1].append([simState])

def simulateTree():
    global nodeDepth
    nodeDepth = 1
    for iter in range(simLevel):
        simulate(nodeDepth=nodeDepth)
        nodeDepth += 1

        


def aiTest(board):
    global numAgentsTotal

    aiMove = rand.randint(0,6)

    time.sleep(1)
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