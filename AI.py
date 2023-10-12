import pygame

self.weights = [0, 0] 
self.score = 0 

def vision(self, pipe): 
    deltax = self.x - pipe.x
    deltay = self.y - (pipe.y + pipe.y_invert)/2
    return (deltax,deltay)
  
def think(self,deltas):
    if deltas[0] < deltas[1]:
        self.jump()

def distance(deltaxy):
    return sqrt(delta[0]**2 + delta[1]**2)

# falta adicionar o sistema de peso