###### IMPORT ######
import random as rand
from math import *
import copy

###### SETUP ######
lookupTable = []

###### FUNCTIONS ######

# Preface! In this module, a "state" is just a nested list that represents a game state, whereas a "node" is a tuple that has a game state as well as the minimax-calculated
# "best" child (column) to search, given that parent.

def add(childNode):
    if not childNode in lookupTable:
        lookupTable.append(childNode)


def compareTables(state1, state2): # compares two game states to see how similar they are (how many of the cell states are shared)
    diff = 0
    for col in range(len(state1)):
        for row in range(len(state1[col])):
            if state1[col][row] != state2[col][row]:
                if state1[col][row] != 0 and state2[col][row] != 0:
                    diff += 0.8 # if in one game state we have a yellow coin, and the other we have red, they're different, but not THAT different
                else:
                    diff += 1 # if in one game state we have a coin and in the other no coin, the two are MORE different than if they both had coins and just diff colors

    return diff # return the total difference between two game states -- larger if the states are more different


def getNearest(gameState):
    global equallyBestStates
    diffTable = []
    for state in lookupTable: # goes through every game state in the table, gives each one a numerical value based on how close it is to the input state
        diffTable.append(compareTables(state[0], gameState))

    equallyBestStates = []
    bestScore = min(diffTable)
    for index in range(len(diffTable)):
        if diffTable[index] == bestScore:
            equallyBestStates.append(lookupTable[index])

    #for item in equallyBestStates:
        #print(item)

    
    numNonZeros = 0
    for item in range(len(equallyBestStates)):
        if equallyBestStates[item][1] != 0:
            numNonZeros += 1
    if numNonZeros == 0:
        #print("all equallyBestStates have a column # of 0")
        return -1
    


    #print(equallyBestStates)
    for column in [3, 4, 2, 5, 1, 6, 0]: # bank of the correct order to search columns in
        for state in equallyBestStates: # runs through all the game states with the same (minimum) diff score
            if state[1] == column: # finds the game state that has a column closest to the middle
                closestGameNode = state
                return closestGameNode # returns the game state that is the closest to the input state and has a suggested move close to the middle - in some cases this may be the input state itself
    


def optimizedChoose(childState):
    if lookupTable == []:
        return -1
    else:
        copiedChildState = copy.deepcopy(childState)
        choice = getNearest(copiedChildState)
        if choice == None:
            for item in equallyBestStates:
                print(item)
        if choice == -1:
            return choice
        else:
            return choice[1]

#print(compareTables([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],[[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]))