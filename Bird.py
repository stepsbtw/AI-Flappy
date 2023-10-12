import pygame
import os
import Globals
import Base

class Bird:
   TIME_ANIMATION = 30
   SPRITES = [pygame.image.load(os.path.join('sprites', 'bird2.png')),
              pygame.image.load(os.path.join('sprites', 'bird1.png'))]
   SPRITE_WIDTH = SPRITES[0].get_width()
   SPRITE_HEIGHT = SPRITES[0].get_height()
   def __init__(self,x,y):
      self.DEAD = False
      self.x = x
      self.y = y
      self.tick_jump = 0
      self.tick_fall = 0
      self.tick_animation=0
      self.is_jumping = False
      self.sprite = self.SPRITES[0]
      #self.weights = [0, 0]
      #self.score = 0

   #def vision(self, xpipe, ypipe):
   # pega o x e y do ponto
   # diminui do x e y do passaro
   # chama o think

   #def think(self, xdelta, ydelta):
   # pega os deltas e decide o output

   def jump(self):
      self.is_jumping = True
      self.tick_fall = 0
      # nao ta nada suave.

   def move(self):
      if self.is_jumping:
         if self.tick_jump >= 5:
            self.is_jumping = False
         self.tick_jump += 1
         self.y -= (self.tick_jump**2)/(Globals.GAME_HEIGHT/160)
         if self.y < Globals.SCREEN_HEIGHT - Globals.GAME_HEIGHT:
            self.DEAD = True
      else:
         self.tick_jump = 0
         self.tick_fall +=1
         self.y += (self.tick_fall**2)/2000
         if self.y < Globals.GAME_HEIGHT - self.SPRITE_HEIGHT:
            self.DEAD = True

   def draw(self, window):
      self.tick_animation += 1
      if self.tick_animation < self.TIME_ANIMATION:
         self.sprite = self.SPRITES[1]
      elif self.tick_animation >= self.TIME_ANIMATION * 2:
         self.tick_animation = 0
      else:
         self.sprite = self.SPRITES[0]

      if self.is_jumping:
         self.sprite = self.SPRITES[1]

      #center_pos = self.sprite.get_rect(topleft=(self.x, self.y)).center
      #rect = self.sprite.get_rect(center=center_pos)
      window.blit(self.sprite,(self.x,self.y)) #imprime o boneco na tela

   def get_mask(self):
      return pygame.mask.from_surface(self.sprite)

