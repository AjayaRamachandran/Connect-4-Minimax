###### IMPORT ######
import random as rand
import time

###### FUNCTIONS ######
def aiTest():
    aiMove = rand.randint(0,6)

    return(aiMove)

def aiPlay():
    time.sleep(0)

###### PSEUDOCODE ######

# spawns a simulation agent (which recursively spawns 7 more, etc.)
    
# once simulation is finished, the scoring script runs through every end state and assigns a numerical score (my score - opp score)

# minimax algorithm then runs, working its way up the tree until all 7 choices have a score assigned

# chooses the highest score (technically part of minimax)

# returns choice to main