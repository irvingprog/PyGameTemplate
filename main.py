import pygame
from pygame.locals import *

screen = None

SCREEN_WIDTH = 640;
SCREEN_HEIGHT = 480;

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Template")


'''
####################################################
#                  SCENES                          #
####################################################
'''

class Game():
    """This Class is a screen of the Game"""
    def __init__(self):
        """Here initialize variables and create the objects
            Example:

            self.myactor = MyActor()
        """
        pass

    def update(self):
        """Here functions that updating in the game

            Example:

            self.myactor.run()
        """
        pass

    def draw(self,screen):
        """Here functions for draw objects on screen
            Example:

            self.myactor.draw(screen)
        """
        pass

'''
####################################################
#                GAME LOOP                         #
####################################################
'''
def main():
    global scene
    pygame.init()
    
    clock = pygame.time.Clock()
    
    scene = Game()
        
    while True:
        scene.update()
        scene.draw(screen)
        clock.tick(60)
        
if __name__ == '__main__':
    main()
