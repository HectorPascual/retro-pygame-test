import pygame
import random


class Alien(pygame.sprite.Sprite):

    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,570)
        self.rect.y = 0
        self.speed = speed

    def update(self, screen):
        self.rect.y += self.speed
        screen.blit(self.image,(self.rect.x, self.rect.y))