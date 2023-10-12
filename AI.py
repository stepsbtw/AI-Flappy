import pygame
import random

self.weights = [0, 0] 
self.score = 0 

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
         weight = random.randrange(0,1000)
         mutations = [inputs[i] + weight, inputs[i] - weight]
         inputs[i] = random.choice(list_mutation) 
  
     return inputs


# falta adicionar o sistema de peso