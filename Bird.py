import pygame
import os
#import random
import Globals
#import math

class Bird:
   TIME_ANIMATION = 30
   SPRITES = [pygame.image.load(os.path.join('sprites', 'bird2.png')),pygame.image.load(os.path.join('sprites', 'bird1.png'))]
   SPRITE_WIDTH = SPRITES[0].get_width()
   SPRITE_HEIGHT = SPRITES[0].get_height()
   def __init__(self,weights):
      self.DEAD = False
      self.x = Globals.SCREEN_WIDTH//8
      self.y = (Globals.GAME_HEIGHT//2) + (Bird.SPRITE_HEIGHT//2)
      self.tick_jump = 0
      self.tick_fall = 0
      self.tick_animation=0
      self.is_jumping = False
      self.sprite = self.SPRITES[0]
      #self.move()
      #self.weights = []
      self.ia_score = 0
      #if not weights:
         #self.weights = [random.randint(-1000,1000),
                            #random.randint(-1000,1000),
                            #random.randint(-1000,1000),
                            #random.randint(-1000,1000)]
      self.weights = weights
      
   def vision(self, pipe):
      if self.DEAD:
         return
      deltax = pipe.x - self.x
      deltay = (pipe.y_invert-pipe.DISTANCE/2) - self.y
      #deltay = pipe.y_invert - self.y
      #deltay2 = pipe.y_invert - self.y
      return (deltax, deltay)

   def brain(self, pipe):
      if self.DEAD:
         return
      inputs = self.vision(pipe)
      #print(inputs)
      outputs = [0, 0]

      outputs[0] = (inputs[0] * self.weights[0]) + (inputs[1] * self.weights[1])
      outputs[1] = (inputs[0] * self.weights[2]) + (inputs[1] * self.weights[3])
      #print(outputs)
      #outputs[0] = math.tanh(outputs[0])
      #outputs[1] = math.tanh(outputs[1])
      #print(outputs)
      if outputs[0] > outputs[1]: # alguma funcao qualquer que determine o output.
         self.jump()
      
   def jump(self):
      if self.DEAD:
         return
      self.is_jumping = True
      self.tick_fall = 2
      self.move()# comecar ja com um valor pra parabola ser mais rapida

   def move(self):
      if self.DEAD:
         return
      if self.is_jumping:
         if self.tick_jump >= 5: # 5 frames de pulo
            self.is_jumping = False
         self.tick_jump += 1
         self.y -= (self.tick_jump**2)/(Globals.GAME_HEIGHT//160)
         if self.y < Globals.SCREEN_HEIGHT - Globals.GAME_HEIGHT:
            self.DEAD = True
      else:
         self.tick_jump = 0
         self.tick_fall +=2
         self.y += (self.tick_fall**2)/2000
         if self.y > Globals.GAME_HEIGHT - self.SPRITE_HEIGHT:
            self.DEAD = True

   def draw(self, window):
      if self.DEAD:
         return
      self.tick_animation += 1
      if self.tick_animation < self.TIME_ANIMATION:
         self.sprite = self.SPRITES[1]
      elif self.tick_animation >= self.TIME_ANIMATION * 2:
         self.tick_animation = 0
      else:
         self.sprite = self.SPRITES[0]

      if self.is_jumping:
         self.sprite = self.SPRITES[1]

      window.blit(self.sprite,(self.x,self.y)) #imprime o boneco na tela

   def get_mask(self):
      if self.DEAD:
         return
      return pygame.mask.from_surface(self.sprite)

   

