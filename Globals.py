import pygame
import os
SCREEN_SCALE = 40
SCREEN_WIDTH = 9*SCREEN_SCALE
SCREEN_HEIGHT = 16*SCREEN_SCALE
SPRITE_BG = pygame.transform.scale(pygame.image.load(os.path.join('sprites','bg.png')),(SCREEN_WIDTH,SCREEN_HEIGHT))
SPRITE_BASE = pygame.transform.scale(pygame.image.load(os.path.join('sprites','base.png')),(SCREEN_WIDTH,SCREEN_HEIGHT/8))
BASE_HEIGHT = SPRITE_BASE.get_height()
SPRITE_BASE_INVERTED = pygame.transform.flip(SPRITE_BASE,False,True)

GAME_HEIGHT = SCREEN_HEIGHT - BASE_HEIGHT # altura do espaço jogavel.
