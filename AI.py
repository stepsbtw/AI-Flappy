import pygame

self.weights = [0, 0] 
self.score = 0 

def vision(self, pipe): 
    deltax = self.x - pipe.x
    deltay = self.y - (pipe.y + pipe.y_invert)/2
    think(deltax, deltay)
  
def think(self, deltax, deltay):
    if deltax < deltay:
        self.jump()

# falta adicionar o sistema de peso