import pygame

##player class
class Player(object):
    
    ##sprites
    goRight = [pygame.image.load("R1.png"), pygame.image.load("R2.png"), pygame.image.load("R3.png"), pygame.image.load("R4.png"), pygame.image.load("R5.png"), pygame.image.load("R6.png")]
    goLeft = [pygame.image.load("L1.png"), pygame.image.load("L2.png"), pygame.image.load("L3.png"), pygame.image.load("L4.png"), pygame.image.load("L5.png"), pygame.image.load("L6.png")]
    forward = pygame.image.load("top.png")
    shield = pygame.image.load("Shield.png")
    explosion = [pygame.image.load("Explosion1.png"), pygame.image.load("Explosion2.png"), pygame.image.load("Explosion3.png"), pygame.image.load("Explosion4.png"), pygame.image.load("Explosion5.png"), pygame.image.load("Explosion6.png"), pygame.image.load("Explosion7.png"), pygame.image.load("Explosion8.png"), pygame.image.load("Explosion9.png"), pygame.image.load("Explosion10.png"), pygame.image.load("Explosion11.png"), pygame.image.load("Explosion12.png"), pygame.image.load("Explosion13.png"), pygame.image.load("Explosion14.png"), pygame.image.load("Explosion15.png")]
    
    def __init__(self, x, y, width, height):
        ##initialize variables
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4
        self.walkCount = 0
        self.faceRight = False
        self.faceLeft = False
        self.hitBox = (self.x + 3, self.y + 2, 25, 28)
        self.lives = 3
        self.immunity = 0
        self.score = 0
        self.run = True
        self.escape = False
        self.died = False
    
    ##draw player with animations and shield and explosion anim    
    def Draw(self, win): 
        if self.walkCount > 15:
            self.walkCount = 0
        elif self.walkCount < 15 and self.died:
            self.walkCount += 1
        
        if self.died:
            self.Explosion(win)
            if self.walkCount == 15:
                self.x = 250
                self.y = 450
                self.died = False
            
        
        elif self.died == False:
            if self.faceRight == False and self.faceLeft == False:
                win.blit(self.forward, (self.x, self.y))
                self.walkCount = 0
                
            if self.faceRight:
                if self.walkCount < 15:
                    win.blit(self.goRight[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.goRight[5], (self.x, self.y))
            
            
            if self.faceLeft:
                if self.walkCount < 15:
                    win.blit(self.goLeft[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
                    
                else:
                    win.blit(self.goLeft[5], (self.x, self.y))
        
               
                    #pygame.draw.rect(win, (255, 0 , 0), (self.hitBox[0], self.hitBox[1], self.hitBox[2], self.hitBox[3]), 2)
    
            if self.immunity > 0:
                self.immunity -= 1
                win.blit(self.shield, (self.x - 2, self.y))
        self.hitBox = (self.x + 3, self.y + 2, 25, 28)    
    
    ##collision for colidding with enemy bullets
    def Collision(self, enemies):
        if self.immunity == 0:
            for enemy in enemies:
                for bullet in enemy.bullets:
                    if bullet.y - bullet.radius < self.hitBox[1] + self.hitBox[3] and bullet.y + bullet.radius > self.hitBox[1]:
                        if bullet.x + bullet.radius > self.hitBox[0] and bullet.x + bullet.radius < self.hitBox[0] + self.hitBox[2]:
                            print("PLAYER SHOT")
                            self.died = True
                            self.PlayerHit()
                            self.score -= 10
    
    ##explosion anim
    def Explosion(self, win):
        if self.walkCount < 15:
            win.blit(self.explosion[self.walkCount], (self.x, self.y))
            self.walkCount
    
    ##what happens when player gets hit                   
    def PlayerHit(self):
        self.lives -= 1
        self.died = True
        self.immunity = 100
        if self.lives <= 0:
            #pygame.display.quit()
            self.run = False
            self.escape = True
