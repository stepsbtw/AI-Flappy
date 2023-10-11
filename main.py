import pygame
import os

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SCREEN_SCALE = 2

WINDOW = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

SPRITES_BIRD = [pygame.image.load(os.path.join('sprites', 'bird1.png')),pygame.image.load(os.path.join('sprites', 'bird3.png'))]
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
   def __init__(self,x,y):
      self.score = 0
      self.x = x
      self.y = y
      self.height = y
      self.speed = 0
      self.tick = 0
      self.accel = 1.5
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
      self.speed = -5 # valor negativo no y, boneco vai pra cima!
      # pula!

   def move(self):
      # SORVETAO, PARABOLA! S = So + Vo + at^2/2
      self.tick+=1
      movement = (self.accel*(self.tick**2))/2 + self.speed
      self.y += movement
       
class Pipe():
   def __init__(self,x,y,height):
       self.height = height
       self.x = x
       self.y = y

main()