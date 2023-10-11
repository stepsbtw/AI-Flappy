import pygame

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 800
SCREEN_SCALE = 2

janela = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

def main():

    while run: 
        clock.tick(60) 
        janela.fill(white) #colocar o BG aqui
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False 
        pygame.display.update() 

    pygame.quit()

class Bird():
   def __init__(self,x,y):
      self.score = 0
      self.x = x
      self.y = y
      self.weights = []
   
   def vision(xpipe, ypipe):
# pega o x e y do ponto
# diminui do x e y do passaro
# chama o think

   def think(xdelta, ydelta):
# pega os deltas e decide o output

   def jump(output):
# pula!
      

class Pipe():
   def __init__(self,x,y,height):
       self.height = height
       self.x = x
       self.y = y