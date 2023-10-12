import pygame
import random

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


# falta adicionar o sistema de peso