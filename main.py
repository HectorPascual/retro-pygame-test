import pygame
import sys
from spaceship import *
from alien import Alien

def init_pygame():
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Arcade Game")
    screen = pygame.display.set_mode(size=[600,400], flags=pygame.RESIZABLE)

    return screen

def game_loop(screen):
    in_game = True
    bg = pygame.image.load("assets/bg.jpg")
    clock = pygame.time.Clock()
    ship = Spaceship()
    bullets = []
    aliens = []
    oldtime_bullet = 0
    oldtime_alien = 0
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        screen.blit(bg,(0,0))
        ship.draw(screen)

        newtime = pygame.time.get_ticks()
        if newtime - oldtime_bullet > 400:
            oldtime_bullet = newtime
            bullets.append(Shot(ship))    

        if newtime - oldtime_alien > 1000:
            oldtime_alien = newtime
            aliens.append(Alien())

        for bullet in bullets:
            bullet.update(screen)

        for alien in aliens:
            alien.update(screen)
            if alien.rect.y == screen.get_height():
                in_game = False
                return

        for bullet in bullets:
            for alien in aliens:
                if pygame.sprite.collide_rect(bullet, alien):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    break

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    screen = init_pygame()
    game_loop(screen)
    print("Game Over")
