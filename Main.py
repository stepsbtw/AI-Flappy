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
   DARWIN = Evolution(0)
   CURRENT_PIPE_NUM = 0
   MVP_SCORE = 0
   while is_running:
      clock.tick(60)
      window.fill((255, 255, 255))
      CURRENT_PIPE = pipes[CURRENT_PIPE_NUM]
      CURRENT_GENERATION = DARWIN.generation
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            is_running = False
      if(not players):
         MVP_SCORE = 0
         pipes = [Pipe()]
         players = DARWIN.new_gen(dead_players)
      base.move()
      for i,player in enumerate(players):
         if player.DEAD:
            dead_players.append(player)
            players.pop(i)
         player.move()
         player.brain(CURRENT_PIPE)
      plus , CURRENT_PIPE = check_score(pipes,players,dead_players,CURRENT_PIPE_NUM,CURRENT_PIPE)
      if plus:
         MVP_SCORE+=1# isso ta dando problema.
      draw_all(window,players,pipes,base,MVP_SCORE,CURRENT_GENERATION)
      pygame.display.update()

   pygame.quit()

# ta faltando um pipe.pop
def check_score(pipes,players,dead_players,CURRENT_PIPE_NUM,CURRENT_PIPE): # a cada cano que some da tela, um novo é gerado.
   add_pipe = False # isso tbm ta dando merda. add_pipe = score
   remove_pipes = []
   for pipe in pipes:
      pipe.move()
      for i, player in enumerate(players): # pega o index e o elemento referido
         if pipe.collision(player):
            player.DEAD = True
            dead_players.append(player)
            players.pop(i)
         if not pipe.score:
               if player.x < pipe.x:
                  player.ia_score += ((pipe.y_invert-pipe.DISTANCE/2)- player.y)/100
               if player.x > pipe.x: # caso ainda nao tenha sido feito ponto e o jogador passou, ponto!
                  pipe.score = True
                  add_pipe = True # se foi ponto, adicionar um cano
                  player.ia_score *= player.ia_score
                  CURRENT_PIPE_NUM += 1
      if pipe.x + pipe.sprite_width < 0: # se o pipe saiu, entra na fila de remocao.
         remove_pipes.append(pipe)
   if add_pipe:
      pipes.append(Pipe()) 
      CURRENT_PIPE = pipes[CURRENT_PIPE_NUM]
   # apenas adicionar o novo cano fora do loop.
   for pipe in remove_pipes: # remover os que ja sairam da tela.
      remove_pipes.remove(pipe)
   return add_pipe,CURRENT_PIPE # se adicionei um pipe, prox pipe.
      
def draw_all(window,birds,pipes,base,mvp_score,generation):
   window.blit(Globals.SPRITE_BG,(0,0))
   for pipe in pipes:
      pipe.draw(window)
   base.draw(window)
   for bird in birds:
      bird.draw(window)
   generation_number = Globals.SCORE_FONT.render(f'generation: {generation}',0,(0,0,0))
   score_text = Globals.SCORE_FONT.render(f'score: {mvp_score}',0,(255,255,255))
   window.blit(generation_number,(Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH/10 - generation_number.get_width(),Globals.GAME_HEIGHT - Globals.GAME_HEIGHT/10 + score_text.get_height()+10))
   window.blit(score_text,(Globals.SCREEN_WIDTH - Globals.SCREEN_WIDTH/10 - score_text.get_width(),Globals.GAME_HEIGHT - Globals.GAME_HEIGHT/10))


main()
