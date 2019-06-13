import pygame
import Enemy
import Player
import Menu
import Movement

pygame.init()

##window size
winX = 500
winY = 500
win = pygame.display.set_mode((winX, winY))

##clock reference
clock = pygame.time.Clock()

##difficulty that will increase as game progresses
difficulty = 1

##menu reference
menu = Menu.Menu()

##background image
background = pygame.image.load("Background.jpg")
font1 = pygame.font.SysFont("comicsans", 30, True)

##Levels and final page and intro
lvls = [False, False, False, False, False, False, False, False, False, False]
exitNow = False
alive = True
intro = True

##player reference
player = Player.Player(250, 410, 32, 32)

##bullet list and delay that will be incremented
bullets = []
bulletDelay = 0
score = 0

##list of enemies for each level
enemies1 = []
enemies2 = []
enemies3 = []
enemies4 = []
enemies5 = []
enemies6 = []
enemies7 = []
enemies8 = []

##shoot delay for enemies that will be incremented      
enemyShootDelay = 0

##collision between player and enemy     
def PlayerEnemyCollision(enemies):
    for a in enemies:
        ##collision between player and enemy
        if player.immunity == 0:
            if player.hitBox[1] < a.hitBox[1] + a.hitBox[3] and player.hitBox[1] + player.hitBox[3] > a.hitBox[1]:
                if player.hitBox[0] + player.hitBox[2] > a.hitBox[0] and player.hitBox[0] < a.hitBox[0] + a.hitBox[2]:
                    print("player hit")
                    enemies1.pop(enemies1.index(a))
                    player.PlayerHit()

##UI
def UI (win):
    ##changes position of score as it gets bigger
    text = font1.render("Score: " + str(score), 1, (255,255,255))
    if score < 100:
        win.blit(text, (385, 475))
    elif score < 1000:
        win.blit(text, (370, 475))
    elif score < 10000:
        win.blit(text, (355, 475))
    elif score < 100000:
        win.blit(text, (340, 475))
    
    ##displays a ship in bottom corner showing how many lives you 
    for a in range(player.lives - 1):
        win.blit(Player.Player.forward, (25 * a, 470))
  
##draw everything that will be displayed in the level
def DrawWin(EnemyList):
    ##background
    win.blit(background, (0,0))
    ##Draw player, UI, Enemies, bullets
    player.Draw(win) 
    # pickUp1.Spawn(win)
    UI(win)
    for a in EnemyList:
        a.increase += difficulty ## increase difficulty
        a.Draw(win)
    for bullet in bullets:
        bullet.Draw(win)

    ##update window
    pygame.display.update()
    
while intro:
    ##display the menu
    menu.DrawMenu(win)
    menu.Mechanics()
    lvls[0] = menu.run
    intro = menu.intro

while alive:
    ##repetitive code to spawn enemies
    for i in range(2):
        for a in range(5):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies1.append(enemy)

    for i in range(3):
        for a in range(6):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies2.append(enemy)
    
    for i in range(3):
        for a in range(7):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies3.append(enemy)
            
    for i in range(4):
        for a in range(9):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies4.append(enemy)
            
    for i in range(5):
        for a in range(10):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies5.append(enemy)
            
    for i in range(5):
        for a in range(11):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies6.append(enemy)
            
    for i in range(6):
        for a in range(11):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies7.append(enemy)
    
    for i in range(7):
        for a in range(11):
            enemy = Enemy.Enemy(10 + 40 * a, 10 + 40 * i, 40, 38, 60 + 40 * a)
            enemies8.append(enemy)
    
    ##level 1
    while lvls[0]:
        clock.tick(25)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvls[0] = False
        
        enemyCount = len(enemies1)
        print (enemyCount)
        
        ##when there are no more enemies
        ##switch to next level
        if enemyCount <= 0:
            print("Level Beat")
            lvls[1] = True
            lvls[0] = False
        
        ##delay bullet firing
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
        
        ##some collision
        player.Collision(enemies1)    
        PlayerEnemyCollision(enemies1)
             
        ##code for bullets       
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies1)
            
            ##remove bullets
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses for player movement
        Movement.Movement().Move(player, bullets, bulletDelay)
        
        ##if player is dead switch to exit screen 
        if player.escape == True:
            exitNow = True
        
        if player.run == False:
            alive = False
            lvls[0] = False
        
        ##draw window
        DrawWin(enemies1)
        
    ##level 2
    while lvls[1]:
        clock.tick(25)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        enemyCount = len(enemies2)
        print (enemyCount)
        
        if enemyCount <= 0:
            print("Level Beat")
            lvls[2] = True
            lvls[1] = False
        
        ##delay bullet firing
    
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
    
            
        player.Collision(enemies2)
        
        PlayerEnemyCollision(enemies2)
             
              
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies2)
            ##move bullet
            
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses
      
        Movement.Movement().Move(player, bullets, bulletDelay)
                
        if player.escape == True:
            exitNow = True
     
        if player.run == False:
            alive = False
            lvls[1] = False
        
        DrawWin(enemies2)
    
    ##level 3
    while lvls[2]:
        clock.tick(25)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        enemyCount = len(enemies3)
        print (enemyCount)
        
        if enemyCount <= 0:
            print("Level Beat")
            lvls[3] = True
            lvls[2] = False
        
        ##delay bullet firing
    
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
    
            
        player.Collision(enemies3)
        
        PlayerEnemyCollision(enemies3)
             
              
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies3)
            ##move bullet
            
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses
      
        Movement.Movement().Move(player, bullets, bulletDelay)
                
        if player.escape == True:
            exitNow = True
     
        if player.run == False:
            alive = False
            lvls[2] = False
        
        DrawWin(enemies3)
    
    ##level 4
    while lvls[3]:
        clock.tick(25)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvls[3] = False
        
        enemyCount = len(enemies4)
        print (enemyCount)
        
        if enemyCount <= 0:
            print("Level Beat")
            lvls[4] = True
            lvls[3] = False
        
        ##delay bullet firing
    
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
    
            
        player.Collision(enemies4)
        
        PlayerEnemyCollision(enemies4)
             
              
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies4)
            ##move bullet
            
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses
      
        Movement.Movement().Move(player, bullets, bulletDelay)
                
        if player.escape == True:
            exitNow = True
     
        if player.run == False:
            alive = False
            lvls[3] = False
        
        DrawWin(enemies4)   
    
    ##level 5
    while lvls[4]: 
        clock.tick(25)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvls[4] = False
        
        enemyCount = len(enemies5)
        print (enemyCount)
        
        if enemyCount <= 0:
            print("Level Beat")
            lvls[5] = True
            lvls[4] = False
        
        ##delay bullet firing
    
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
    
            
        player.Collision(enemies5)
        
        PlayerEnemyCollision(enemies5)
             
              
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies5)
            ##move bullet
            
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses
      
        Movement.Movement().Move(player, bullets, bulletDelay)
                
        if player.escape == True:
            exitNow = True
     
        if player.run == False:
            alive = False
            lvls[4] = False
        
        DrawWin(enemies5)  
    
    ##level 6
    while lvls[5]: 
        clock.tick(25)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvls[5] = False
        
        enemyCount = len(enemies6)
        print (enemyCount)
        
        if enemyCount <= 0:
            print("Level Beat")
            lvls[6] = True
            lvls[5] = False
        
        ##delay bullet firing
    
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
    
            
        player.Collision(enemies6)
        
        PlayerEnemyCollision(enemies6)
             
              
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies6)
            ##move bullet
            
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses
      
        Movement.Movement().Move(player, bullets, bulletDelay)
                
        if player.escape == True:
            exitNow = True
     
        if player.run == False:
            alive = False
            lvls[5] = False
        
        DrawWin(enemies6)  
    
    ##level 7
    while lvls[6]:
        clock.tick(25)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvls[6] = False
        
        enemyCount = len(enemies7)
        print (enemyCount)
        
        if enemyCount <= 0:
            print("Level Beat")
            lvls[7] = True
            lvls[6] = False
        
        ##delay bullet firing
    
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
    
            
        player.Collision(enemies7)
        
        PlayerEnemyCollision(enemies7)
             
              
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies7)
            ##move bullet
            
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses
      
        Movement.Movement().Move(player, bullets, bulletDelay)
                
        if player.escape == True:
            exitNow = True
     
        if player.run == False:
            alive = False
            lvls[6] = False
        
        DrawWin(enemies7)   
    
    ##level 8
    while lvls[7]:
        clock.tick(25)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvls[7] = False
        
        enemyCount = len(enemies8)
        print (enemyCount)
        
        if enemyCount <= 0:
            print("Level Beat")
            lvls[0] = True
            lvls[7] = False
        
        ##delay bullet firing
    
        if bulletDelay < 10:
            bulletDelay += 1
        else:
            bulletDelay = 0
    
            
        player.Collision(enemies8)
        
        PlayerEnemyCollision(enemies8)
             
              
        for bullet in bullets:
            to_remove = enemy.Collision(bullets, bullet, enemies8)
            ##move bullet
            
            if to_remove:
                score += (2 * int(difficulty))
            
            if bullet.y > 0 and to_remove == False:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    
        ##key presses
      
        Movement.Movement().Move(player, bullets, bulletDelay)
                
        if player.escape == True:
            exitNow = True
     
        if player.run == False:
            alive = False
            lvls[7] = False
        
        DrawWin(enemies8)   
    
    difficulty += 0.5
        
##exit screen
while exitNow:
    
    for event in pygame.event.get():
        if event == pygame.QUIT:
            exitNow = False
    
    ##all the text
    win.blit(background, (0,0))
    scoreText = font1.render("Your score: " + str(score), 1, (255, 255, 255))
    enterText = font1.render("press enter to quit", 1, (255, 255, 255))
    
    win.blit(endText2, (100, 200))
    win.blit(endText, (100, 250))
    win.blit(enterText, (150, 300))
    win.blit(scoreText, (100, 400))
    pygame.display.update()
    
    ##press enter to quit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        exitNow = False

pygame.quit()##exit
