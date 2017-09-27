# EG16-04 Steerable cheese

import pygame

class ImageDemo:

    @staticmethod
    def do_image_demo():
        init_result = pygame.init()
        if init_result[1] != 0:
            print('pygame not installed properly')
            return

        width = 800
        height = 600
        size = (width, height)

        surface = pygame.display.set_mode(size)
        pygame.display.set_caption('Moving cheese')

        cheeseImage = pygame.image.load("cheese.png")

        cheeseX = 40
        cheeseY = 60
        cheeseYSpeed = 3
        cheeseMovingUp = False
        cheeseMovingDown = False
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(30)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    elif e.key == pygame.K_UP:
                        cheeseMovingUp = True
                    elif e.key == pygame.K_DOWN:
                        cheeseMovingDown = True
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        cheeseMovingUp = False
                    elif e.key == pygame.K_DOWN:
                        cheeseMovingDown = False
            if cheeseMovingDown:
                cheeseY = cheeseY+cheeseYSpeed
            if cheeseMovingUp:
                cheeseY = cheeseY-cheeseYSpeed
            surface.fill((255,255,255))
            cheesePos = (int(cheeseX),int(cheeseY))
            surface.blit(cheeseImage, cheesePos)
            pygame.display.flip()
                    
ImageDemo.do_image_demo()

