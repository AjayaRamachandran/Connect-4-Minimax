###### IMPORT ######
import pygame
import time

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

fps = 144
clock = pygame.time.Clock()

gameBoard = ((0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0),(0, 0, 0, 0, 0, 0))

#pygame.display.set_icon(None)

###### CLASSES ######
class Background:
    def __init__(self, image):
        self.image = pygame.image.load(image)

###### FUNCTIONS ######
def refreshBoard(): # function to refresh the board after a player/opponent's click
    height = 5
    while gameBoard[dropColumn][height] == 0: # repeatedly checks in downward succession for the first filled coin of the column, akin to gravity
        height -= 1

    height += 1 # previous value represents first filled row, increment by 1 to get last empty row

    gameBoard[dropColumn][height] = 1 # fill said slot

def renderNextCoin():
    pygame.draw.circle(screen, coinColor1, (tempDropX, 60), 15, 0)

def aiTurn():
    time.sleep(1)



###### MAINLOOP ######
running = True # Runs the game loop
while running:
    screen.fill((0, 0, 0))
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
        print(dropColumn)

        #graphicsDropX = graphicsDropX + (tempDropX - graphicsDropX) * 0.1

        renderNextCoin()
        #print(tempDropX[0])
        
        if pygame.mouse.get_pressed(num_buttons=3)[0] == 1: # if the mouse is pressed, change click status to turn can play out
            refreshBoard()
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





