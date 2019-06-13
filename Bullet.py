import pygame

##bullet class
class Bullet(object):
    def __init__(self, x, y, radius, color):
        ##initialize position, color, and radius
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8
    
    ##draw
    def Draw(self, win):
        pygame.draw.circle(win, self.color, (round(self.x),round( self.y)), self.radius)
    
    ##update position 
    def update(self):
        self.y += self.vel