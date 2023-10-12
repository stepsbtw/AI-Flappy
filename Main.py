import pygame
import os
import Globals
from Bird import Bird
from Pipe import Pipe
from Base import Base

def main():
   pygame.init()
   IS_RUNNING = True
   CLOCK = pygame.time.Clock()

# CRIANDO LOOP

   WINDOW = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
   players = [Bird(Globals.SCREEN_WIDTH/8, (Globals.GAME_HEIGHT/2) - Bird.SPRITE_HEIGHT/2)]
   pipes = [Pipe(Globals.SCREEN_WIDTH+Globals.SCREEN_WIDTH/2)]
   base = Base(Globals.SCREEN_HEIGHT - Base.HEIGHT)
   score = 0 # pra i.a desliga

# GAME LOOP

   while IS_RUNNING:
      CLOCK.tick(60)
      WINDOW.fill((255, 255, 255))

      for event in pygame.event.get(): # CHECK DE EVENTOS
         if event.type == pygame.QUIT:
            IS_RUNNING = False
         if event.type == pygame.KEYDOWN:
            match event.key:
               case K_SPACE: 
                  for player in players:
                     player.jump()

      for i,player in enumerate(players): # ENUMERAR E PEGAR O INDEX
         player.move()
         if player.DEAD:
            players.pop(i)
      base.move()
      add_pipe = False
      remove_pipes = []

# CRIACAO E REMOÇÃO DO LOOP DE CANOS.

      for pipe in pipes:
         pipe.move()
         for i, player in enumerate(players): # pega o index de cada passaro em passaros.
            if pipe.collision(player):
               players.pop(i) # MATEI O PASSARO.
            if not pipe.score:
               if player.x > pipe.x: # se o passaro passou do cano cria um novo.
                  pipe.score = True
                  add_pipe = True
         if pipe.x + pipe.sprite_width < 0:
            remove_pipes.append(pipe)

      if add_pipe:
         score +=1
         pipes.append(Pipe(Globals.SCREEN_WIDTH))

      for pipe in remove_pipes:
         remove_pipes.remove(pipe)

      draw_all(WINDOW,players,pipes,base,score)
      pygame.display.update()

   pygame.quit()

# FUNCAO PRA IMPRIMIR NA TELA

def draw_all(window,birds,pipes,base,score):
   window.blit(Globals.SPRITE_BG,(0,0))
   for pipe in pipes:
      pipe.draw(window)
   base.draw(window)
   for bird in birds:
      bird.draw(window)
   score_text = Globals.SCORE_FONT.render(f'score: {score}',0,(255,255,255))
   window.blit(score_text,(Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH/10 - score_text.get_width(),Globals.GAME_HEIGHT - Globals.GAME_HEIGHT/10))


main()
