import pygame
import os

SCREEN_WIDTH = 350
SCREEN_HEIGHT = 600
SCREEN_SCALE = 2

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SPRITES_BIRD = [
   pygame.image.load(os.path.join('sprites', 'bird2.png')),
   pygame.image.load(os.path.join('sprites', 'bird1.png'))
]
SPRITE_PIPE = pygame.image.load(os.path.join('sprites', 'pipe.png'))
SPRITE_FLOOR = pygame.image.load(os.path.join('sprites', 'base.png'))
SPRITE_BG = pygame.image.load(os.path.join('sprites', 'bg.png'))


def main():
   pygame.init()
   IS_RUNNING = True
   CLOCK = pygame.time.Clock()
   BIRD = Bird(150, 200)
   PIPES = [Pipe(100,SCREEN_HEIGHT),Pipe(100,0),Pipe(150,SCREEN_HEIGHT-100),Pipe(150,100)]
   while IS_RUNNING:  
      #print(BIRD.tick_animation)
      CLOCK.tick(60)
      WINDOW.fill((0, 200, 200))  #colocar o BG aqui
      BIRD.do_all(WINDOW)
      #PIPES[0].draw(WINDOW)
      #PIPES[1].draw(WINDOW)
      #PIPES[2].draw(WINDOW)
      #PIPES[3].draw(WINDOW)
      #print(BIRD.speed)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            IS_RUNNING = False
      pygame.display.update()

   pygame.quit()


class Bird:
   TEMPO_ANIMACAO = 30
   SPRITES = SPRITES_BIRD

   def __init__(self,x,y):
      self.score = 0
      self.x = x
      self.y = y
      self.speed = 1
      self.tick= 0
      self.tick_animation=0
      self.height = y
      self.accel = 20.5
      self.sprite = self.SPRITES[0]
      self.weights = [0, 0]

   #def vision(self, xpipe, ypipe):

   # pega o x e y do ponto
   # diminui do x e y do passaro
   # chama o think

   #def think(self, xdelta, ydelta):

   # pega os deltas e decide o output

   def jump(self):
      self.tick = 0
      self.y -= self.accel
      # valor negativo no y, boneco vai pra cima!
      # pula!

   def move(self):
      # SORVETAO, PARABOLA! S = So + Vo + at^2/2
      self.tick += 1
      self.y = min((self.y + (self.tick**2)/2000 ),SCREEN_HEIGHT - self.sprite.get_height())
      #if self.tick < 0:
         #self.y = self.y-self.speed-(self.tick**2)/100#max((self.y - self.speed -(self.tick**2)/2000),SCREEN_HEIGHT - self.sprite.get_height())
      if self.y >= SCREEN_HEIGHT - self.sprite.get_height():
         #pula!
            self.jump()

   def draw(self, window):
      self.tick_animation += 1
      if self.tick_animation < self.TEMPO_ANIMACAO:
         self.sprite = self.SPRITES[1]
      elif self.tick_animation >= self.TEMPO_ANIMACAO * 2:
         self.tick_animation = 0
      else:
         self.sprite = self.SPRITES[0]

      if self.speed > 0:
         self.sprite = self.SPRITES[1]

      #center_pos = self.sprite.get_rect(topleft=(self.x, self.y)).center
      #rect = self.sprite.get_rect(center=center_pos)
      window.blit(self.sprite,(self.x,self.y))

   #def gravity(self):
      #self.tick -= 1
      #self.y = min((self.y + self.speed), SCREEN_HEIGHT-self.sprite.get_height())

   def do_all(
      self,
      window,
   ):
      self.draw(window)
      self.move()
      #self.gravity()


class Pipe:
   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.sprite = SPRITE_PIPE

   def draw(self,window):
      window.blit(self.sprite,(self.x,self.y))
      #window.blit(self.sprite,(self.x,self.y))
#printar flipado

main()
