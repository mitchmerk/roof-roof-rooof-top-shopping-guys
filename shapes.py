#Final Project
import pygame 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#def draw_middle(screen, x, y):
    #pygame.draw.line(screen, WHITE, [150 + x, 33 + y], [150 + x, 3 + y], 2)

    
#Setup 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pong")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    #draw_middle(screen, x_coord, y_coord)
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    pygame.draw.line(screen, WHITE, [350, 0], [350, 550], 2)
    pygame.draw.line(screen, WHITE, [2, 180], [2, 300], 2)
    pygame.draw.line(screen, WHITE, [695, 180], [695, 300], 2)
    pygame.draw.polygon(screen, WHITE, [[100,100], [0, 0], [0, 135], [0,200], [50,150]], 0)


 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
