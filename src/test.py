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
'''

print(windetection.mainRun(spau.unpackage("aaJa61Q9N1N11a", width=7, height=6)))
print(spau.unpackage("aaJa61Q9N1N11a", width=7, height=6))

'''
for Xoffset in range(3, -1, -1):
    print(Xoffset)

for Xoffset in range(4):
    print(Xoffset)
    '''

