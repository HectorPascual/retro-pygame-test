import pygame
import sys
from spaceship import *
import random
from alien import Alien

RESTART_GAME = -1
EXIT_GAME = -2

def init_pygame():
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Arcade Game")
    screen = pygame.display.set_mode(size=[600,400], flags=pygame.RESIZABLE)

    return screen


def game_loop(screen):
    bg = pygame.image.load("assets/bg.jpg")
    clock = pygame.time.Clock()
    ship = Spaceship()
    bullets = []
    aliens = []
    oldtime_bullet = 0
    oldtime_alien = 0
    newtime = 0
    score = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(bg,(0,0))
        ship.draw(screen)
        if newtime == 0:
            start(screen, bg)
        newtime = pygame.time.get_ticks()
        if newtime - oldtime_bullet > 400:
            oldtime_bullet = newtime
            bullets.append(Shot(ship))

        if newtime - oldtime_alien > random.randint(800, 1700):
            oldtime_alien = newtime
            aliens.append(Alien(oldtime_alien % 3 + 1))

        for bullet in bullets:
            bullet.update(screen)

        for alien in aliens:
            alien.update(screen)
            if alien.rect.y >= screen.get_height():
                action = show_gameover(screen, score)
                return action

        for bullet in bullets:
            for alien in aliens:
                if pygame.sprite.collide_rect(bullet, alien):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    score += 1
                    break
        update_score(screen, score)
        pygame.display.update()
        clock.tick(60)


def update_score(screen, score):
    font = pygame.font.Font('fonts/game_over.ttf', 32)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (560, 15)
    screen.blit(score_text, score_text_rect)


def start(screen, bg):
    font = pygame.font.Font('fonts/game_over.ttf',128)
    count = 3
    count_text = font.render(str(count), True, (0,0,0))
    count_text_rect = count_text.get_rect()
    count_text_rect.center = (300,200)

    while count > 0:
        screen.blit(bg,(0,0))
        screen.blit(count_text, count_text_rect)
        count -= 1
        count_text = font.render(str(count), True, (0, 0, 0))
        pygame.display.update()
        pygame.time.delay(1000)

def show_gameover(screen, score):

    font = pygame.font.Font('fonts/game_over.ttf',128)
    font_small = pygame.font.Font('fonts/game_over.ttf',32)
    gameover = font.render('GAME OVER', True, (0, 0, 0))
    play_again = font_small.render('Press SPACE to play again or ESCAPE to exit', True, (0,0,0))

    play_again_rect = play_again.get_rect()
    play_again_rect.center = (300,260)
    gameover_rect = gameover.get_rect()
    gameover_rect.center = (300, 200)
    clock = pygame.time.Clock()

    font = pygame.font.Font('fonts/game_over.ttf', 64)
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (300, 150)
    while True:
        screen.blit(gameover, gameover_rect)
        screen.blit(play_again, play_again_rect)
        screen.blit(score_text, score_text_rect)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            return RESTART_GAME
        elif key[pygame.K_ESCAPE]:
            return EXIT_GAME
        pygame.display.update()
        pygame.event.pump()
        clock.tick(60)


if __name__ == "__main__":
    screen = init_pygame()
    action = RESTART_GAME
    while action == RESTART_GAME:
        action = game_loop(screen)
    sys.exit()
