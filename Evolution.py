import pygame
import random
from Bird import Bird

class Evolution:
    def new_gen(self, players, old_players,generation):
        if not old_players:
            print('geracao 1')
            for i in range(100):
                    players.append(Bird([]))
                    generation+=1
                    return
        generation+=1
        mvp = self.battle_royale(old_players)
        if mvp.ia_score > 0: # caso haja um melhor, selecao natural!
            print('selecao natural!')
            players.clear()
            for i in range(len(old_players)):
                weights = self.mutate(mvp.weights)       
                players.append(Bird(weights))
            old_players.clear()
        else:      # caso todos sejam podres, aniquilacao, cataclisma, eclipse, apocalipse
            print('nao teve selecao')
            players.clear()
            for i in range(len(old_players)):
                    players.append(Bird([mvp.weights]))
                    return

    #quando achar o melhor, e passar pra frente, variar!
    def mutate(self,weights): # variacao genetica dos pesos, pegar e somar uma constante pequena!
        for i in range(len(weights)):
            weight = random.randint(0,100) # peso do peso
            mutations = [weights[i] + weight, weights[i] - weight]
            weights.append(random.choice(mutations))
        return weights

    def battle_royale(self,players):
        mvp = players[0]
        mvp_score = 0
        for i,player in enumerate(players):
            if players[i].ia_score > mvp_score:
                mvp_score = player.ia_score
        return mvp
