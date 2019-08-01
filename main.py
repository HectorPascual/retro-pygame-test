import pygame
from spaceship import *

def init_pygame():
	pygame.init()
	pygame.display.init()
	pygame.display.set_caption("Arcade Game")
	screen = pygame.display.set_mode(size=[600,400], flags=pygame.RESIZABLE)

	return screen

def game_loop(screen):
    bg = pygame.image.load("bg.jpg")
    clock = pygame.time.Clock()
    ship = Spaceship()
    bullets = []
    oldtime = 0
    while True:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT: 
    			sys.exit()

    	screen.blit(bg,(0,0))
    	ship.draw(screen)

        newtime = pygame.time.get_ticks()
        if newtime - oldtime > 400:
            oldtime = newtime
            bullets.append(Shot(ship))
        
        for bullet in bullets:
            bullet.update(screen)
    	pygame.display.update()
    	clock.tick(60)


if __name__ == "__main__":
	screen = init_pygame()
	game_loop(screen)