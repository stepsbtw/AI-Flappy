import pygame
import os
import Globals

class Pipe:
   SPRITE = pygame.image.load(os.path.join('sprites', 'pipe.png'))
   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.sprite = SPRITE
      self.sprite_invert = pygame.transform.flip(self.sprite,False,True)

   def draw(self,window):
      window.blit(self.sprite,(self.x,self.y))
      window.blit(self.sprite_invert,(self.x,self.y))
      #window.blit(self.sprite,(self.x,self.y))

#printar o inverso, um cano sempre tem o seu cano reverso.
