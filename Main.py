import pygame
import os
import Globals
from Pipe import Pipe
from Base import Base
from Evolution import Evolution
from Bird import Bird
import random


def main():
   pygame.init()
   is_running = True
   clock = pygame.time.Clock()
   window = pygame.display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
   pipes = [Pipe(0)]
   base = Base()
   players = []
   dead_players = []
   DARWIN = Evolution()
   players = DARWIN.first_gen()
   MVP_CURRENT_GEN_SCORE = 0
   CURRENT_PIPE = 0

   while is_running:
      clock.tick(60)
      window.fill((255, 255, 255))
      CURRENT_GENERATION = DARWIN.generation
      
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            is_running = False

      CURRENT_PIPE = 0

      if players:
         if pipes and players[0].x > (pipes[0].x + pipes[0].sprite_width):
            CURRENT_PIPE = 1
      else:
         players = DARWIN.new_gen(dead_players)
         MVP_CURRENT_GEN_SCORE = 0
         pipes = [Pipe(0)]
         continue

      for player in players:
         player.move()
         player.brain(pipes[CURRENT_PIPE])
      base.move()
      MVP_CURRENT_GEN_SCORE = check(pipes,players,dead_players,MVP_CURRENT_GEN_SCORE)
      
         
      #if not players: # quando todos morrem, passar pra prox geracao.
         #MVP_CURRENT_GEN_SCORE = 0
         #pipes = [Pipe()]
         #players = DARWIN.new_gen(dead_players)
         
      for i,player in enumerate(players):
         if player.y < Globals.SCREEN_HEIGHT - Globals.GAME_HEIGHT:
            dead_players.append(player)
            players.pop(i)
         if player.y > Globals.GAME_HEIGHT - player.SPRITE_HEIGHT:
            dead_players.append(player)
            players.pop(i)

      draw_all(window,players,pipes,base,MVP_CURRENT_GEN_SCORE,CURRENT_GENERATION)
      pygame.display.update()

   pygame.quit()
   quit()

# ta faltando um pipe.pop
def check(pipes,players,dead_players,MVP_CURRENT_GEN_SCORE): # a cada cano que some da tela, um novo é gerado.
   add_pipe = False # isso tbm ta dando merda. add_pipe = score
   remove_pipes = []
   for pipe in pipes:
      for i,player in enumerate(players):
         if pipe.collision(player):
            dead_players.append(player)
            players.pop(i)
         if not pipe.score and player.x > pipe.x: # caso ainda nao tenha sido feito ponto e o jogador passou, ponto!
                  pipe.score = True
                  add_pipe = True # se foi ponto, adicionar um cano
                  #player.ia_score *= 2
      pipe.move()
      if pipe.x + pipe.sprite_width < 0: # se o pipe saiu, entra na fila de remocao.
         remove_pipes.append(pipe)
   if add_pipe: # apenas adicionar o novo cano fora do loop.
      player.ia_score += 1
      MVP_CURRENT_GEN_SCORE += 1
      if MVP_CURRENT_GEN_SCORE >= 5 and MVP_CURRENT_GEN_SCORE <= 10:
         pipes.append(Pipe(Globals.SCREEN_WIDTH//95))
      elif MVP_CURRENT_GEN_SCORE >= 10 and MVP_CURRENT_GEN_SCORE <= 15:
            pipes.append(Pipe(Globals.SCREEN_WIDTH//90))
      elif MVP_CURRENT_GEN_SCORE > 15 and MVP_CURRENT_GEN_SCORE <= 20: 
            pipes.append(Pipe(Globals.SCREEN_WIDTH//85))
      elif MVP_CURRENT_GEN_SCORE > 25: 
            pipes.append(Pipe(Globals.SCREEN_WIDTH//75)) 
      else:
         pipes.append(Pipe(0))
   for pipe in remove_pipes: # remover os que ja sairam da tela.
      pipes.remove(pipe)
   return MVP_CURRENT_GEN_SCORE # se adicionei um pipe, prox pipe.
      
def draw_all(window,players,pipes,base,mvp_score,generation):
   window.blit(Globals.SPRITE_BG,(0,0))
   for pipe in pipes:
      pipe.draw(window)
   base.draw(window)
   for player in players:
      player.draw(window)
   generation_number = Globals.SCORE_FONT.render(f'generation: {generation}',0,(0,0,0))
   score_text = Globals.SCORE_FONT.render(f'score: {mvp_score}',0,(255,255,255))
   window.blit(generation_number,(Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH/10 - generation_number.get_width(),Globals.GAME_HEIGHT - Globals.GAME_HEIGHT/10 + score_text.get_height()+10))
   window.blit(score_text,(Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH/10 - score_text.get_width(),Globals.GAME_HEIGHT - Globals.GAME_HEIGHT/10))


main()
