# name: move_rect.py
# author: Jasmine Amohia
# date: 20/08/24
# desc: move red rectangle in window

import pygame

pygame.init()

#Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#4 args: xcord, ycord, height, width
player = pygame.Rect((300, 250, 50, 50))

#Game loop
run = True
while run:
	
	screen.fill((0, 0, 0))
	
	pygame.draw.rect(screen, (255, 0, 0), player)

	key = pygame.key.get_pressed()
	if key[pygame.K_a] == True:
		player.move_ip(-1, 0)
	elif key[pygame.K_d] == True:
		player.move_ip(1, 0)
	elif key[pygame.K_w] == True:
		player.move_ip(0, -1)
	elif key[pygame.K_s] == True:
		player.move_ip(0, 1) 

	#Event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update() #Refresh screen

pygame.quit()
