import pygame
import os
import Globals
import Base
import random

class Pipe:
   DISTANCE = Globals.SCREEN_HEIGHT//6 # entre canos!
   SPEED = Globals.SCREEN_WIDTH//100 # velocidade legal p/ ia
   SPRITE = pygame.image.load(os.path.join('sprites', 'pipe.png'))
   def __init__(self,speed):
      self.x = Globals.SCREEN_WIDTH# default 
      self.y = 0
      self.y_invert = 0
      self.height = 0
      self.sprite_invert = self.SPRITE
      self.sprite_invert_height = self.SPRITE.get_height
      self.sprite_invert_width = self.SPRITE.get_width()
      self.sprite = pygame.transform.flip(self.sprite_invert,False,True)
      self.sprite_height = self.SPRITE.get_height()
      self.sprite_width = self.SPRITE.get_width()
      self.score = False # ainda nao foi feito ponto.
      self.rand_height() # gerador de alturas aleatorios.
      self.speed = self.SPEED
      if speed:
         self.speed = speed

   def rand_height(self):
      self.height = random.randrange(Globals.GAME_HEIGHT//6, Globals.GAME_HEIGHT - Globals.GAME_HEIGHT//6)
      self.y = self.height - self.sprite_height
      self.y_invert = self.height + self.DISTANCE 
      

   def move(self):
      self.x -= self.speed

   def draw(self,window):
      window.blit(self.sprite,(self.x,self.y))
      window.blit(self.sprite_invert,(self.x,self.y_invert))

   def collision(self,player):
      if player.DEAD:
         return
      player_mask = player.get_mask()
      pipe_mask = pygame.mask.from_surface(self.sprite)
      invert_mask = pygame.mask.from_surface(self.sprite_invert)

      player_distance = (self.x - player.x,self.y - player.y)
      player_distance_invert = (self.x - player.x, self.y_invert - player.y)

      collision = player_mask.overlap(pipe_mask,player_distance)
      collision_invert = player_mask.overlap(invert_mask,player_distance_invert)

      if collision or collision_invert:
         return True
      return False

#printar o inverso, um cano sempre tem o seu cano reverso.
