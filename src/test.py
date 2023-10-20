###### IMPORT ######
import pygame
import time

import minimax
import windetection
import transpositiontable
import statepackager as spau

###### TEST ######

'''
print(windetection.mainRun([[0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0]]))


print(windetection.mainRun(spau.unpackage("aaJa61Q9N1N11a", width=7, height=6)))

for column in spau.unpackage("aaJa61Q9N1N11a", width=7, height=6):
    print(column)


for Xoffset in range(3, -1, -1):
    print(Xoffset)

for Xoffset in range(4):
    print(Xoffset)
    '''
print([[5, 0], [4, 1], [3, 2], [2, 3]] is list)