# EG16-05 background sprite

import pygame

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

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Cracker Chase')
        background_image = pygame.image.load('background.png')
        self.background_sprite = Sprite(image=background_image,
                                        game=self)

        clock = pygame.time.Clock()        

        while True:
            clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
            self.background_sprite.draw()
            pygame.display.flip()


game = CrackerChase()
game.play_game()
