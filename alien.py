import pygame
import random


class Alien(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,580)
        self.rect.y = 0

    def update(self, screen):
            self.rect.y += 1
            screen.blit(self.image,(self.rect.x, self.rect.y))