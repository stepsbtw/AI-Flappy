import pygame
import os
import Globals

class Base:
    SPRITE = pygame.transform.scale(pygame.image.load(os.path.join('sprites','base.png')),(Globals.SCREEN_WIDTH,Globals.SCREEN_HEIGHT/8))
    SPRITE_INVERTED = pygame.transform.flip(SPRITE,False,True)
    SPEED = Globals.SCREEN_WIDTH/85
    WIDTH = SPRITE.get_width()
    HEIGHT = SPRITE.get_height()

    def __init__(self):
        self.y = Globals.SCREEN_HEIGHT - Base.HEIGHT
        self.x = 0
        self.x2 = self.WIDTH

    def draw(self,window):
        window.blit(self.SPRITE_INVERTED,(self.x,0))
        window.blit(self.SPRITE,(self.x,self.y))
        window.blit(self.SPRITE_INVERTED,(self.x2,0))
        window.blit(self.SPRITE,(self.x2,self.y))

    def move(self):
        self.x -= self.SPEED
        self.x2 -=  self.SPEED

        if self.x + self.WIDTH <= 0:
            self.x = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH <= 0:
            self.x2 = self.x + self.WIDTH