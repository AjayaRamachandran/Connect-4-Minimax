###### IMPORT ######

import copy
from math import *
import time
import random as rand


###### VARIABLES ######
charString = "abcdefghiJKLMNOPQR123456789"

###### FUNCTIONS ######
def package(gameState):
    string = ""
    flattenedState = [num for elem in gameState for num in elem]

    for digitSet in range(int(len(flattenedState) / 3)):
        setValue = flattenedState[digitSet * 3] * 9 + flattenedState[digitSet * 3 + 1] * 3 + flattenedState[digitSet * 3 + 2] * 1
        string = string + charString[setValue]

    return string

def unpackage(hash, width, height):
    flattenedState = []

    for hashIndex in range(len(hash)):
        char = hash[hashIndex]
        charIndex = charString.index(char)

        digit1 = floor(charIndex / 9)
        digit2 = floor((charIndex % 9) / 3)
        digit3 = charIndex % 3

        flattenedState.append(digit1)
        flattenedState.append(digit2)
        flattenedState.append(digit3)

    state = []
    for col in range(width):
        rowData = []
        for row in range(height):
            rowData.append(flattenedState[col * (width-1) + row])
        state.append(rowData)

    return state

def testList():
    myList = []
    for i in range(7):
        row = []
        for a in range(6):
            row.append(rand.randint(0,2))
        myList.append(row)

    return myList


'''
epicList = testList()
packagedAndUnpackagedEpicList = unpackage(package(epicList), width=7, height=6)

print(epicList)
print(package(epicList))
print(packagedAndUnpackagedEpicList)
'''