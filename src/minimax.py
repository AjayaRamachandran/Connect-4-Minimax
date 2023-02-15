###### IMPORT ######
import random as rand
import time

###### VARIABLES ######
simLevel = 10
numAgentsTotal = 0



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


class simAgent:
    def __init__(self):
        None
    
    def simulate(self, nodeDepth, boardState):
        global numAgentsTotal

        if nodeDepth == simLevel:
            None
        else:
            #numAgentsTotal += 1
            print(nodeDepth)
            if nodeDepth % 2 == 1:
                simTeam = "ai"
            else:
                simTeam = "player"
            testCol = 1
            testBoard = boardState

            for testCol in range(0,7):
                simState = runAddCoin(column=testCol, testBoard=testBoard, team=simTeam)
                if not simState == "fail":
                    agent = simAgent()
                    agent.simulate(nodeDepth=nodeDepth+1, boardState=testBoard)

        


def aiTest(board):
    global numAgentsTotal

    aiMove = rand.randint(0,6)
    agent1 = simAgent()
    #aiMove = agent1.simulate(nodeDepth=1, boardState=board)
    agent1.simulate(1, board)
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