import pygame

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 800
SCREEN_SCALE = 2

WINDOW = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

SPRITES_BIRD = [pygame.image.load(),pygame.image.load()]
SPRITE_PIPE = pygame.image.load()
SPRITE_FLOOR = pygame.image.load()
SPRITE_BG = pygame.image.load()

def main():
    is_running = True
    while is_running:
        clock.tick(60) 
        window.fill(white) #colocar o BG aqui
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                is_running = False 
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
      self.accel = 0
      self.weights = []
   
   def vision(self, xpipe, ypipe):
# pega o x e y do ponto
# diminui do x e y do passaro
# chama o think

   def think(self, xdelta, ydelta):
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