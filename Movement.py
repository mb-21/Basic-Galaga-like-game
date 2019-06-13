import pygame
import Bullet

##movement class
class Movement():
    
    def __init__(self):
        self.keys = pygame.key.get_pressed()
    
    ##key presses
    def Move(self, player, bullets, bulletDelay):
        if player.died == False:
            if self.keys[pygame.K_SPACE] and bulletDelay == 0:  
                bullets.append(Bullet.Bullet(round(player.x + player.width // 2), round(player.y - player.height // 2), 6, (255, 255, 255)))
           
            if self.keys[pygame.K_UP] and player.y > 0:
                player.y -= player.vel
                player.faceRight = False
                player.faceLeft = False
                
            if self.keys[pygame.K_DOWN] and player.y < 500 - player.height:
                player.y += player.vel
                player.faceRight = False
                player.faceLeft = False
                
            if self.keys[pygame.K_RIGHT] and player.x < 500 - player.width:
                player.x += player.vel
                player.faceRight = True 
                player.faceLeft = False
                
            if self.keys[pygame.K_LEFT] and player.x > 0:
                player.x -= player.vel
                player.faceRight = False
                player.faceLeft = True