###### IMPORT ######
import random as rand
import time
import copy
import windetection

###### VARIABLES ######
simLevel = 2
treeCoords = None
gameStateLibrary = [] # large list of all possible game states, simulated from current state
gameIndexLibrary = [] # paired large list of game indexes (string of moves made to get there)
gameDepthLibrary = [] # paired large list of game depths, for easy searching through depth levels later

gameStatesOfDepth = []
gameIndexesOfDepth = []

nodeDepth = 0
pathToBranch = 0
permutations = 0
testBoard = []

pathToBranch = None
###### FUNCTIONS ######

def checkIfFull(sampleBoard):
    full = True
    sampleBoardCopy = copy.deepcopy(sampleBoard)
    #print(sampleBoardCopy)

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
    for testCol in range(7): # runs across every column
        testBoard = copy.deepcopy(boardCopy)
        if checkIfFull(testBoard) == False: # if the board is full, don't run this bit
            simState = simAddCoin(column=testCol, variation=testBoard, team=team) # runs the simAddCoin functions for every column
            if not simState == "fail": # excludes columns where the next move would exit the top of the board
                children.append(copy.deepcopy(simState))
                if depth == 0:
                    score = windetection.mainRun(simState)
                    listOfChildrenColumns.append(testCol)
                    listOfChildrenScores.append(score)

            #print(simState)
    
    return children


def minimax(state, depth, alpha, beta, maximizingPlayer):
    global iters
    iters += 1
    gameState = copy.deepcopy(state)
    #print(gameState)

    if depth == simLevel or gameOver:
        return windetection.mainRun(gameState)
    
    if maximizingPlayer:
        maxEval = -100000
        for child in simulateChildren(gameState, depth % 2 == 0, depth):
            #print(child)
            eval = minimax(child, depth+1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    
    else:
        minEval = 100000
        for child in simulateChildren(gameState, depth % 2 == 0, depth):
            #print(child)
            eval = minimax(child, depth+1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval
    




def aiTest(board): # master function, cues tree simulation and minimax algorithm
    global boardCopy
    global listOfChildrenColumns
    global listOfChildrenScores
    global iters
    global gameOver

    boardCopy = copy.deepcopy(board)
    listOfChildrenColumns = []
    listOfChildrenScores = []
    iters = 0
    gameOver = windetection.mainRun(gameState) != 0
    minimax(boardCopy, 0, -100000, 100000, False)
    print(iters)
    print(listOfChildrenScores)
    if len(listOfChildrenScores) > 0:
        aiMove = listOfChildrenColumns[listOfChildrenScores.index(max(listOfChildrenScores))]
    else:
        aiMove = "None"


    #aiMove = rand.randint(0,6) # test

    return(aiMove)



def aiPlay():
    time.sleep(0)


###### PSEUDOCODE ######

#    recursively creates generations of simulation, using all the elements of the previous simulation as reference points

#    with each new generation's element, a numerical "tag" identifier is attached, which is used to find specific game
#    states in the future based on moves used to get there

#    all "bottom-rung" game states (max moves used to get there) are then scored on how beneficial they are using some
#    weightages

#    once every bottom-rung game state is scored, the minimax algorithm is applied, and traced back up to the top to pick
#    the next best move



###### MONTE CARLO SIMULATION NOTES ######

#    scoring function uses a heuristic method with a specific heuristic value, which is determined by the types of situations
#    present in the game state

#    most methods online use an arbitrary method of determining the heuristic value, from power-systems (2^length of stack) and
#    such. to make the best of the limited searchability this algorithm has, I will employ a monte-carlo simulation with
#    hundreds of bots playing thousands of games with one another, which will affect the prime weightages if they win.

#    using a simulation to methodically converge upon the heuristic weights as opposed to choosing an arbitrary heuristic
#    function should make the bots as effective as possible with their limited search range