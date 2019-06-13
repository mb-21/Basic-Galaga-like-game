import pygame

##menu class
class Menu(object):
    
    def __init__(self):
        ##initilize variables
        self.text = " Use arrow keys to move"
        self.text1 = "Spacebar to shoot"
        self.text2 = "Don't let the enemies shoot you"
        
        self.intro = True
        self.run = False
        
        self.titleFont = pygame.font.SysFont("comicsans", 50, True)
        self.subFont = pygame.font.SysFont("sans", 20, False, True)
        self.title = self.titleFont.render("Spaceship Defender", 1, (255,255,255))
        self.message1 = self.subFont.render(self.text, 1, (255,255,255))
        self.message2 = self.subFont.render(self.text1, 1, (255, 255, 255))
        self.message3 = self.subFont.render(self.text2, 1, (255, 255, 255))
        self.sub = self.subFont.render("Press Enter To Start", 1, (255,255,255))
    
    ##display
    def DrawMenu(self, win):
        win.blit(self.title, (55, 150))
        win.blit(self.sub, (160, 300))
        win.blit(self.message1, (155, 350))
        win.blit(self.message2, (180, 370))
        win.blit(self.message3, (135, 390))
        
        pygame.display.update()
    
    ##key presses   
    def Mechanics(self):
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.intro = False
                
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            self.run = True
            self.intro = False   