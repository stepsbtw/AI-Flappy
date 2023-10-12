import pygame
import os

SCREEN_SCALE = 30
SCREEN_WIDTH = 9*SCREEN_SCALE
SCREEN_HEIGHT = 16*SCREEN_SCALE
pygame.font.init()
SCORE_FONT = pygame.font.SysFont('comic-sans',30)
SPRITE_BASE = pygame.transform.scale(pygame.image.load(os.path.join('sprites','base.png')),(SCREEN_WIDTH,SCREEN_HEIGHT/8))
GAME_HEIGHT = SCREEN_HEIGHT - SPRITE_BASE.get_height()
SPRITE_BG = pygame.transform.scale(pygame.image.load(os.path.join('sprites','bg.png')),(SCREEN_WIDTH,SCREEN_HEIGHT))

