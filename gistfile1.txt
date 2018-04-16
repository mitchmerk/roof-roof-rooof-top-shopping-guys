# Ben Weidner, Ryan Miller, Mitch Merkowsky
# 4/11/2018
# PONG+PLUS

import pygame
import random
import math

# Define some colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
YELLOW = [255, 255, 0]

# Classes
class Paddle(): # paddle class
    def __init__(self, x_pos, y_pos, color):
        # --- Class Attributes ---

        # Height and Width
        height = 50
        width = 15
        
        # Position
        self.pos = [x_pos, y_pos] # X/Y Position

        # Size
        self.size = [width, height] # Height/Width

        # Position Change (Movement)
        self.change = 0 # Change in Y position

        # Color
        self.col = color # Color

    def draw(self, screen): # draw method to draw the paddle
        pygame.draw.rect(screen, self.col, [self.pos, self.size])

    def move(self): # move method (moves paddles up and down)
        self.pos[1] += self.change
        if self.pos[1] > 350:
            self.pos[1] = 350
        elif self.pos[1] < 101:
            self.pos[1] = 101

class Ball(): # ball class
    def __init__(self, x_pos, y_pos, size, angle):
        # --- Class Attributes ---
        # Width and Height of the boundaries
        height = 500
        width = 750
        
        # Set the initial X/Y change
        x_change = 1
        y_change = 1
        chooser = random.randint(0, 1)
        if x_change == 0:
            if chooser == 0:
                x_change = 1
            elif chooser == 1:
                x_change = -1
        if y_change == 0:
            if chooser == 0:
                y_change = 1
            elif chooser == 1:
                y_change = -1
        
        # Position
        self.pos = [x_pos, y_pos] # X/Y Position

        # Size
        self.size = size # Height/Width

        # Angle
        self.angle = angle # Angle

        # Speed
        self.speed = 2.5 # Speed

    def draw(self, screen): # draw method to draw the paddle
        pygame.draw.circle(screen, YELLOW, (int(self.pos[0]), int(self.pos[1])), self.size)

    def move(self): # move method (moves paddles up and down)
        self.pos[0] += math.sin(self.angle) * self.speed
        self.pos[1] += math.cos(self.angle) * self.speed
            
    #def bounce(self): # bounces the ball off the walls/paddles
        # Paddle Bouncing
        #if self.pos[0] > width - self.size:
           # self.x = 2 * (width - self.size) - self.pos[0]
           # self.angle = - self.angle

       # elif self.pos[0] < self.size:
            #self.pos[0]

        

def walls(): # draws the walls
    # Top Wall
    pygame.draw.polygon(screen, WHITE, [[0, 0], [750, 0], [750, 100], [700, 100], [650, 50], [100, 50], [50, 100], [0 , 100]])
    # Bottom Wall
    pygame.draw.polygon(screen, WHITE, [[0, 500], [750, 500], [750, 400], [700, 400], [650, 450], [100, 450], [50, 400], [0 , 400]])
 
    
pygame.init()

# Set the width and height of the screen [width, height]
size = (750, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("PONG+PLUS")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Instances of the Paddle class
player_one = Paddle(35, 225, BLUE)
player_two = Paddle(700, 225, RED)
direction = random.uniform(0, math.pi * 2)
game_ball = Ball(375, 250, 7, direction)

# Paddle Speed
speed = 2

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # PLAYER ONE CONTROLS
        # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_one.change = (speed * -1)
            elif event.key == pygame.K_s:
                player_one.change = speed
 
        # Reset speed when key goes up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_one.change = 0
            elif event.key == pygame.K_s:
                player_one.change = 0


        # PLAYER TWO CONTROLS
        # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_two.change = (speed * -1)
            elif event.key == pygame.K_DOWN:
                player_two.change = speed
 
        # Reset speed when key goes up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_two.change = 0
            elif event.key == pygame.K_DOWN:
                player_two.change = 0
                
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # --- Drawing code should go here
    screen.fill(BLACK)
    
    # Walls
    walls()

    # Paddles
    player_one.draw(screen)
    player_one.move()

    player_two.draw(screen)
    player_two.move()
    
    # Ball
    game_ball.draw(screen)
    game_ball.move()
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
