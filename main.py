import pygame
import os

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SCREEN_SCALE = 2

WINDOW = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

SPRITES_BIRD = [pygame.image.load(os.path.join('sprites', 'bird2.png')),pygame.image.load(os.path.join('sprites', 'bird1.png'))]
SPRITE_PIPE = pygame.image.load(os.path.join('sprites', 'pipe.png'))
SPRITE_FLOOR = pygame.image.load(os.path.join('sprites', 'base.png'))
SPRITE_BG = pygame.image.load(os.path.join('sprites', 'bg.png'))

def main():
   IS_RUNNING = True
   CLOCK = pygame.time.Clock()
   while IS_RUNNING:
      CLOCK.tick(60)
      WINDOW.fill((0,200,200)) #colocar o BG aqui
      for event in pygame.event.get(): 
         if event.type == pygame.QUIT:
            IS_RUNNING = False 
      pygame.display.update() 

   pygame.quit()

class Bird():
   TEMPO_ANIMACAO = 30
   SPRITES = SPRITES_BIRD
   def __init__(self,x,y):
      self.score = 0
      self.x = x
      self.y = y
      self.speed = 0
      self.tick = 0
      self.tick_animation = 0
      self.height = y
      self.accel = 1.5
      self.sprite = self.sprites[0]
      self.weights = [0,0]
   
   def vision(self, xpipe, ypipe):
      x
      # pega o x e y do ponto
      # diminui do x e y do passaro
      # chama o think


   def think(self, xdelta, ydelta):
      x
      # pega os deltas e decide o output

   def jump(self, output):
      self.tick = 0
      self.speed = -2*accel # valor negativo no y, boneco vai pra cima!
      self.height = self.y
      # pula!

   def move(self):
      # SORVETAO, PARABOLA! S = So + Vo + at^2/2
      self.tick+=1
      movement = (self.accel*(self.tick**2))/2 + self.speed
      self.y += movement

   def draw(self,window):
      self.tick_animation += 1
      if self.tick_animation < self.TEMPO_ANIMACAO:
         self.sprite = self.SPRITES[1]
      else:
         self.sprite = self.SPRITES[0]

      if self.speed > 0:
         self.sprite = self.SPRITES[1]

      center_pos = self.sprite.get_rect(topleft=(self.x,self.y)).center
      rect = self.sprite.get_rect(center = center_pos)
      window.blit(self.sprite, rect.topleft)

   def do_all(self,window,):
      self.draw(self,window)
      self.movement(self)
       
class Pipe():
   def __init__(self,x,y,height):
       self.height = height
       self.x = x
       self.y = y

main()