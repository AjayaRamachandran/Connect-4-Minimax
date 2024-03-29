###### IMPORT ######
import pygame
import time

import minimax
import windetection
import transpositiontable
import statepackager as spau # stands for [S]tate [P]ackage [A]nd [U]npackage
###### IMAGES ######
None

###### SETUP ######
pygame.init()

windowSize = (500, 500)

pygame.display.set_caption("Connect 4") # Sets title of window
screen = pygame.display.set_mode(windowSize) # Sets the dimensions of the window to the windowSize
font = pygame.font.Font(None, 36)

tempDropX = 0
graphicsDropX = 0

clickedStatus = 0

coinColor1 = (255, 0, 0)
coinColor2 = (255, 255, 0)
boardColor = (0, 0, 255)
emptyColor = (0, 0, 0)

fps = 60
clock = pygame.time.Clock()

gameBoard = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
winCells = [[]]
boardWidth = 7
boardHeight = 6

bhe = 70 # board horizontal edges, recorded in pixels from edge
bve = 100 # board vertical edges, recorded in pixels from edge


###### CLASSES ######
class Background:
    def __init__(self, image):
        self.image = pygame.image.load(image)

###### FUNCTIONS ######

def drawBoard(): # draws game state
    # draws plain blue board, with dimensions based on window width
    pygame.draw.polygon(screen, boardColor, [(bhe, bve),(windowSize[0] - bhe,  bve),(windowSize[0] - bhe, windowSize[1] - bve),(bhe ,windowSize[1] - bve)], width=0)

    for h in range(boardWidth):
        for v in range(boardHeight):
            if gameBoard[h][v] == 0:
                pygame.draw.circle(screen, emptyColor, (100 + h*50, 375 - v*50), 15, 0)
            elif gameBoard[h][v] == 1:
                pygame.draw.circle(screen, coinColor1, (100 + h*50, 375 - v*50), 15, 0)
            elif gameBoard[h][v] == 2:
                pygame.draw.circle(screen, coinColor2, (100 + h*50, 375 - v*50), 15, 0)

    #print(winCells)
    if isinstance(winCells, list) and len(winCells) == 4:
        for h in range(boardWidth):
            for v in range(boardHeight):
                if [h, v] in winCells:
                    pygame.draw.line(screen, emptyColor, (100 + h*50 + 6, 375 - v*50 - 6), (100 + h*50 - 6, 375 - v*50 + 6), 5)
                    pygame.draw.line(screen, emptyColor, (100 + h*50 + 6, 375 - v*50 + 6), (100 + h*50 - 6, 375 - v*50 - 6), 5)
        if gameScore <= -1:
            text = font.render("Yellow (AI) has won", True, coinColor2)
            text_rect = (130, 430)
            screen.blit(text, text_rect)
        if gameScore >= 2:
            text = font.render("Red (player) has won", True, coinColor1)
            text_rect = (130, 430)
            screen.blit(text, text_rect)


def addCoin(team, column): # function to refresh the board after a player/opponent's click
    height = boardHeight - 1
    teamCopy = team
    columnCopy = column
    global gameBoard

    if gameBoard[columnCopy][height] == 0 or team == "ai": # checks if stack is filled, if so does not let player go there
        while gameBoard[columnCopy][height - 1] == 0 and not height == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
            height -= 1

        if teamCopy == "player":
            gameBoard[columnCopy][height] = 1 # fill said slot with red piece
        elif teamCopy == "ai":
            gameBoard[columnCopy][height] = 2 # fill said slot with yellow piece

        return("success") # returns success/fail based on whether the slot is a valid move
    else:
        return("fail")


def renderNextCoin():
    pygame.draw.circle(screen, coinColor1, (graphicsDropX, 60), 15, 0) # renders a preview coin where the mouse is hovering


def aiTurn(): # outsources actual ai play to the minimax module "minimax.py"
    dropColumn = minimax.aiPlay(board=gameBoard)
    print("AI chose column: " + str(dropColumn))
    if dropColumn != "None":
        addCoin(team="ai", column=dropColumn)


def runTime(mouseClicked): # part of the game loop that runs always, even if the mouse is clicked
    global clickedStatus, graphicsDropX, dropColumn

    screen.fill(emptyColor)
    drawBoard()

    if clickedStatus == 0: # if the turn has yet to be played, then the next coin will follow the mouse x until mouse clicked
        tempDropX = round((pygame.mouse.get_pos()[0]) / 50) * 50

        if tempDropX < 100: # checks for board bounds (7 columns)
            tempDropX = 100
        elif tempDropX > 400:
            tempDropX = 400
        
        dropColumn = int(tempDropX / 50 - 2) # turns tempDropX into an integer which represents the column that the mouse is hovering over

        graphicsDropX = graphicsDropX + (tempDropX - graphicsDropX) * 0.3

        renderNextCoin()
        
        if mouseClicked == 1:
            if pygame.mouse.get_pressed(num_buttons=3)[0] == 1: # if the mouse is pressed, change click status to turn can play out
                None

    # runs framerate wait time
    clock.tick(fps)
    # Update the screen
    pygame.display.update()


###### MAINLOOP ######
running = True # Runs the game loop
while running:
    runTime(0)
    for event in pygame.event.get(): # Checks if program is quit, if so stops the code
        if event.type == pygame.QUIT:
            running = False

    # if player has clicked their mouse, we run a varied version of the gameloop until they have let go of their mouse.
    # normally, the gameloop will check to see if the mouse is pressed and if so place a coin, but we run the gameloop without this.
    # previously, this was a time.sleep() function but that causes the whole program to freeze for a second and is very annoying.
    # now, we're essentially waiting for the mouse to unpress WHILE KEEPING THE GAMELOOP RUNNING.
    if pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
        while pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
            runTime(1)

            for event in pygame.event.get(): # Checks if program is quit, if so stops the code
                if event.type == pygame.QUIT:
                    running = False
        
        if windetection.mainRun(gameBoard, "tree") == 0:
            if addCoin(team="player", column=dropColumn) == "success": # only processes as a valid move if "success" returns
                drawBoard()
                pygame.display.update()
                gameScore = windetection.mainRun(gameBoard, "tree")

                print("-------------------------------------------------------------------")
                if gameScore != 2:
                    aiTurn()
                    print("Game state HASH: " + spau.package(gameBoard))
                
                print("Current game score: " + str(gameScore))

                gameScore = windetection.mainRun(gameBoard, "tree")
                winCells = windetection.mainRun(gameBoard, "main")

                if gameScore == 2:
                    print("The Player has won")
                    print("The winning cells are: " + str(winCells))
                elif gameScore == -1:
                    print("The AI has won")
                    print("The winning cells are: " + str(winCells))
        
# Quit Pygame
pygame.quit()