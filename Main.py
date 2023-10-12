import pygame
import os
import Globals
from Bird import Bird
from Pipe import Pipe
#import Floor

def main():
   pygame.init()
   IS_RUNNING = True
   CLOCK = pygame.time.Clock()
   WINDOW = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
   Player = Bird((Globals.SCREEN_WIDTH/2) - Bird.SPRITE_WIDTH/2, (Globals.GAME_HEIGHT/2) - Bird.SPRITE_HEIGHT/2)
   PIPES = [Pipe(0,0)]
   # tentei gerar pra cada pipe um inverso.
   # criei o passaro centralizado.
   while IS_RUNNING:  
      CLOCK.tick(60)
      WINDOW.fill((255, 255, 255))
      WINDOW.blit(Globals.SPRITE_BG,(0,0))
      WINDOW.blit(Globals.SPRITE_BASE_INVERTED,(0,0)) # bordinha.
      WINDOW.blit(Globals.SPRITE_BASE,(0,Globals.GAME_HEIGHT))
      Player.do_all(WINDOW)
      #PIPES[0].draw(WINDOW)
      #PIPES[1].draw(WINDOW)
      #PIPES[2].draw(WINDOW)
      #PIPES[3].draw(WINDOW)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            IS_RUNNING = False
         if event.type == pygame.KEYDOWN:
            match event.key:
               case K_SPACE: 
                  Player.jump()

      pygame.display.update()

   pygame.quit()

main()
