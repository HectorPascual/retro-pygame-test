import pygame

def init_pygame():
	pygame.init()
	pygame.display.init()
	pygame.display.set_caption("Arcade Game")
	screen = pygame.display.set_mode(size=[600,400], flags=pygame.RESIZABLE)

	return screen

def game_loop(screen):
	bg = pygame.image.load("bg.jpg")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
		screen.blit(bg,(0,0))
		pygame.display.update()



if __name__ == "__main__":
	screen = init_pygame()
	game_loop(screen)