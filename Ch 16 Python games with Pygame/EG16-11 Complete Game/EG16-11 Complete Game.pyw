# EG16-11 Complete Game

import pygame

import random

import sys

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

    def intersects_with(self,sprite):
        max_x = self.position[0]+self.image.get_width()
        max_y = self.position[1]+self.image.get_height()
        
        smax_x = sprite.position[0]+sprite.image.get_width()
        smax_y = sprite.position[1]+sprite.image.get_height()
        if max_x < sprite.position[0]:
            return False

        if max_y < sprite.position[1]:
            return False

        if self.position[0] > smax_x:
            return False

        if self.position[1] > smax_y:
            return False

        return True

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

    def __init__(self, image, game, captured_sound):
        super().__init__(image, game)
        self.captured_sound = captured_sound
                
    def reset(self):
        self.position[0] = random.randint(0,
                self.game.width-self.image.get_width())
        self.position[1] = random.randint(0,
                self.game.height-self.image.get_height())

    def update(self):
        if self.intersects_with(game.cheese_sprite):
            self.captured_sound.play()
            self.reset()
            self.game.score += 10


class Tomato(Sprite):

    def __init__(self, image, game, entry_delay):
        super().__init__(image, game)
        self.entry_delay = entry_delay

    def update(self):

        self.entry_count = self.entry_count + 1
        if self.entry_count < self.entry_delay:
            return

        for i in range(0,2):
            if game.cheese_sprite.position[i] > self.position[i]:
                self.speed[i] =  self.speed[i] + self.acceleration[i]
            else:
                self.speed[i] =  self.speed[i] - self.acceleration[i]

            self.speed[i] = self.speed[i] * self.friction[i]
            self.position[i] = self.position[i] + self.speed[i]

        if self.intersects_with(game.cheese_sprite):
            self.game.end_game()
        
    def reset(self):
        self.entry_count = 0
        self.friction = [0.99, 0.99]
        self.acceleration = [0.2, 0.2]
        self.speed = [0, 0]
        self.position = [-100,-100]
        
class CrackerChase:
    '''
    Plays the amazing cracker chase game
    '''

    def display_message(self, message, y_pos):
        '''
        Displays a message on the screen
        The first argument is the message text
        The second argument is the vertical position
        of the text
        The text is drawn centered on the screen
        It is drawn with a black shadow
        '''
        shadow = self.font.render(message, True, (0,0,0))
        text = self.font.render(message, True, (0,0,255))
        text_position = [self.width/2 - text.get_width()/2, y_pos]
        self.surface.blit(shadow, text_position)
        text_position[0] += 2
        text_position[1] += 2
        self.surface.blit(text, text_position)
        
    def update_game(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
                if e.key == pygame.K_DOWN:
                    self.cheese_sprite.StopMoveDown()
                if e.key == pygame.K_LEFT:
                    self.cheese_sprite.StopMoveLeft()
                if e.key == pygame.K_RIGHT:
                    self.cheese_sprite.StopMoveRight()
                    
        for sprite in self.sprites:
            sprite.update()

                    
    def draw_game(self):
        for sprite in self.sprites:
            sprite.draw()
        status = 'Score: ' + str(game.score)
        self.display_message(status, 0)
            

    def start_game(self):
        for sprite in self.sprites:
            sprite.reset()
        self.game_running = True
        self.score=0

    def end_game(self):
        self.game_running = False
        if self.score > self.top_score:
            self.top_score = self.score

    def update_start(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif e.key == pygame.K_g:
                    self.start_game()
        
    def draw_start(self):
        self.start_background_sprite.draw()
        self.display_message(message='Top Score: ' + str(self.top_score),y_pos=0)
        self.display_message(message='Welcome to Cracker Chase', y_pos=150)
        self.display_message(message='Steer the cheese to', y_pos=250)
        self.display_message(message='capture the crackers', y_pos=300)
        self.display_message(message='BEWARE THE KILLER TOMATOES', y_pos=350)
        self.display_message(message='Arrow keys to move', y_pos=450)
        self.display_message(message='Press G to play', y_pos=500)
        self.display_message(message='Press Escape to exit', y_pos=550)
        
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

        self.font = pygame.font.Font(None, 60)

        start_background_image = pygame.image.load('start background.png')
        self.start_background_sprite = Sprite(image=start_background_image,
                                              game=self)

        self.sprites = []

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Cracker Chase')
        background_image = pygame.image.load('background.png')
        self.background_sprite = Sprite(image=background_image,
                                        game=self)

        self.sprites.append(self.background_sprite)

        cracker_image = pygame.image.load('cracker.png')
        cracker_eat_sound = pygame.mixer.Sound('burp.wav')

        for i in range(20):
            cracker_sprite = Cracker(image=cracker_image,
                game=self, captured_sound=cracker_eat_sound)

            self.sprites.append(cracker_sprite)

        cheese_image = pygame.image.load('cheese.png')
        self.cheese_sprite = Cheese(image=cheese_image,
                                        game=self)

        self.sprites.append(self.cheese_sprite)

        tomato_image = pygame.image.load('tomato.png')

        for entry_delay in range(300,3000,300):
            tomato_sprite = Tomato(image=tomato_image,
                                        game=self,
                                        entry_delay=entry_delay )
            self.sprites.append(tomato_sprite)
        
        clock = pygame.time.Clock()

        self.score = 0
        self.top_score = 0
        self.end_game()

        self.game_active = True

        while self.game_active:
            clock.tick(60)
            if self.game_running:
                self.update_game()
                self.draw_game()
            else:
                self.update_start()
                self.draw_start()
            pygame.display.flip()
        


game = CrackerChase()
game.play_game()
