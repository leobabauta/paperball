import pygame

 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
     
        # Call the parent class (Sprite) constructor
        super(Ball, self).__init__()
     
        # Load the image
        self.image = pygame.image.load("paper20.png").convert()
     
        # Set our transparent color
        self.image.set_colorkey(RED)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect(center=(50,200))
        self.changex = 0
        self.changey = 0
        self.gravity = .025


    def update(self):
        self.rect.x += self.changex
        if self.changex > 0 and self.changex > self.gravity:
            self.changex -= self.gravity
        elif self.changex > 0:
            self.changex = 0

        self.rect.y += self.changey


# Set the width and height of the screen [width, height]
size = (800, 450)
screen = pygame.display.set_mode(size)


# Create a Ball object
paperball = Ball()


# Create a list of every sprite.
all_sprites_list = pygame.sprite.Group()

# Add the ball to the list of sprites
all_sprites_list.add(paperball)


# Load the background image
background_image = pygame.image.load("cartoony.jpg").convert()

# Load the laser sound
click_sound = pygame.mixer.Sound("laser5.ogg")

pygame.display.set_caption("Paperball")
 
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                paperball.changex += 2
            if event.key == pygame.K_2:
                paperball.changex += 4
            if event.key == pygame.K_3:
                paperball.changex += 6
            if event.key == pygame.K_4:
                paperball.changex += 8



    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # Display background
    screen.blit(background_image, [0, 0])

    # Call the update() method for all blocks in the block_list
    all_sprites_list.update()

    # Update & display ball sprite
    all_sprites_list.draw(screen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
