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

# Width and Height of the boundaries
arena_height = 500
arena_width = 750

# Classes


class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        #This randomizes the size of the Obstacle
        randint = random.randint(10, 90)
        self.image = pygame.Surface([randint, randint])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(130, 600)
        self.rect.x = random.randrange(60, 420)
 
    def update(self):
        """ Called each frame. """
 
        # Move block down one pixel
        self.rect.y += 1
 
        # If block is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.reset_pos()
        
class Paddle(pygame.sprite.Sprite): # paddle class
    # Constructor function
    def __init__(self, x_pos, y_pos, color):
        # Call the parent's constructor
        super().__init__()
 
        self.width = 15
        self.height = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        self.rect.x = x_pos
        self.rect.y = y_pos

        self.speed = 3
 
    # Update the player
    def update(self, change_dir):        
        self.change = change_dir
        print(self.change)
        vert_axis_pos = self.change
        # Move y according to the axis. We multiply by 15 to speed up the movement.
        self.rect.y = int(self.rect.y + vert_axis_pos * 3)
 
        # Makes sure the paddle is contained within the borders of the arena
        if self.rect.y > 350:
            self.rect.y = 350
        elif self.rect.y < 101:
            self.rect.y = 101

class Ball(pygame.sprite.Sprite): # ball class
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create the image of the ball
        self.image = pygame.Surface([10, 10])
 
        # Color the ball
        self.image.fill(YELLOW)
 
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()
 
        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        # Speed in pixels per cycle
        self.speed = 0
 
        # Floating point representation of where the ball is
        self.x = 0
        self.y = 0
 
        # Direction of ball in degrees
        self.direction = 0
 
        # Height and width of the ball
        self.width = 7
        self.height = 7
 
        # Set the initial ball speed and position
        self.reset()
 
    def reset(self):
        self.x = 375
        self.y = 250
        self.speed= 3.0
 
        # Direction of ball (in degrees)
        self.direction = random.randrange(-45,45)
 
        # Flip a 'coin'
        if random.randrange(2) == 0 :
            # Reverse ball direction, let the other guy get it first
            self.direction += 90
            self.y = 50
 
    # This function will bounce the ball off a horizontal surface (not a vertical one)
    def bounce(self,diff):
        self.direction = (90 - self.direction) % 360
        self.direction -= diff
 
        # Speed the ball up
        #self.speed *= 1.1
 
    # Update the position of the ball
    def update(self):
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)
 
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
 
        if self.y < 0:
            self.reset()
 
        if self.y > 600:
            self.reset()
 
        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y
 
        # Do we bounce off the left of the screen?
        #if self.x <= 0:
         #   self.direction = (360-self.direction) % 360
 
        # Do we bounce of the right side of the screen?
        #if self.x > self.screenwidth - self.width:
         #   self.direction = (360-self.direction) % 360

        # Do we bounce of the top of the screen?
        #if self.y <= 0:
          #  self.direction = (360 - self.direction) % 360
            
        # Do we bounce of the bottom of the screen?
        #if self.y > self.height - self.screenheight:
         #   self.direction = (360 - self.direction) % 360
            
class Wall(pygame.sprite.Sprite): # draws the walls
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        super().__init__()
        #These values set how much health the players have.
        self.health1 = 550
        
        self.health2= 550
        #These values change the health values.
        self.health_damage = 0

        #These values assign the health to the health bar.
        #self.haelth_change = 

        #self.health1 = self.health_change

        #This assigns the color for player 1 (red).
        self.color = GREEN

        #This assigns the color for player 2(blue).
        self.color2 = GREEN

    #This changes the color to yellow for player 1(red).
    def healthcolor_change(self):
        
        self.color = YELLOW
        
    #This changes the color to red for player 1 (red).  
    def healthcolor_change2(self):

        self.color = RED
        
    def health_change(self,num):
        
        #These are used to deturmin what color the health bar is.
        self.change_health1 = 0

        self.health1 -= num

    def health2_change(self,num):
        self.change_health2 = 0
        
        self.health2 -= num
        
        
    def draw(self, screen):
        # Top Wall
        pygame.draw.polygon(screen, WHITE, [[0, 0], [750, 0], [750, 100], [700, 100], [650, 50], [100, 50], [50, 100], [0 , 100]])
        # Bottom Wall
        pygame.draw.polygon(screen, WHITE, [[0, 500], [750, 500], [750, 400], [700, 400], [650, 450], [100, 450], [50, 400], [0 , 400]])

        #This draws the top health bar.
        pygame.draw.rect(screen, RED, [97,3,556,40], 0)
        pygame.draw.rect(screen, BLACK, [100,5,550,35], 0)

        #This draws the bottom health bar.
        pygame.draw.rect(screen, BLUE, [97,456,556,39], 0)
        pygame.draw.rect(screen, BLACK, [100,458,550,35], 0)

        #==========vvvvHealth Barsvvvv=====================

        #This will draw the health bar for blue.
        pygame.draw.rect(screen, GREEN, [100,458,self.health1,35], 0)


        #This will draw the health bar for red.
        pygame.draw.rect(screen, GREEN, [100,5,550,35], 0)

        #==========^^^^Health Bars^^^^=====================            
        
        
        #This will draw the text for player 1. (BLUE)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("PLAYER 1", True, WHITE)
        screen.blit(text, [340, 465])
        
        #This will draw the text for player 2. (RED)
        text = font.render("PLAYER 2", True, WHITE)
        screen.blit(text, [340, 10])

        #This will draw the top left point box.
        pygame.draw.rect(screen, RED, [2,3,82,40], 0)
        pygame.draw.rect(screen, BLACK, [5,5,76,36], 0)

        #This will draw the bottom right point box.
        pygame.draw.rect(screen, BLUE, [663,456,82,39], 0)
        pygame.draw.rect(screen, BLACK, [665,458,76,35], 0)

        #This will draw the top right sprite box
        pygame.draw.rect(screen, RED, [677,2,66,59], 0)
        pygame.draw.rect(screen, BLACK, [680,5,60,53], 0)

        #This will draw the bottom left sprite box
        pygame.draw.rect(screen,BLUE,[8,435,65,58],0)
        pygame.draw.rect(screen,BLACK,[10,437,60,53],0)

        #This will be for the score for player 2 (red).
        point = score1
        point1 = str(point)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(point1, True, WHITE)
        screen.blit(text, [30, 10])

        #This will be for the score for player 1 (blue).
        point = score2
        point2 = str(point)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(point2, True, WHITE)
        screen.blit(text, [695, 465])

        
score1 = 0
score2 = 0
#This draws the obstacles.
all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
for i in range(3):
    # This represents a block
    block = Block(GREEN)
    # Set a random location for the block
    block.rect.x = random.randrange(475)
    block.rect.y = random.randrange(550)
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
pygame.init()


pygame.init()

# Set the width and height of the screen [width, height]
size = (750, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("PONG+PLUS")
 
# Loop until the user clicks the close button.
exit_game = False
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Instances of the Ball class
game_ball = Ball()

balls = pygame.sprite.Group()
balls.add(game_ball)

# Instances of the Paddle class
player_one = Paddle(35, 225, BLUE)
player_two = Paddle(700, 225, RED)

movingsprites = pygame.sprite.Group()
movingsprites.add(player_one)
movingsprites.add(player_two)
movingsprites.add(game_ball)

player_one_change = 0
player_two_change = 0

# Instances of the Wall class
border = Wall()


# -------- Main Program Loop -----------
while not exit_game:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True

        # PLAYER ONE CONTROLS
        # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_one_change = -1
            elif event.key == pygame.K_s:
                player_one_change = 1
 
        # Reset speed when key goes up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
               player_one_change = 0
            elif event.key == pygame.K_s:
                player_one_change = 0
                
        # PLAYER TWO CONTROLS
        # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_two_change = -1
            elif event.key == pygame.K_DOWN:
                player_two_change = 1
 
        # Reset speed when key goes up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_two_change = 0
            elif event.key == pygame.K_DOWN:
                player_two_change = 0
 
    # --- Screen-clearing code goes here
    screen.fill(WHITE)
    
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # Set the screen's background
    screen.fill(BLACK)

    border.draw(screen)

    if not done:
        # Update the player and ball positions
        player_one.update(player_one_change)
        player_two.update(player_two_change)
        game_ball.update()


    # See if the ball hits the player one paddle
    if pygame.sprite.spritecollide(player_one, balls, False):
        diff = (player_one.rect.x + player_one.height / 2) - (game_ball.rect.x + game_ball.height / 2)
 
        game_ball.bounce(diff)
        score1 += 1
 
    # See if the ball hits the player two paddle
    if pygame.sprite.spritecollide(player_two, balls, False):
        diff = (player_two.rect.x + player_two.height / 2) - (game_ball.rect.x + game_ball.height / 2)
 
        game_ball.bounce(diff)
        score2 += 1
    
    # If the ball goes beyond the screen on the right.
    if game_ball.x > 725 and game_ball.y > 100 and game_ball.y < 380:
        score2 += 1
        border.self_health -= 30
        game_ball.reset

    #If the ball goes beyond the screen on the left. 
    if game_ball.x < 5 and game_ball.y > 100 and game_ball.y < 380:
        score1 += 1
        border.self_health -= 30
        game_ball.reset()
        
    for block in block_list:
        if pygame.sprite.spritecollide(block, balls, False):
            diff = (player_two.rect.x + player_two.height / 2) - (game_ball.rect.x + game_ball.height / 2)
            game_ball.bounce(diff)
        if pygame.sprite.spritecollide(block, balls, False):    
           block.reset_pos()
           
        
    #This will change the color of the health bar for player 1 (blue).
    if border.health1 < 250:
        border.healthcolor_change()

    if border.health1 < 150:
        border.healthcolor_change2()

    if border.health1 <= 0:
        break
        
        
  #This will change the color of the health bar for player 1(red).
    if border.health2 < 250:
        border.healthcolor_change()

    if border.health2 < 150:
        border.healthcolor_change2()

    if border.health2 <= 0:
        break       
    
 
    
    # Draw Everything
    movingsprites.draw(screen)
    all_sprites_list.draw(screen)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
