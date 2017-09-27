# EG16-08 Cheese and crackers

import pygame

import random

class Sprite:
    '''
    A sprite in the game. Can be sub-classed
    to create sprites with particular behaviours
    '''
    def __init__(self, image, game):
        '''
        Initialize a sprite
        image is the image to use to draw the sprite
        default position is origin (0,0)
        game is the game that contains this sprite
        '''
        self.image = image
        self.position = [0, 0]
        self.game = game
        self.reset()

    def update(self):
        '''
        Called in the game loop to update
        the status of the sprite.
        Does nothing in the super class
        '''
        pass

    def draw(self):
        '''
        Draws the sprite on the screen at its
        current position
        '''
        self.game.surface.blit(self.image, self.position)

    def reset(self):
        '''
        Called at the start of a new game to
        reset the sprite
        '''
        pass


class Cheese(Sprite):
    '''
    Player controlled cheese object that can be steered
    around the screen by the player
    '''

    def reset(self):
        '''
        Reset the cheese position and stop any movement
        Set the movement speed back to the start speed
        '''
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
        self.position[0] = (self.game.width - self.image.get_width())/2
        self.position[1] = (self.game.height - self.image.get_height())/2
        self.movement_speed=[5,5]
        
    def update(self):
        '''
        Update the cheese position and then stop it moving off
        the screen.
        '''
        if self.movingUp:
            self.position[1] = self.position[1] - (self.movement_speed[1])
        if self.movingDown:
            self.position[1] = self.position[1] + (self.movement_speed[1])
        if self.movingLeft:
            self.position[0] = self.position[0] - (self.movement_speed[0])
        if self.movingRight:
            self.position[0] = self.position[0] + (self.movement_speed[0])

        if self.position[0] < 0:
            self.position[0]=0
        if self.position[1] < 0:
            self.position[1]=0
        if self.position[0] + self.image.get_width() > self.game.width:
            self.position[0] = self.game.width - self.image.get_width()
        if self.position[1] + self.image.get_height() > self.game.height:
            self.position[1] = self.game.height - self.image.get_height()

        
    def StartMoveUp(self):
        'Start the cheese moving up'
        self.movingUp = True
        
    def StopMoveUp(self):
        'Stop the cheese moving up'
        self.movingUp = False
        
    def StartMoveDown(self):
        'Start the cheese moving down'
        self.movingDown = True
        
    def StopMoveDown(self):
        'Stop the cheese moving down'
        self.movingDown = False

    def StartMoveLeft(self):
        'Start the cheese moving left'
        self.movingLeft = True
        
    def StopMoveLeft(self):
        'Stop the cheese moving left'
        self.movingLeft = False

    def StartMoveRight(self):
        'Start the cheese moving right'
        self.movingRight = True
        
    def StopMoveRight(self):
        'Stop the cheese moving right'
        self.movingRight = False

class Cracker(Sprite):
    '''
    The cracker provides a target for the cheese
    When reset it moves to a different random place
    on the screen
    '''
    def reset(self):
        self.position[0] = random.randint(0,
                self.game.width-self.image.get_width())
        self.position[1] = random.randint(0,
                self.game.height-self.image.get_height())
        

class CrackerChase:
    '''
    Plays the amazing cracker chase game
    '''
    
    def play_game(self):
        '''
        Starts the game playing
        Will return when the player exits
        the game.
        '''
        init_result = pygame.init()
        if init_result[1] != 0:
            print('pygame not installed properly')
            return

        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.sprites = []

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Cracker Chase')
        background_image = pygame.image.load('background.png')
        self.background_sprite = Sprite(image=background_image,
                                        game=self)

        self.sprites.append(self.background_sprite)

        cracker_image = pygame.image.load('cracker.png')

        for i in range(20):
            cracker_sprite = Cracker(image=cracker_image,
                                          game=self)

            self.sprites.append(cracker_sprite)

        cheese_image = pygame.image.load('cheese.png')
        self.cheese_sprite = Cheese(image=cheese_image,
                                        game=self)

        self.sprites.append(self.cheese_sprite)
        
        clock = pygame.time.Clock()        

        while True:
            clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    elif e.key == pygame.K_UP:
                        self.cheese_sprite.StartMoveUp()
                    elif e.key == pygame.K_DOWN:
                        self.cheese_sprite.StartMoveDown()
                    elif e.key == pygame.K_LEFT:
                        self.cheese_sprite.StartMoveLeft()
                    elif e.key == pygame.K_RIGHT:
                        self.cheese_sprite.StartMoveRight()
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        self.cheese_sprite.StopMoveUp()
                    elif e.key == pygame.K_DOWN:
                        self.cheese_sprite.StopMoveDown()
                    elif e.key == pygame.K_LEFT:
                        self.cheese_sprite.StopMoveLeft()
                    elif e.key == pygame.K_RIGHT:
                        self.cheese_sprite.StopMoveRight()

            for sprite in self.sprites:
                sprite.update()

            for sprite in self.sprites:
                sprite.draw()
                
            pygame.display.flip()


game = CrackerChase()
game.play_game()
