# Ben Weidner, Ryan Miller, Mitch Merkowsky
# 4/22/2018 v3
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

pygame.init()

music = pygame.mixer.Sound("pong+plus_music.ogg")
bounce_sound = pygame.mixer.Sound("bounce_sound.ogg")
health_drop_sound = pygame.mixer.Sound("health_drop.ogg")
victory_music = pygame.mixer.Sound("Mighty Like Us.ogg")

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
        self.rect.y = random.randrange(80, 400)
        self.rect.x = random.randrange(90, 400)
 
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
    def bounce(self, diff):
        bounce_sound.play()
        self.direction = self.direction % 360
        self.direction -= diff
 
        # Speed the ball up
        self.speed *= 1.01
        
    # Update the position of the ball
    def update(self):
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)
 
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        if self.y < 45:
            self.reset()

        if self.y > 455:
            self.reset()
 
        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y

#This is the class that makes the points,healthbars, Player words, and sprite boxes.
class Wall(pygame.sprite.Sprite): # draws the walls
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        super().__init__()

        #This is where the score is held.
        self.score_p1 = 0

        self.score_p2 = 0

        #These values set how much health the players have.
        self.health1 = 550
        
        self.health2= 550
        
        #This assigns the color for player 1 (red).
        self.color1 = GREEN

        #This assigns the color for player 2(blue).
        self.color2 = GREEN

        #This value deturmins who hit the paddle last.
        self.paddle_last_hit = bool

    #This is what changes the score for player 1.
    def score_change_p1(self,num):
        self.score_p1 += num

    #This is what changes the score for player 2.
    def score_change_p2(self,num):
        self.score_p2 += num
    
    #This changes the color to yellow for player 1(red).
    def healthcolor_change_p1(self):        
        self.color1 = YELLOW
        
    #This changes the color to red for player 1 (red).  
    def healthcolor_change_p1(self):
        self.color1 = RED

    #This changes the color to yellow for player 2 (red).  
    def healthcolor_change_p2(self):
        self.color2 = YELLOW

    #This changes the color to red for player 2 (red).  
    def healthcolor_change_p2(self):
        self.color2 = RED
        
    #This changes the health bar for player 1 (Red).
    def health1_change(self,num):
        self.health1 -= num
        health_drop_sound.play()

    #This changes the health bar for player 2 (Blue).
    def health2_change(self,num):        
        self.health2 -= num
        health_drop_sound.play()
        
    def draw(self, screen):
        #This draws the top health bar.
        pygame.draw.rect(screen, RED, [97,3,556,40], 0)
        pygame.draw.rect(screen, BLACK, [100,5,550,35], 0)

        #This draws the bottom health bar.
        pygame.draw.rect(screen, BLUE, [97,456,556,39], 0)
        pygame.draw.rect(screen, BLACK, [100,458,550,35], 0)

        #This will draw the health bar for blue.
        pygame.draw.rect(screen, self.color1  , [100,458,self.health1,35], 0)

        #This will draw the health bar for red.
        pygame.draw.rect(screen, self.color2, [100,5,self.health2,35], 0)
        
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
        point = self.score_p2
        point1 = str(point)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(point1, True, WHITE)
        screen.blit(text, [30, 10])

        #This will be for the score for player 1 (blue).
        point = self.score_p1
        point2 = str(point)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(point2, True, WHITE)
        screen.blit(text, [695, 465])

class Border(pygame.sprite.Sprite):
    def __init__(self, w, h, x_pos, y_pos):
        # Call the parent's constructor
        super().__init__()
        # set the wall sprite
        self.width = w
        self.height = h
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y_pos
        self.rect.x = x_pos
        
#This is the main program loop. Its so we can loop back to the begining after the game is over.
def main():
    #This draws the obstacles.
    all_sprites_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    for i in range(3):
        # This represents a block
        block = Block(WHITE)
        # Set a random location for the block
        block.rect.x = random.randrange(60, 300)
        block.rect.y = random.randrange(90, 400)
        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)

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
    wall = Wall()

    # Instances of the Border Class
    border_top = Border(750, 50, 0, 0)
    border_bot = Border(750, 50, 0, 450)
    border_top_left = Border(75, 50, 0, 50)
    border_top_right = Border(75, 50, 675, 50)
    border_bot_left = Border(75, 50, 0, 400)
    border_bot_right = Border(75, 50, 675, 400)

    bordersprites = pygame.sprite.Group()
    bordersprites.add(border_top)
    bordersprites.add(border_bot)
    bordersprites.add(border_top_left)
    bordersprites.add(border_bot_left)
    bordersprites.add(border_top_right)
    bordersprites.add(border_bot_right)
    
    music.play(loops = -1)
    # -------- Main Program Loop -----------
    while not exit_game:

        # Sound
        victory_music.stop()
        
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

        bordersprites.draw(screen)
        wall.draw(screen)
        
        if not done:
            # Update the player and ball positions
            player_one.update(player_one_change)
            player_two.update(player_two_change)
            game_ball.update()

        # See if the ball hits the borders
        for boundary in bordersprites:
            if pygame.sprite.spritecollide(boundary, balls, False):
                diff = (boundary.rect.x + boundary.height * 2) - (game_ball.rect.x + game_ball.height * 2)
                game_ball.bounce(diff)

        # See if the ball hits the player one paddle
        if pygame.sprite.spritecollide(player_one, balls, False):
            diff = (player_one.rect.x + player_one.height * 2) - (game_ball.rect.x + game_ball.height * 2)
            game_ball.bounce(diff)
            wall.paddle_last_hit == True
            wall.score_change_p1(5)

        # See if the ball hits the player two paddle
        if pygame.sprite.spritecollide(player_two, balls, False):
            diff = (player_two.rect.x + player_two.height / 2) - (game_ball.rect.x + game_ball.height / 2)
            game_ball.bounce(diff)
            wall.paddle_last_hit == False
            wall.score_change_p2(5)

        # If the ball goes beyond the paddle on the right.
        if game_ball.x > 750:
            wall.score_change_p1(20)
            wall.health2_change(50)
            game_ball.reset()

        #If the ball goes beyond the paddle on the left. 
        if game_ball.x < 0:
            wall.score_change_p2(20)
            wall.health1_change(50)
            game_ball.reset()

        #This deals with the blocks.
        for block in block_list:
            if pygame.sprite.spritecollide(block, balls, False):
                if wall.paddle_last_hit == True:
                    wall.score_change_p2(50)
                if wall.paddle_last_hit == False:
                    wall.score_change_p1(50)
                diff = (block.rect.x + block.rect.y / 2) - (game_ball.rect.x + game_ball.height / 2)
                game_ball.bounce(diff)
            if pygame.sprite.spritecollide(block, balls, False):
                block.reset_pos()
               
        #This will change the color of the health bar for player 1 blue.
        if wall.health1 < 250:
            wall.healthcolor_change_p1()

        if wall.health1 < 150:
            wall.healthcolor_change_p1()

        #if player 1 has no health display the game over screen.
        if wall.health1 <= 0:
            victory_music.play()
            music.stop()
            #break
            playagain = True
            while playagain == True:
                myimage = pygame.image.load("Red_Win.jpg")
                imagerect = myimage.get_rect()
                
                screen.fill(BLACK)
                screen.blit(myimage, imagerect)
                pygame.display.flip()

                
                uInput = input("Play again?")
                try:
                    if uInput.lower() == "y":
                        main()
                    if uInput.lower() == "n":
                        pygame.quit()
                except:
                    print("Letters only")
                
                '''
                #My attempt at the (Y/N)
                if event.type == pygame.KEYDOWN:
                    # Figure out if it was an arrow key. If so
                    # adjust speed.
                    if event.key == pygame.K_y:
                        main()
                
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_y:
                            main()
                        if event.key == pygame.K_n:
                            pygame.quit()
                '''
            screen.fill(BLACK)
            
      #This will change the color of the health bar for player 2 red.
        if wall.health2 < 250:
            wall.healthcolor_change_p2()

        if wall.health2 < 150:
            wall.healthcolor_change_p2()

        #If player 2 has no health. Display game over.
        if wall.health2 <= 0:
            victory_music.play()
            music.stop()
            playagain = True
            while playagain == True:
                myimage = pygame.image.load("Blue_Win.jpg")
                imagerect = myimage.get_rect()
                
                screen.fill(BLACK)
                screen.blit(myimage, imagerect)
                pygame.display.flip()
                
                
                #This is the continue prompt.
                uInput = input("Play again?")
                try:
                    if uInput.lower() == "y":
                        main()
                    if uInput.lower() == "n":
                        pygame.quit()
                except:
                    print("Letters only")

                 
                '''
                #I tried the (Y/N) thing.
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == pygame.k_y:
                            main()
                '''
                
            screen.fill(BLACK)
     
        

        # Draw Everything
        movingsprites.draw(screen)
        all_sprites_list.draw(screen)


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)
        
#Calls the main program.
if __name__ == "__main__":
    main()
 
# Close the window and quit.
pygame.quit()
