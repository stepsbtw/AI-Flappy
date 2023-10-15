import pygame
import random
from Bird import Bird

class Evolution:
    def __init__(self):
        self.generation = 0

    def first_gen(self):
        players = []
        print(f'geracao: {self.generation}')
        for i in range(100):
            weights = [random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000)]
            players.append(Bird(weights))
        return players
        
    def new_gen(self, old_players):
        new_players = []
        self.generation += 1
        mvp = self.battle_royale(old_players)
        old_players.clear()
        print(f'geracao: {self.generation}')
        if mvp.ia_score > 0:
            for i in range(100):
                weights_mutate = self.mutate(mvp.weights)
                new_players.append(Bird(weights_mutate))
        else:
            new_players.append(Bird(mvp.weights))
            for i in range(99):
                weights = [random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000),random.randint(-1000,1000)]
                new_players.append(Bird(weights))
        return new_players

    #quando achar o melhor, e passar pra frente, variar!
    def mutate(self,weights): # variacao genetica dos pesos, pegar e somar uma constante pequena!
        for i in range(4):
            weight = random.randint(0,100) # peso do peso
            mutations = [weights[i] + weight, weights[i] - weight]
            weights[i] = random.choice(mutations)
        return weights

    def battle_royale(self,players):
        mvp = players[0]
        mvp_score = 0
        for player in players:
            if player.ia_score > mvp_score:
                mvp = player
                mvp_score = player.ia_score
        print(f'record : {mvp_score}')
        return mvp
