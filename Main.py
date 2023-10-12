import pygame
import os
import Bird
import Pipe
import Floor

SCREEN_WIDTH = 350
SCREEN_HEIGHT = 600
SCREEN_SCALE = 2

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SPRITE_BG = pygame.image.load(os.path.join('sprites','bg'))

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
   
main()
