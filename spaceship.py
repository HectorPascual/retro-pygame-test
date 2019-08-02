import pygame

class Shot(pygame.sprite.Sprite):

    def __init__(self, ship):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("assets/bullet_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = ship.rect.x+30
        self.rect.y = ship.rect.y-10

    def update(self, screen):
            self.rect.y -=2
            screen.blit(self.image,(self.rect.x, self.rect.y))
          

class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/ship.png")
        self.rect = self.image.get_rect()
        self.rect.x = 290
        self.rect.y = 300

    def handle_keys(self, screen):  
        key = pygame.key.get_pressed()
        dist = 4
        if key[pygame.K_DOWN] and self.rect.y < screen.get_height()-70: 
            self.rect.y += dist 
        elif key[pygame.K_UP] and self.rect.y >= 0: 
            self.rect.y -= dist 
        if key[pygame.K_RIGHT] and self.rect.x < screen.get_width()-70: 
            self.rect.x += dist 
        elif key[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= dist 


    def draw(self, screen):
        self.handle_keys(screen)
        screen.blit(self.image, (self.rect.x, self.rect.y))
