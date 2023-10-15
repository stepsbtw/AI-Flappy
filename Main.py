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
   pipes = [Pipe()]
   base = Base()
   players = []
   dead_players = []
   DARWIN = Evolution()
   players = DARWIN.first_gen()
   MVP_CURRENT_GEN_SCORE = 0

   while is_running:

      clock.tick(60)
      window.fill((255, 255, 255))
      CURRENT_GENERATION = DARWIN.generation

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            is_running = False

      if not players: # quando todos morrem, passar pra prox geracao.
         MVP_CURRENT_GEN_SCORE = 0
         pipes = [Pipe()]
         players = DARWIN.new_gen(dead_players)

      base.move()

      plus = check(pipes,players,dead_players)
      if plus:
         MVP_CURRENT_GEN_SCORE+=1

      draw_all(window,players,pipes,base,MVP_CURRENT_GEN_SCORE,CURRENT_GENERATION)
      pygame.display.update()

   pygame.quit()

# ta faltando um pipe.pop
def check(pipes,players,dead_players): # a cada cano que some da tela, um novo é gerado.
   add_pipe = False # isso tbm ta dando merda. add_pipe = score
   remove_pipes = []
   for pipe in pipes:
      pipe.move()
      for player in players:
         if not pipe.score:
               if player.x < pipe.x:
                  player.ia_score += ((pipe.y_invert-pipe.DISTANCE/2)- player.y)//100
                  #print(player.x, pipe.x,pipe.y_invert,pipe.DISTANCE) # to dando ponto pro quao perto ele chega
               if player.x > pipe.x: # caso ainda nao tenha sido feito ponto e o jogador passou, ponto!
                  pipe.score = True
                  add_pipe = True # se foi ponto, adicionar um cano
                  player.ia_score *= 2
                  #player.ia_score += 1
         if player.DEAD:
            dead_players.append(player) # adiciona-lo na lista de mortos.
            players.remove(player)
         player.move()
         player.brain(pipe) # pega o index e o elemento referido
         if pipe.collision(player):
            player.DEAD = True
            dead_players.append(player)
            players.remove(player)
      if pipe.x + pipe.sprite_width < 0: # se o pipe saiu, entra na fila de remocao.
         remove_pipes.append(pipe)
   if add_pipe:
      pipes.append(Pipe()) 
   # apenas adicionar o novo cano fora do loop.
   for pipe in remove_pipes: # remover os que ja sairam da tela.
      remove_pipes.remove(pipe)
   return add_pipe # se adicionei um pipe, prox pipe.
      
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
