###### IMPORT ######
import random as rand
import time
import copy

###### VARIABLES ######
simLevel = 5
treeCoords = None
gameStateLibrary = []
gameIndexLibrary = []
gameDepthLibrary = []

bufferLevel = []
bufferPaths = []

nodeDepth = 0
pathToBranch = 0
permutations = 0
testBoard = []

pathToBranch = None
###### FUNCTIONS ######

def checkIfFull(sampleBoard):
    notFull = True
    sampleBoardCopy = sampleBoard
    #print(sampleBoardCopy)

    for column in sampleBoardCopy:
        for row in column:
            if row == 0:
                notFull = False

    return(notFull)



def simAddCoin(column, variation, team): # simulates the placing of a coin in a certain column then returns the new gameState
    simheight = 5
    variationCopy = copy.deepcopy(variation)
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



def mapVariations(board, mapTeam, runDepth, path): # calculates every possible next move given a board state
    mapTeamCopy = mapTeam
    runDepthCopy = runDepth
    global pathToBranch
    pathToBranch = path
    
    boardCopy = copy.deepcopy(board)

    for testCol in range(7): # runs across every column

        testBoard = boardCopy
        pathToBranchCopy = pathToBranch

        if checkIfFull(testBoard) == False: # if the board is full, don't run this bit
            
            simState = simAddCoin(column=testCol, variation=testBoard, team=mapTeamCopy) # runs the simAddCoin functions for every column
            #print(simState)

            if not simState == "fail": # excludes columns where the next move would exit the top of the board

                if str(pathToBranchCopy) == "None":
                    pathToBranchCopy = str(testCol)
                else:
                    pathToBranchCopy = str(pathToBranchCopy) + str(testCol)

                gameStateLibrary.append(simState) # appends the simState to the library
                gameIndexLibrary.append(pathToBranchCopy)
                gameDepthLibrary.append(runDepthCopy)
 


def simulate(depth): # runs the mapVariations functions for every board state in a certain nodeDepth
    #global testBoard
    global nodeDepth
    global gameStateLibrary
    global bufferLevel
    global bufferPaths

    for version in range(len(gameStateLibrary)):
        if gameDepthLibrary[version] == nodeDepth-1:
            bufferLevel.append(copy.deepcopy(gameStateLibrary[version]))
            bufferPaths.append(gameIndexLibrary[version])


    for variation in range(len(bufferLevel)):
        currentLevel = bufferLevel[variation]
        currentPath = bufferPaths[variation]

        if depth % 2 == 0:
            simTeam = "ai"
        else:
            simTeam = "player"
        

        mapVariations(board=currentLevel, mapTeam=simTeam, runDepth=nodeDepth, path=currentPath) # runs the mapVariations function if the simLevel limit is not reached
    
    #oldBufferLevel = copy.deepcopy(bufferLevel)
    bufferLevel = []



def simulateTree(): # head function for branch simulation
    global nodeDepth
    nodeDepth = 0
    for depth in range(simLevel): # runs the simulate function for every nodeDepth to the limit
        nodeDepth = depth + 1
        simulate(depth=nodeDepth)



def aiTest(board): # master function, cues tree simulation and minimax algorithm
    global gameStateLibrary
    global gameIndexLibrary
    global gameDepthLibrary
    global pathToBranch
    global permutations

    #permutations = 0


    boardCopy = copy.deepcopy(board)
    pathToBranch = None
    gameStateLibrary.append(boardCopy) # primes simulation with initial state, which is the current board state
    #bufferLevel.append(boardCopy) # sets the current board state to the only object within the current buffer, which is access when making variations



    gameIndexLibrary.append(0)
    gameDepthLibrary.append(0)
    
    simulateTree()
    print(len(gameIndexLibrary))
    #print(gameIndexLibrary)


    gameStateLibrary = []
    gameIndexLibrary = []
    gameDepthLibrary = []

    aiMove = rand.randint(0,6) # test

    time.sleep(0.2)
    #print(permutations)
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