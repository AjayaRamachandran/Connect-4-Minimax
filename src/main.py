###### IMPORT ######
import pygame
import time

import minimax
###### IMAGES ######
None

###### SETUP ######
pygame.init()

windowSize = (500, 500)

pygame.display.set_caption("Connect 4") # Sets title of window
screen = pygame.display.set_mode(windowSize) # Sets the dimensions of the window to the windowSize

tempDropX = 0
graphicsDropX = 0

clickedStatus = 0

coinColor1 = (255, 0, 0)
coinColor2 = (255, 255, 0)
boardColor = (0, 0, 255)
emptyColor = (0, 0, 0)

fps = 144
clock = pygame.time.Clock()

gameBoard = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
bhe = 70 # board horizontal edges, recorded in pixels from edge
bve = 100 # board vertical edges, recorded in pixels from edge


#pygame.display.set_icon(None)

###### CLASSES ######
class Background:
    def __init__(self, image):
        self.image = pygame.image.load(image)

###### FUNCTIONS ######

def drawBoard(): # draws game state
    # draws plain blue board, with dimensions based on window width
    pygame.draw.polygon(screen, boardColor, [(bhe, bve),(windowSize[0] - bhe,  bve),(windowSize[0] - bhe, windowSize[1] - bve),(bhe ,windowSize[1] - bve)], width=0)

    for h in range(7):
        for v in range(6):
            if gameBoard[h][v] == 0:
                pygame.draw.circle(screen, emptyColor, (100 + h*50, 375 - v*50), 15, 0)
            elif gameBoard[h][v] == 1:
                pygame.draw.circle(screen, coinColor1, (100 + h*50, 375 - v*50), 15, 0)
            elif gameBoard[h][v] == 2:
                pygame.draw.circle(screen, coinColor2, (100 + h*50, 375 - v*50), 15, 0)


def addCoin(team): # function to refresh the board after a player/opponent's click
    height = 5
    while gameBoard[dropColumn][height - 1] == 0 and not height == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
        height -= 1

    if team == "player":
        gameBoard[dropColumn][height] = 1 # fill said slot with red piece
    elif team == "ai":
        gameBoard[dropColumn][height] = 2 # fill said slot with yellow piece

def renderNextCoin():
    pygame.draw.circle(screen, coinColor1, (tempDropX, 60), 15, 0)

def aiTurn():
    global dropColumn
    dropColumn = minimax.aiPlay()
    print(dropColumn)

    addCoin("ai")



###### MAINLOOP ######
running = True # Runs the game loop
while running:
    screen.fill(emptyColor)
    drawBoard()

    for event in pygame.event.get(): # Checks if program is quit, if so stops the code
        if event.type == pygame.QUIT:
            running = False

    if clickedStatus == 0: # if the turn has yet to be played, then the next coin will follow the mouse x until mouse clicked
        tempDropX = round((pygame.mouse.get_pos()[0]) / 50) * 50

        if tempDropX < 100: # checks for board bounds (7 columns)
            tempDropX = 100
        elif tempDropX > 400:
            tempDropX = 400
        
        dropColumn = int(tempDropX / 50 - 2) # turns tempDropX into an integer which represents the column that the mouse is hovering over
        #print(dropColumn)

        #graphicsDropX = graphicsDropX + (tempDropX - graphicsDropX) * 0.1

        renderNextCoin()
        #print(tempDropX[0])
        
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1: # if the mouse is pressed, change click status to turn can play out
            addCoin("player")
            
            clickedStatus = 1



    if clickedStatus == 1:
        aiTurn()
        clickedStatus = 0
    
    #print(clickedStatus)

    # runs framerate wait time
    clock.tick(fps)
    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()





