import pygame
import Bullet
import random

##Enemy class
class Enemy(object):
    enemy1Sprite = pygame.image.load("Enemy01.png")
    explosion = [pygame.image.load("Explosion1.png"), pygame.image.load("Explosion2.png"), pygame.image.load("Explosion3.png"), pygame.image.load("Explosion4.png"), pygame.image.load("Explosion5.png"), pygame.image.load("Explosion6.png"), pygame.image.load("Explosion7.png"), pygame.image.load("Explosion8.png"), pygame.image.load("Explosion9.png"), pygame.image.load("Explosion10.png"), pygame.image.load("Explosion11.png"), pygame.image.load("Explosion12.png"), pygame.image.load("Explosion13.png"), pygame.image.load("Explosion14.png"), pygame.image.load("Explosion15.png")]
    
    def __init__(self, x, y, width, height, end):
        ##initialize variables
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.vel = .5
        self.facing = 1
        self.hitBox = (self.x, self.y, 35, 38)
        self.bullets = []
        self.increase = 1
        self.delay = random.randint(50, 300 / self.increase)
        self.count = 1
        self.walkCount = 0
        self.died = False
    
    ##shooting
    def Shoot(self, win):
        
        if self.count < self.delay:
            self.count += 1
        else:
            self.count = 0
            
        if len(self.bullets) < 5 and self.count == 0:
            self.bullets.append(Bullet.Bullet(self.x, self.y, 7, (255, 0, 0)))
        
         
        for bullet in self.bullets:
            bullet.update()
            bullet.Draw(win)
            print("bullet")
            if bullet.y > 500:
                print("Pop")
                self.bullets.pop(self.bullets.index(bullet))
            
        
    ##draw               
    def Draw(self, win):
        
        self.Shoot(win)
        
        win.blit(self.enemy1Sprite, (self.x, self.y))
        
        if self.vel > 0:
            if self.x < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
        else:
            if self.x > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
        
        self.hitBox = (self.x, self.y, 35, 38)
        #pygame.draw.rect(win, (255, 0, 0), (self.hitBox[0], self.hitBox[1], self.hitBox[2], self.hitBox[3]), 2)
    
    
    ##collision
    def Collision(self, bullets, bullet, enemies):
        for enemy in enemies:
            if bullet.y - bullet.radius < enemy.hitBox[1] + enemy.hitBox[3] and bullet.y + bullet.radius > enemy.hitBox[1]:
                if bullet.x + bullet.radius > enemy.hitBox[0] and bullet.x + bullet.radius < enemy.hitBox[0] + enemy.hitBox[2]:
                    #bullets.pop(bullets.index(bullet))
   
                    print ("enemy hit")
                    enemies.pop(enemies.index(enemy))
                    return True
        return False
