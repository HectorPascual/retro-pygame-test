import pygame

class Shot():
    def __init__(self, ship):
        self.x = ship.x+30
        self.y = ship.y-10
        self.bullet_1 = pygame.image.load("bullet_1.png")
        self.bullet_2 = pygame.image.load("bullet_2.png")
        self.id = 0 

    def update(self, screen):
            self.y -=2
            if self.id%2 == 0:
                screen.blit(self.bullet_1,(self.x, self.y))
            else: 
                screen.blit(self.bullet_2,(self.x, self.y))
            self.id +=1


class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.image.load("ship.png")
       self.x = 0
       self.y = 0

    

    def handle_keys(self, screen):  
        key = pygame.key.get_pressed()
        dist = 4
        if key[pygame.K_DOWN] and self.y < screen.get_height()-70: 
            self.y += dist 
        elif key[pygame.K_UP] and self.y >= 0: 
            self.y -= dist 
        if key[pygame.K_RIGHT] and self.x < screen.get_width()-70: 
            self.x += dist 
        elif key[pygame.K_LEFT] and self.x >= 0:
            self.x -= dist 


    def draw(self, screen):
        self.handle_keys(screen)
        screen.blit(self.image, (self.x, self.y))
