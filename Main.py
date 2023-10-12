import pygame
import os
from Bird import Bird
from Pipe import Pipe
import Globals
#import Floor

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
#SCREEN_SCALE = 2

def main():
   pygame.init()
   IS_RUNNING = True
   CLOCK = pygame.time.Clock()
   WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   SPRITE_BG = pygame.transform.scale(pygame.image.load(os.path.join('sprites','bg.png')),(300,600))
   BIRD = Bird(150, 300) 
   PIPES = [Pipe(100,SCREEN_HEIGHT),Pipe(100,0),Pipe(150,SCREEN_HEIGHT-100),Pipe(150,100)]
   # tentei gerar pra cada pipe um inverso.
   while IS_RUNNING:  
      CLOCK.tick(60)
      WINDOW.fill((255, 255, 255))
      WINDOW.blit(SPRITE_BG,(0,0))#colocar o BG aqui
      BIRD.do_all(WINDOW)
      #PIPES[0].draw(WINDOW)
      #PIPES[1].draw(WINDOW)
      #PIPES[2].draw(WINDOW)
      #PIPES[3].draw(WINDOW)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            IS_RUNNING = False
      pygame.display.update()

   pygame.quit()

main()
