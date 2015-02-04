import math
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (800, 450)
screen = pygame.display.set_mode(size)

# Load the background image
background_image = pygame.image.load("cartoony.jpg").convert()

# Load the spaceship, then make the background transparent
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)

# Load the laser sound
click_sound = pygame.mixer.Sound("laser5.ogg")

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    screen.blit(background_image, [0, 0])

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
     
    # Copy image to screen:
    screen.blit(player_image, [x, y])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


# NOTE: create a ball class to load paper ball image


'''
FOR BALL CLASS - to load an image (exaple)

def __init__(self):
    """ Graphic Sprite Constructor. """
 
    # Call the parent class (Sprite) constructor
    super().__init__()
 
    # Load the image
    self.image = pygame.image.load("player.png").convert()
 
    # Set our transparent color
    self.image.set_colorkey(WHITE)
'''