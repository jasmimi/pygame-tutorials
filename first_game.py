import pygame

pygame.init()

#Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Game loop
run = True
while run:
	#Event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

pygame.quit()
