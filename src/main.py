###### IMPORT ######
import pygame

###### SETUP ######
pygame.init()

windowSize = (500, 500)


pygame.display.set_caption("Schemedit v1.0.2") # Sets title of window
screen = pygame.display.set_mode(windowSize) # Sets the dimensions of the window to the windowSize
#pygame.display.set_icon(None)

###### CLASSES ######
class Background:
    def __init__(self, image):
        self.image = pygame.image.load(image)

###### FUNCTIONS ######
        


###### MAINLOOP ######
running = True # Runs the game loop
while running:
    for event in pygame.event.get(): # Checks if program is quit, if so stops the code
        if event.type == pygame.QUIT:
            running = False
            
    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()





