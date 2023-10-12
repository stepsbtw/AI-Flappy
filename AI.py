import pygame
import random

def eyes(self, deltas):
    best_distance = 

def brain(self, foods):
    receptors = self.eyes()
    if receptors == None:
        return

    outputs = [0, 0]

    outputs[0] = (receptors[1] * self.inputs[0]) + (receptors[0] * self.inputs[2])
    outputs[1] = (receptors[1] * self.inputs[1]) + (receptors[0] * self.inputs[3])

     self.decision(outputs[0], outputs[1])


class Generations:
    def __init__(self, generation):
        self.generation = generation

    def new_gen(self, players):
        self.generation += 1
        mvp = self.mvp(creatures)
        players.remove_all()
        if mvp.score > 0:
            for i in range(num_players):
                mvp_weights = mutate(mvp.weights)         
                players.append(Player(weights = mvp_weights))
        else:
            mvp_weights = mvp.weights
            creatures.append(Player(weights = mvp_weights))
            for i in range(num_players-1):
                players.append(Player())

        players.remove_all()

    def mvp(players):
        mvp = players[0]
        best = 0
        for player in players:
            if players.score > best:
                best = player.best
                mvp = player
        return mvp


if not have_brain:
    self.weights = [random.randInt(-100,100),random.randInt(-100,100),random.randInt(-100,100),random.randInt(-100,100)] 
self.score = 0 
    have_brain = True
else:
    self.weights = weights

def vision(self, pipe): 
    deltax = self.x - pipe.x
    deltay = self.y - (pipe.y + pipe.y_invert)/2
    return (deltax,deltay)
  
def think(self,deltas):
    if deltas[0] < deltas[1]:
        self.jump()

def distance(deltas):
    return sqrt(deltas[0]**2 + deltas[1]**2)

def mutation(inputs):
     for i in range(len(inputs)):
         weight = random.randrange(0,100)
         mutations = [inputs[i] + weight, inputs[i] - weight]
         inputs[i] = random.choice(list_mutation) 
  
     return inputs
