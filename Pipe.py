import pygame
import os

class Pipe:
   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.sprite = pygame.image.load(os.path.join('sprites', 'pipe.png'))
      self.sprite_invert = pygame.transform.flip(self.sprite,False,True)

   def draw(self,window):
      window.blit(self.sprite,(self.x,self.y))
      window.blit(self.sprite_invert,(self.x,self.y))
      #window.blit(self.sprite,(self.x,self.y))

#printar o inverso, um cano sempre tem o seu cano reverso.
